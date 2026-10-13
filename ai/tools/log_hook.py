#!/usr/bin/env python3
"""Raw AI log: append every Claude Code hook event to research/ai-log/raw/<session>.jsonl.

Wired in .claude/settings.json. Never blocks or fails a session: every error is swallowed.
Binary payloads (base64 fields, e.g. page images read by an agent) are replaced by their
sha256 and size; all text is kept. A log part over MAX_PART bytes continues in
<session>.2.jsonl, <session>.3.jsonl, ...

`log_hook.py --compact FILE...` applies the same replacement to logs written before it.
See ai/ai-log.md.
"""
import base64
import hashlib
import json
import os
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

MAX_PART = 40_000_000


def strip_binary(value):
    """Replace every base64 field with its sha256, size and the fact it was omitted."""
    if isinstance(value, dict):
        out = {}
        for key, item in value.items():
            if key == "base64" and isinstance(item, str):
                try:
                    data = base64.b64decode(item, validate=False)
                except Exception:
                    data = item.encode()
                out[key] = {"omitted": "binary", "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)}
            else:
                out[key] = strip_binary(item)
        return out
    if isinstance(value, list):
        return [strip_binary(item) for item in value]
    return value


def part_path(log_dir: Path, session: str, n: int) -> Path:
    return log_dir / (f"{session}.jsonl" if n == 1 else f"{session}.{n}.jsonl")


def log_part(log_dir: Path, session: str) -> Path:
    """The newest part of the session's log; a new one once it is over MAX_PART."""
    n = 1
    while part_path(log_dir, session, n + 1).is_file():
        n += 1
    path = part_path(log_dir, session, n)
    if path.is_file() and path.stat().st_size > MAX_PART:
        path = part_path(log_dir, session, n + 1)
    return path


def compact(path: Path) -> None:
    """Rewrite one log with binary payloads stripped. Lines appended meanwhile are kept."""
    tmp = path.with_suffix(".compacting")
    with open(path, "rb") as src, open(tmp, "w", encoding="utf-8") as dst:
        for line in src:
            try:
                dst.write(json.dumps(strip_binary(json.loads(line)), ensure_ascii=False) + "\n")
            except ValueError:
                dst.write(line.decode("utf-8", "replace"))
        rest = src.read()
        if rest:
            dst.write(rest.decode("utf-8", "replace"))
    os.replace(tmp, path)


def main() -> None:
    raw = sys.stdin.read()
    event = json.loads(raw)
    root = Path(os.environ.get("CLAUDE_PROJECT_DIR") or event.get("cwd") or ".")
    session = event.get("session_id", "unknown")
    log_dir = root / "research" / "ai-log" / "raw"
    log_dir.mkdir(parents=True, exist_ok=True)

    entry = {"ts": datetime.now(timezone.utc).isoformat(), **strip_binary(event)}
    with open(log_part(log_dir, session), "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    name = event.get("hook_event_name")
    if name in ("Stop", "SubagentStop", "SessionEnd", "PreCompact"):
        transcript = event.get("transcript_path")
        if transcript and Path(transcript).is_file():
            shutil.copyfile(transcript, log_dir / f"{session}.transcript.jsonl")
    if name == "SessionStart":
        # Stdout of SessionStart is added to the model's context: the gate needs the session ID.
        print(f"Raw AI log session: {session} (research/ai-log/raw/{session}.jsonl)")


if __name__ == "__main__":
    if sys.argv[1:2] == ["--compact"]:
        for name in sys.argv[2:]:
            compact(Path(name))
        sys.exit(0)
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
