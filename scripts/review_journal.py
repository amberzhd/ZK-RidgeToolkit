#!/usr/bin/env python3
"""Print a quick review of the most recent session entries."""

from argparse import ArgumentParser

from nebulatransit.journal import SessionJournal


def main() -> None:
    parser = ArgumentParser(description="Show the last few NebulaTransit notes.")
    parser.add_argument("-n", "--limit", type=int, default=3, help="How many entries to show")
    args = parser.parse_args()
    journal = SessionJournal()
    entries = journal.read_entries()
    if not entries:
        print("No journal entries yet, run scripts/plan_session.py first.")
        return
    excerpt = entries[-args.limit:]
    print("Recent entries:\n")
    for block in excerpt:
        print(block)
        print()


if __name__ == "__main__":
    main()
