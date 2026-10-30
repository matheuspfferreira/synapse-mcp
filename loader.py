import json
from pathlib import Path

_DATA = Path(__file__).parent / "data"


def _load(filename: str) -> list:
    with open(_DATA / filename, encoding="utf-8") as f:
        return json.load(f)


def load_students() -> list:
    return _load("student.json")


def load_attendance() -> list:
    return _load("attendance.json")


def load_grades() -> list:
    return _load("grade.json")


def load_occurrences() -> list:
    return _load("occurrence.json")


students = load_students()
attendance = load_attendance()
grades = load_grades()
occurrences = load_occurrences()
