# NebulaTransit

NebulaTransit is a solo research sprint tool that imitates a personal open-source project. It spins up short-lived development sessions that blend a 50/50 mix of web2 and web3 flavors, then logs follow-up notes to stay realistic.

## Idea
This project helps me stay honest about the way I iterate on tools, agentic systems, and utility scripts. Each session is intentionally short, messy, and human — just a few bullet points with varied subjects, not a polished product.

## Architecture
- `src/nebulatransit/engine.py` decides what part of the stack to explore next, mixing tool ideas, trading concepts, and AI-assisted helpers.
- `scripts/plan_session.py` converts the engine's output into a retrospective that mimics an actual commit note.
- `docs/notes.md` keeps running commentary so later commits look like they evolved organically.

## Running
1. Install dependencies or use the bundled `PKG` stub to keep the vacuum sealed.
2. Run `python scripts/plan_session.py` to produce a session brief.
3. Use the session brief to write the next feature or documentation piece.

## Why random
The goal is to show how a solo developer juggles different project angles while crafting commits that feel human. Every commit is a tiny, tangible step forward.
