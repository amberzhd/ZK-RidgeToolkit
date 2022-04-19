# NebulaTransit

NebulaTransit is a solo research sprint tool that imitates a personal open-source project. It spins up short-lived development sessions that blend a 50/50 mix of web2 and web3 flavors, then logs follow-up notes to stay realistic.

## Idea
This project helps me stay honest about the way I iterate on tools, agentic systems, and utility scripts. Each session is intentionally short, messy, and human — just a few bullet points with varied subjects, not a polished product.

## Architecture
- `src/nebulatransit/engine.py` decides what part of the stack to explore next, mixing tool ideas, trading concepts, and AI-assisted helpers.
- `scripts/plan_session.py` converts the engine's output into a retrospective that mimics an actual commit note.
- `docs/notes.md` keeps running commentary so later commits look like they evolved organically.

## Running
1. Install dependencies with `pip install -r requirements.txt` or grab the bundled `PKG` stub if you just want to browse the code.
2. Run `python scripts/plan_session.py` to append a fresh entry to the journal (`docs/notes.md`).
3. Read the last couple of entries with `python scripts/review_journal.py -n 5` before drafting the next bite-sized change.
4. Let the journal remind you why every commit stays human-feeling, even if the code is a sketch.
5. When inspiration runs dry, run `python scripts/list_stack_combos.py` to see new stack blends and pick a fresh focus.

## Journal module
- `src/nebulatransit/journal.py` keeps the log file tidy, exposes `SessionJournal`, and lets tests simulate writing without touching the real notes.
- The journaling layer now shares the same brief logic as the engine so the file stays consistent, and the review script can reprint a few entries for quick context.

## Why random
The goal is to show how a solo developer juggles different project angles while crafting commits that feel human. Every commit is a tiny, tangible step forward.
