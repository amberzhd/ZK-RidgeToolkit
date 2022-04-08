from pathlib import Path

from nebulatransit.engine import NebulaTransitEngine
from nebulatransit.journal import SessionJournal


def test_render_entry_includes_timestamp(tmp_path: Path) -> None:
    engine = NebulaTransitEngine()
    session = engine.draft_session()
    journal = SessionJournal(notes_file=tmp_path / "notes.md")
    timestamp = "2022-04-05T09:12:34"
    entry = journal.render_entry(session, engine, timestamp)
    assert f"timestamp: {timestamp}" in entry
    assert session.focus in entry


def test_append_entry_creates_note_file(tmp_path: Path) -> None:
    engine = NebulaTransitEngine()
    session = engine.draft_session()
    journal = SessionJournal(notes_file=tmp_path / "notes.md")
    journal.append_entry(session, engine, timestamp="2022-04-06T11:19:07")
    text = (tmp_path / "notes.md").read_text()
    assert "timestamp: 2022-04-06T11:19:07" in text


def test_read_entries_returns_blocks(tmp_path: Path) -> None:
    sample = tmp_path / "notes.md"
    sample.write_text("# Journal\n---\ntimestamp: 2022-04-01T00:00:01\nFocus: debug\n---\n")
    journal = SessionJournal(notes_file=sample)
    entries = journal.read_entries()
    assert len(entries) == 1
    assert "Focus: debug" in entries[0]
