# Relatório final — segunda auditoria integral AATA

## Baselines
- S: `twjudson/aata@3069910e3ded72ff5e18837a97a0e810c92790e2`
- T0: `13ed5d803cf37bed1d60b246e6f8c8369328d278`
- T1 (último commit que altera o conteúdo traduzido): `7f5ab4eae6a11373875281baf943611b40faac80`

## Resultado editorial
A rodada consolidou o cotejo integral já documentado na Issue #31, fechou os paratextos e executou uma passagem adversarial de reconciliação. Foram corrigidos defeitos demonstráveis de tradução e erros materiais herdados da fonte, estes últimos registrados separadamente em `interventions.md`. Preferências sem erro demonstrável não foram usadas para reescrever o texto.

Dois candidatos da passagem anterior foram reclassificados como falsos positivos: o parágrafo inglês em `galois.xml` está dentro de comentário XML e não é reader-facing; e não há marcadores de conflito ativos no arquivo.

## Gates
- XML bem-formado: PASS nesta branch antes dos commits.
- Marcadores de conflito: PASS (nenhum encontrado).
- `runner.cli`: NOT_RUN — pacote/comando não existe no repositório.
- Workflows oficiais / HTML / PDF: PENDING — serão executados no PR e registrados em `outputs.md`.
- Revisão editorial humana independente: PENDING — obrigatória pela Issue #31 e não substituível por esta execução.

## Artefatos
- `manifest.json`: manifesto v3.
- `coverage.csv`: ledger enumerado das unidades reader-facing e disposições.
- `termbase.json`: termbase v2 reconciliada.
- `findings.jsonl`: achados estruturados v3.
- `interventions.md`: correções materiais da fonte.
- `outputs.md`: registro de builds/inspeção.
