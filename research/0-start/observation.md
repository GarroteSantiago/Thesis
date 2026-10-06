---
id: observation
row: 0
by: me
status: provisional
inputs: []
---
# Observation

Message abstractions (OOP, actors) are used in languages, agents and networks, but not in operating systems, hardware and low-level programming. Below that point, systems rest on primitives that break their own rules, so they cannot define themselves.

## How I noticed it
While coding and studying in different situations:
- While coding parallel algorithms in C, Rust and assembly, I noticed that the machine still works imperatively, both in its instruction set and in its whole model of threads and shared memory, while we programmers think and design in objects and messages. Going down to the machine costs effort and loses features on the way, i.e. encapsulation.
- While writing an interpreter in Java, I noticed that an interpreter mostly reads text and maps it onto operations written in the host language, instead of dispatching objects' behaviours or even function calls. The language rests on primitives that are not part of it, so it cannot define itself. Smalltalk is the exception, defining itself in its own objects and messages above its virtual machine. A system should define itself, without escape routes that are exceptions to its own rules: a system that breaks its own rules cannot be taken seriously. The idea of this thesis is to realize Smalltalk's idea all the way down.
- While seeing how microservices work, I noticed that networked systems communicate only through messages and isolate their state, which lets layers be put in between (interposition: proxies, load balancers, firewalls, monitors) without changing either side. Machines at a low level still expose their state as global and shared in hardware, where layers cannot be put in between the way the network allows, even though the field knows the consequences.
