from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import List, Optional

from nebulatransit.engine import NebulaTransitEngine, SessionDraft


class SessionJournal:
    """Utility to append and inspect session notes."""

    def __init__(self, notes_file: Optional[Path] = None) -> None:
        self.notes_file = (
            notes_file
            if notes_file is not None
            else Path(__file__).resolve().parents[1] / "docs" / "notes.md"
        )

    def render_entry(self, session: SessionDraft, engine: NebulaTransitEngine, timestamp: str) -> str:
        header = ["---", f"timestamp: {timestamp}"]
        header.extend(engine.brief(session))
        header.append("")
        return "\n".join(header)

    def append_entry(
        self,
        session: SessionDraft,
        engine: NebulaTransitEngine,
        timestamp: Optional[str] = None,
    ) -> None:
        ts = timestamp or datetime.utcnow().replace(microsecond=0).isoformat()
        entry = self.render_entry(session, engine, ts)
        self.notes_file.parent.mkdir(parents=True, exist_ok=True)
        has_content = self.notes_file.exists() and self.notes_file.stat().st_size > 0
        with self.notes_file.open("a", encoding="utf-8") as out:
            if has_content:
                out.write("\n")
            out.write(entry)
            out.write("\n")

    def read_entries(self) -> List[str]:
        if not self.notes_file.exists():
            return []
        entries: List[str] = []
        current: List[str] = []
        with self.notes_file.open("r", encoding="utf-8") as doc:
            for line in doc:
                if line.strip() == "---":
                    if current and current[0].strip() == "---":
                        entries.append("".join(current).rstrip())
                    current = ["---\n"]
                elif current:
                    current.append(line)
        if current and current[0].strip() == "---":
            entries.append("".join(current).rstrip())
        return entries
