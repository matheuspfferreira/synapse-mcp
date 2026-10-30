from datetime import datetime

_interventions: list = []


def register_intervention(
    student_id: str,
    intervention_type: str,
    description: str,
    coordinator_email: str,
) -> dict:
    entry = {
        "id": f"INT{len(_interventions) + 1:03d}",
        "student_id": student_id,
        "type": intervention_type,
        "description": description,
        "coordinator_email": coordinator_email,
        "registered_at": datetime.now().isoformat(timespec="seconds"),
    }
    _interventions.append(entry)
    return {"status": "registrado", "intervention": entry}


def get_interventions(student_id: str, coordinator_email: str) -> list:
    return [
        i for i in _interventions
        if i["student_id"] == student_id
        and i["coordinator_email"] == coordinator_email
    ]
