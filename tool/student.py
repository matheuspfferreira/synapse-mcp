import loader


def _classify_risk(student_id: str) -> str:
    absences = sum(
        1 for r in loader.attendance
        if r["aluno_id"] == student_id and not r["presente"]
    )
    student_grades = [r["valor"] for r in loader.grades if r["aluno_id"] == student_id]
    avg = sum(student_grades) / len(student_grades) if student_grades else 10.0
    occ_count = sum(1 for o in loader.occurrences if o["aluno_id"] == student_id)

    if absences >= 4 or avg < 5.0 or occ_count >= 2:
        return "alto"
    if absences >= 2 or avg < 6.5 or occ_count >= 1:
        return "médio"
    return "baixo"


def get_at_risk_students(classroom: str, period: str, coordinator_email: str) -> list:
    filtered = [
        s for s in loader.students
        if s["turma"] == classroom
        and s["turno"] == period
        and s["coordinator_email"] == coordinator_email
    ]
    return [
        {
            "id": s["id"],
            "nome": s["nome"],
            "turma": s["turma"],
            "turno": s["turno"],
            "risco": _classify_risk(s["id"]),
        }
        for s in filtered
    ]
