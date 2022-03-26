from dataclasses import dataclass
import random
from typing import List

@dataclass
class SessionDraft:
    focus: str
    stack_mix: str
    deliverable: str
    notes: List[str]


class NebulaTransitEngine:
    def __init__(self) -> None:
        self.themes = [
            "agentic workflow", "edge analytics", "alternative data visualization",
            "bot-assisted trading", "personal finance tooling", "DIY research journal",
        ]
        self.stacks = {
            "web2": ["Next.js + Supabase", "FastAPI + Postgres", "Electron + SQLite"],
            "web3": ["Solana + Anchor", "Ethereum + Graph", "zkSync + Rust"],
        }
        self.targets = [
            "prototype a lightweight dashboard",
            "write a short essay about the workflow",
            "capture telemetry for user experiments",
            "sketch a new CLI helper for deployment",
            "design a research note template",
        ]

    def pick_theme(self) -> str:
        return random.choice(self.themes)

    def pick_stack_mix(self) -> str:
        primary = random.choice(self.stacks["web2"])
        secondary = random.choice(self.stacks["web3"])
        return f"{primary} + {secondary}"

    def pick_target(self) -> str:
        return random.choice(self.targets)

    def draft_session(self) -> SessionDraft:
        focus = f"Exploring {self.pick_theme()}"
        stack_mix = self.pick_stack_mix()
        deliverable = f"{self.pick_target()}"
        notes = [
            "Aligns with the idea that not every sprint is a launch.",
            "Keeps the narrative casual yet honest about time spent.",
        ]
        if random.random() > 0.5:
            notes.append("Throw in a quick experiment that can run on a desktop.")
        return SessionDraft(focus, stack_mix, deliverable, notes)

    def brief(self, session: SessionDraft) -> List[str]:
        summary = [
            f"Focus: {session.focus}",
            f"Stack: {session.stack_mix}",
            f"Goal: {session.deliverable}",
        ]
        summary.extend(session.notes)
        return summary
