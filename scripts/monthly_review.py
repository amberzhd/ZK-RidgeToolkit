#!/usr/bin/env python3
"""Show how the journal has trended over the months."""

from argparse import ArgumentParser
from collections import Counter
from datetime import datetime
from typing import List, Optional

from nebulatransit.journal import SessionJournal


def parse_timestamp(entry: str) -> Optional[datetime]:
    for line in entry.splitlines():
        if line.startswith("timestamp:"):
            value = line.split("timestamp:", 1)[1].strip()
            try:
                return datetime.fromisoformat(value)
            except ValueError:
                return None
    return None


def main() -> None:
    parser = ArgumentParser(description="Summarize journal activity by month.")
    parser.add_argument("-n", "--limit", type=int, default=5, help="Show the last N entries")
    args = parser.parse_args()
    journal = SessionJournal()
    entries = journal.read_entries()
    if not entries:
        print("No entries recorded yet.")
        return
    timestamps: List[datetime] = [ts for ts in (parse_timestamp(entry) for entry in entries) if ts is not None]
    month_counts = Counter(ts.strftime("%Y-%m") for ts in timestamps)
    print("Entry counts by month:")
    for month, count in sorted(month_counts.items()):
        print(f"- {month}: {count}")
    print("\nRecent entries:\n")
    recent = entries[-args.limit:]
    for block in recent:
        print(block)
        print()


if __name__ == "__main__":
    main()
