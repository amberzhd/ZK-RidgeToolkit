#!/usr/bin/env python3
from nebulatransit.engine import NebulaTransitEngine
from nebulatransit.journal import SessionJournal


def main():
    engine = NebulaTransitEngine()
    session = engine.draft_session()
    journal = SessionJournal()
    journal.append_entry(session, engine)


if __name__ == "__main__":
    main()
