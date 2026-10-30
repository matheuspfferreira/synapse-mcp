from pathlib import Path

import loader  # noqa: F401 — triggers data load at startup
from mcp.server.fastmcp import FastMCP
from tool.history import get_student_history
from tool.intervention import get_interventions, register_intervention
from tool.student import get_at_risk_students

app = FastMCP("synapse")

_CONTRACT = Path(__file__).parent / "resource" / "CONTRACT.md"


@app.resource("resource://synapse/contract")
def contract() -> str:
    """Regras de negócio, critérios de risco e restrições éticas do Synapse."""
    return _CONTRACT.read_text(encoding="utf-8")


@app.tool()
def get_at_risk_students_tool(classroom: str, period: str, coordinator_email: str) -> list:
    """Lista alunos com nível de risco para uma turma e turno.

    Args:
        classroom: Código da turma (ex: 8A, 9B).
        period: Turno do aluno — 'matutino' ou 'vespertino'.
        coordinator_email: E-mail do coordenador autenticado.
    """
    return get_at_risk_students(classroom, period, coordinator_email)


@app.tool()
def get_student_history_tool(student_id: str, coordinator_email: str) -> dict:
    """Retorna o histórico completo de frequência, notas e ocorrências de um aluno.

    Args:
        student_id: ID do aluno (ex: A001).
        coordinator_email: E-mail do coordenador autenticado.
    """
    return get_student_history(student_id, coordinator_email)


@app.tool()
def register_intervention_tool(
    student_id: str,
    intervention_type: str,
    description: str,
    coordinator_email: str,
) -> dict:
    """Registra uma intervenção pedagógica para um aluno (persiste apenas na sessão).

    Args:
        student_id: ID do aluno (ex: A001).
        intervention_type: Tipo da intervenção (ex: 'contato_familia', 'orientador', 'plano_individual').
        description: Descrição detalhada da ação realizada ou planejada.
        coordinator_email: E-mail do coordenador autenticado.
    """
    return register_intervention(student_id, intervention_type, description, coordinator_email)


@app.tool()
def get_interventions_tool(student_id: str, coordinator_email: str) -> list:
    """Lista todas as intervenções registradas para um aluno na sessão atual.

    Args:
        student_id: ID do aluno (ex: A001).
        coordinator_email: E-mail do coordenador autenticado.
    """
    return get_interventions(student_id, coordinator_email)


if __name__ == "__main__":
    app.run(transport="stdio")
