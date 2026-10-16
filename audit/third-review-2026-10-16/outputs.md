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
| GitHub Actions do PR atual | PENDING | Atualizar quando os workflows terminarem. |
| HTML e PDF do PR atual | PENDING | Acompanhar workflows oficiais; inspeção visual ainda pendente. |
| Revisão humana independente | PENDING | Gate editorial do projeto; não substituído por esta revisão. |
| Aviso de licença / versão GFDL | PENDING | Remissão ao apêndice corrigida; versão 1.3 exige validação dos responsáveis pelos direitos. |
