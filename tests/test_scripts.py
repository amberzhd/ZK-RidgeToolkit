from datetime import datetime

from scripts.mock_entry import split_notes
from scripts.monthly_review import parse_timestamp


def test_split_notes_records_nonempty_segments() -> None:
    value = "one; two ; ; three"
    assert split_notes(value) == ["one", "two", "three"]


def test_parse_timestamp_handles_iso() -> None:
    entry = "---\ntimestamp: 2022-05-05T13:24:19\n"
    ts = parse_timestamp(entry)
    assert isinstance(ts, datetime)
    assert ts.year == 2022 and ts.month == 5 and ts.day == 5
