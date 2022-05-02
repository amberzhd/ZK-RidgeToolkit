#!/usr/bin/env python3
"""Append a handcrafted entry to the notebook without relying on randomness."""

from argparse import ArgumentParser
from datetime import datetime
from typing import List

from nebulatransit.engine import NebulaTransitEngine, SessionDraft
from nebulatransit.journal import SessionJournal


def split_notes(value: str) -> List[str]:
    return [line.strip() for line in value.split(";") if line.strip()]


def main() -> None:
    parser = ArgumentParser(description="Create a manual journal entry for NebulaTransit.")
    parser.add_argument("--focus", required=True, help="Describe the focus for the entry")
    parser.add_argument("--stack", required=True, help="Describe the stack mix")
    parser.add_argument("--goal", required=True, help="Describe the deliverable")
    parser.add_argument("--notes", default="", help="Semicolon-separated notes")
    parser.add_argument("--timestamp", help="ISO timestamp to write into the entry")
    args = parser.parse_args()

    engine = NebulaTransitEngine()
    session = SessionDraft(
        focus=args.focus,
        stack_mix=args.stack,
        deliverable=args.goal,
        notes=split_notes(args.notes) or ["Manual touch-up noted in the journal."],
    )
    journal = SessionJournal()
    journal.append_entry(session, engine, timestamp=args.timestamp or datetime.utcnow().replace(microsecond=0).isoformat())
    print("Wrote manual entry to docs/notes.md")


if __name__ == "__main__":
    main()
