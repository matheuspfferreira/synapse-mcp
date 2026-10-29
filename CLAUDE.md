# Hackathon 2026 — Contexto do Projeto

## Evento
UniCesumar + Elotech + Axion. Tema: "Educação que chega: tecnologia contra as barreiras do aprender".

## Desafio escolhido
**Desafio 1 — Antes que seja tarde: evasão e abandono escolar.**

Pergunta-guia: como perceber os sinais de abandono a tempo e direcionar o apoio certo para cada estudante?

## Ideia-chave
O problema não é falta de dados — escolas já têm frequência, notas e ocorrências. O problema é que esses dados chegam fragmentados e tarde demais, e o coordenador pedagógico não sabe o que fazer com eles: qual causa investigar, quem contatar, qual abordagem usar.

A solução não é mais um painel de alertas. É **infraestrutura de contexto**: um servidor MCP (Model Context Protocol) que estrutura os dados da Elotech e os disponibiliza para qualquer ferramenta de IA raciocinar sobre eles — orientando o coordenador a agir, não apenas a enxergar o risco.

**Lema: conectar soluções que já existem.**

## Como chegamos aqui
Partimos da pergunta que o desafio não faz diretamente: depois que o risco é identificado, o que acontece? Percebemos que a detecção já existe — o que falta é apoio estruturado para a ação. Investigando a rotina do coordenador, encontramos alguém sem contexto histórico e sem registro do que funcionou. O servidor MCP é a peça que faltava entre o dado bruto e a ação orientada.

## Nome do projeto
**Synapse** — ponto de conexão entre dois elementos. Ecoa a ponte entre os dados da Elotech e qualquer ferramenta de IA via servidor MCP.

## Arquitetura técnica

**Linguagem:** Python  
**SDK:** `mcp` (Model Context Protocol SDK oficial da Anthropic para Python)  
**Dados:** SQLite local com dados fictícios simulando o schema da Elotech  
**Transporte:** stdio (padrão para integração com Claude Desktop e outros clientes MCP)

### Estrutura de pastas
```
synapse-mcp/
├── main.py              # entrypoint do servidor MCP
├── data/
│   └── seed.sql         # dados fictícios (alunos, frequência, notas, ocorrências)
├── db.py                # conexão e queries SQLite
├── tools/
│   ├── alunos.py        # ferramentas de consulta de alunos em risco
│   ├── historico.py     # histórico por aluno
│   └── intervencoes.py  # registro e consulta de intervenções
└── requirements.txt
```

### Ferramentas MCP (tools)
- `get_alunos_em_risco(turma, periodo)` — lista alunos com padrão de risco por turma
- `get_historico_aluno(aluno_id)` — frequência, notas e ocorrências de um aluno
- `registrar_intervencao(aluno_id, tipo, descricao)` — salva ação tomada pelo coordenador
- `get_intervencoes(aluno_id)` — histórico de intervenções anteriores

### Fluxo
Cliente MCP (ex: Claude Desktop) → servidor Synapse → SQLite (dados Elotech simulados)

## Restrições do regulamento
- Dados: apenas fictícios ou públicos abertos (LGPD)
- IA como apoio — contribuição autoral da equipe é obrigatória
- Solução deve ser viável para redes de ensino reais
