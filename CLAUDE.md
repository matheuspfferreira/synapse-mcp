# Synapse MCP — Mapa de implementação

## Contexto
Servidor MCP educacional que expõe dados fictícios da Elotech como camada de contexto
para ferramentas de IA, orientando coordenadores pedagógicos na prevenção de evasão escolar.
Lema: conectar soluções que já existem.

---

## Stack
- Python + `mcp[cli]` (SDK oficial Anthropic)
- Dados em memória carregados de arquivos JSON fixos
- Transporte: stdio
- Sem banco de dados, sem framework web

---

## Mapa de dependências

### 1. `resource/CONTRACT.md` ← sem dependência
Regras de negócio em linguagem natural expostas como MCP Resource.
O modelo lê este arquivo antes de usar qualquer tool.

Definir:
- Critérios de classificação de risco (alto / médio / baixo)
- Regras de sugestão de ação por perfil de risco
- Restrições éticas (IA orienta, coordenador decide)

---

### 2. `loader.py` ← depende dos arquivos `data/*.json`
Carrega os quatro JSONs na inicialização e os mantém em memória.
Exporta quatro listas globais usadas pelos módulos de tool.

Implementar:
- `load_students()` → lista de alunos
- `load_attendance()` → lista de registros de frequência
- `load_grades()` → lista de notas
- `load_occurrences()` → lista de ocorrências

---

### 3. `tool/student.py` ← depende de `loader.py`
Retorna alunos em risco filtrando por turma e período.
Aplica as regras de classificação definidas no CONTRACT.

Implementar:
- `get_at_risk_students(classroom, period)` → lista de alunos com nível de risco

---

### 4. `tool/history.py` ← depende de `loader.py`
Agrega o histórico completo de um aluno: frequência, notas e ocorrências.

Implementar:
- `get_student_history(student_id)` → dict com frequência, notas e ocorrências do aluno

---

### 5. `tool/intervention.py` ← depende de `loader.py`
Registra e consulta intervenções. Como não há banco de dados,
intervenções são mantidas em uma lista em memória durante a sessão.

Implementar:
- `register_intervention(student_id, type, description)` → confirma registro
- `get_interventions(student_id)` → lista de intervenções registradas

---

### 6. `main.py` ← depende de todos os módulos acima
Entrypoint do servidor. Registra tools e resources no app MCP.

Implementar:
- Instanciar `FastMCP("synapse")`
- Registrar resource: `CONTRACT.md`
- Registrar tools: `get_at_risk_students`, `get_student_history`,
  `register_intervention`, `get_interventions`
- Chamar `loader` na inicialização para carregar dados em memória

---

## Ordem de implementação sugerida
1. `resource/CONTRACT.md`
2. `loader.py`
3. `tool/student.py`
4. `tool/history.py`
5. `tool/intervention.py`
6. `main.py`

---

## Critério de pronto
- `mcp dev main.py` sobe sem erro
- Claude Desktop conecta ao servidor via stdio
- As quatro tools respondem com dados fictícios coerentes
- O model lê o CONTRACT antes de sugerir ações
