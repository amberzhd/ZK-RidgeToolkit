#!/usr/bin/env python3
from datetime import datetime
from pathlib import Path
from nebulatransit.engine import NebulaTransitEngine

NOTES_FILE = Path(__file__).resolve().parents[1] / "docs" / "notes.md"


def append_session(session, engine):
    timestamp = datetime.utcnow().isoformat(timespec="seconds")
    block = ["---", f"timestamp: {timestamp}"]
    block.extend(engine.brief(session))
    block.append("\n")
    with NOTES_FILE.open("a", encoding="utf-8") as out:
        out.write("\n".join(block))


def main():
    engine = NebulaTransitEngine()
    session = engine.draft_session()
    NOTES_FILE.parent.mkdir(parents=True, exist_ok=True)
    append_session(session, engine)


if __name__ == "__main__":
    main()
