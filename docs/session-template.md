# Session Template

Use this outline before each commit to keep the journal entry grounded:

1. `Focus:` Describe what single thread you chased (agentic workflow, bot build, data sketch, etc.).
2. `Stack:` List the combination of web2/web3 pieces you explored; mention the full tuple even if you only prototyped part of it.
3. `Goal:` Share the deliverable or experiment you touched that day.
4. `Notes:` Keep it conversational — mention constraints, quick wins, or what still feels rough.

Sample entry:

```
---
timestamp: 2022-04-12T19:47:22
Focus: Exploring bot-assisted trading chops
Stack: Electron + SQLite + Ethereum + Graph
Goal: sketch a CLI helper for deployment
Notes: Tried injecting signed payloads and logged the failures; still worried about silent errors, so I left a TODO.
```

Refer to this before running `scripts/plan_session.py` so the autotune stays human.
