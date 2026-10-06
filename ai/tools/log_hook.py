#!/usr/bin/env python3
"""Raw AI log: append every Claude Code hook event to research/ai-log/raw/<session>.jsonl.

Wired in .claude/settings.json. Never blocks or fails a session: every error is swallowed.
See ai/ai-log.md.
"""
import json
import os
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path


def main() -> None:
    raw = sys.stdin.read()
    event = json.loads(raw)
    root = Path(os.environ.get("CLAUDE_PROJECT_DIR") or event.get("cwd") or ".")
    session = event.get("session_id", "unknown")
    log_dir = root / "research" / "ai-log" / "raw"
    log_dir.mkdir(parents=True, exist_ok=True)

    entry = {"ts": datetime.now(timezone.utc).isoformat(), **event}
    with open(log_dir / f"{session}.jsonl", "a", encoding="utf-8") as f:
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
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
