import loader


def get_student_history(student_id: str, coordinator_email: str) -> dict:
    student = next(
        (s for s in loader.students if s["id"] == student_id),
        None,
    )
    if student is None:
        return {"erro": "Aluno não encontrado."}
    if student["coordinator_email"] != coordinator_email:
        return {"erro": "Acesso não autorizado para este aluno."}

    return {
        "aluno": {
            "id": student["id"],
            "nome": student["nome"],
            "turma": student["turma"],
            "turno": student["turno"],
        },
        "frequencia": [r for r in loader.attendance if r["aluno_id"] == student_id],
        "notas": [r for r in loader.grades if r["aluno_id"] == student_id],
        "ocorrencias": [r for r in loader.occurrences if r["aluno_id"] == student_id],
    }
