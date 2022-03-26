from nebulatransit.engine import NebulaTransitEngine, SessionDraft


def test_draft_session_shape():
    engine = NebulaTransitEngine()
    session = engine.draft_session()
    assert isinstance(session, SessionDraft)
    assert session.focus.startswith("Exploring ")


def test_brief_includes_stack_and_goal():
    engine = NebulaTransitEngine()
    session = engine.draft_session()
    summary = engine.brief(session)
    assert any(line.startswith("Stack:") for line in summary)
    assert any(line.startswith("Goal:") for line in summary)
