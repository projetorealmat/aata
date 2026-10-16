# Registro de validações — terceira revisão

| Gate/artefato | Estado | Evidência ou limite |
|---|---|---|
| Comparação S↔T0 | PASS | Baselines fixados no manifesto; 23 capítulos ativos e paratextos cotejados. |
| Critérios 1–29 | PASS | Matriz completa em report.md; ledger estruturado em findings.jsonl. |
| Cobertura por arquivo | PASS | coverage.csv registra os 23 capítulos, assembly, paratextos e ativos vinculados. |
| Falsos positivos de travessão | DESCARTADOS | Marcador XML <mdash/> presente nos trechos de cosets, crypt e isomorph. |
| Comparação dos apêndices GFDL | PASS | gfdl.xml e gfdl-mathbook.xml idênticos entre S e T0. |
| XML local / ElementTree | NOT_RUN | Não houve checkout local nem validador local nesta execução. |
| runner.cli validate | NOT_RUN | runner.cli não existe no repositório. |
| Sage | NOT_RUN | Código cotejado estaticamente; sem execução do Sage. |
| Build/HTML/PDF do baseline T0 | PASS | Registro de build da rodada anterior; sem inspeção visual de PDF. |
| HTML do PR atual | PASS | “Publicar HTML traduzido — Álgebra Abstrata”, run 134 (#38908579373), concluído com sucesso no head ab197747448e4cccd805f3484db16af063d12f83. |
| Verificador REALMat do PR atual | IN_PROGRESS | “REALMat — verificar AATA”, run 174 (#38908579461), em execução no mesmo head. |
| Prévia PDF do PR atual | IN_PROGRESS | “Prévia do PDF — AATA”, run 11 (#38908578970), em execução; inspeção visual ainda pendente. |
| Revisão humana independente | PENDING | Gate editorial do projeto; não substituído por esta revisão. |
| Aviso de licença / versão GFDL | PENDING | Remissão ao apêndice corrigida; versão 1.3 exige validação dos responsáveis pelos direitos. |
