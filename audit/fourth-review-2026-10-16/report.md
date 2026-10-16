# Quarta revisão da tradução de AATA — critérios 1–30

## Baselines

- Original, S: twjudson/aata, commit 3069910e3ded72ff5e18837a97a0e810c92790e2.
- Texto de partida, T0: projetorealmat/aata, master, commit f48b7db5b2251afc01918f8de85cfeb93f6fa295, após o merge do PR #34.
- Texto com as emendas desta rodada, T1: ramo review/fourth-round-30-criteria-2026-10-16; o último commit que alterou capítulos é e0e6f3d03b18bfc11c96f6293c8905c41d495025.
- Issue de acompanhamento: #35.

## Escopo e método

A revisão é cumulativa: usa como base o cotejo integral S↔T0 já documentado em audit/third-review-2026-10-16 (PR #34) e reabre a versão pós-merge. Nesta rodada foram conferidos os 23 capítulos ativos e os paratextos inventariados, as correções anteriores registradas, a estrutura de IDs, os marcadores de matemática, as figuras e os blocos Sage. O foco novo foi aprofundar os critérios 1, 18, 27, 28, 29 e, sobretudo, 30, com reconstrução de argumentos e checagem de fórmulas em contexto.

O inventário dos 23 capítulos encontrou 1.582 IDs XML em cada edição, sem ID faltante ou excedente; 65 elementos de figura em cada edição; e 709 blocos Sage em cada edição. A contagem mecânica de marcadores matemáticos foi de 17.419 no original e 17.436 na tradução; ela inclui marcadores aninhados e serve somente como indicador de inventário, não como teste de equivalência matemática. Os IDs dos objetos leitor-facing coincidem. Os resultados por arquivo estão em coverage.csv.

Esta rodada não repete do zero a leitura frase a frase dos 23 capítulos: os critérios linguísticos 2–26 são transportados da revisão integral anterior, com revalidação das correções registradas e das áreas alteradas. Assim, este relatório não apresenta uma nova medição independente de toda a fluência lexical. A revisão de validade matemática e contextual foi refeita nos pontos identificados, e defeitos herdados da fonte foram registrados separadamente dos erros de tradução.

## Resultado

O ledger contém 13 registros: 10 defeitos matemáticos/editoriais herdados da fonte corrigidos nesta rodada; dois defeitos da fonte cuja correção já estava incorporada em T0 e agora recebeu nota editorial explícita; e uma nota editorial anteriormente adicionada à tradução cuja proveniência foi explicitada. Os números identificam causas e intervenções, não uma nota de qualidade. Não foi confirmado erro novo de tradução em prosa nesta rodada; os novos achados concentram-se em validade matemática e na sinalização de intervenções preexistentes.

### Achados corrigidos nesta rodada

- Em matrix.xml, corrigidos o sinal de um passo da dica da identidade de polarização e o vetor-coluna transposto incorretamente na prova do teorema sobre matrizes ortogonais.
- Em actions.xml, corrigido o ponto que aparecia como decimal na notação de um ciclo.
- Em struct.xml, corrigido o subgrupo ambiente incorreto no exercício sobre a série derivada e explicitada a hipótese de finitude no exercício que caracteriza grupos solúveis por fatores de ordem prima.
- Em normal.xml, excluídos os índices repetidos i e j do intervalo que nomeia 3-ciclos.
- Em fields.xml, explicitada a não negatividade necessária para raízes quadradas reais, incluído o caso de tangência com discriminante zero e completada a direção recíproca da caracterização dos números construtíveis por torres quadráticas.
- Em galois.xml, restringido o enunciado do Teorema Fundamental da Álgebra a polinômios não constantes.
- Foram acrescentadas notas editoriais em galois.xml e permute.xml para distinguir correções de erros da fonte de conteúdo originalmente traduzido. A nota sobre a convenção de multiplicação à esquerda para a direita em permute.xml também foi identificada como intervenção editorial.

### Critérios considerados

| Nº | Critério | Resultado desta rodada |
|---:|---|---|
| 1 | Inclusão indevida de trecho | Identificadas duas correções da fonte já presentes em T0 sem explicação explícita; notas editoriais acrescentadas. Uma nota de convenção da tradução foi identificada como editorial. |
| 2 | Omissão indevida de trecho | Sem nova omissão confirmada; achados anteriores foram revalidados contra o ledger do PR #34. |
| 3 | Alteração de significado | Revalidada a distinção entre erro de tradução e erro da fonte; nenhum novo desvio semântico de tradução confirmado nesta rodada. |
| 4 | Consistência interna | Revalidação das emendas terminológicas e notacionais da revisão anterior; correção de notação de ciclo. |
| 5 | Consistência externa | A terminologia foi herdada da pesquisa direcionada registrada em audit/third-review-2026-10-16; não foi feita nova busca terminológica exaustiva. |
| 6 | Repetição | Nenhuma repetição nova confirmada; as correções anteriores permanecem no baseline. |
| 7 | Coesão textual | Sem nova quebra de encadeamento confirmada nos trechos reabertos. |
| 8 | Coerência textual | Identificados e corrigidos enunciados e argumentos incompatíveis com a matemática: série derivada, finitude, raízes e teorema da álgebra. |
| 9 | Referenciação e anáfora | Nenhuma ambiguidade referencial nova confirmada; remissões anteriores permanecem registradas na auditoria precedente. |
| 10 | Ambiguidade | Especificados o domínio da raiz real, o caso de tangência e os índices distintos de um 3-ciclo. |
| 11 | Clareza | Completada a direção recíproca da prova sobre torres de corpos e tornadas explícitas as hipóteses necessárias. |
| 12 | Naturalidade e fluência | Revalidação cumulativa da revisão linguística anterior; sem nova ocorrência confirmada nesta rodada. |
| 13 | Registro e estilo acadêmico | Mantido o registro formal; notas de intervenção classificadas como editoriais. |
| 14 | Gramática | Nenhum novo desvio confirmado nos trechos reabertos. |
| 15 | Ortografia | Nenhum erro ortográfico novo confirmado. |
| 16 | Pontuação | Corrigido o ponto decimal indevido na notação do ciclo de uma permutação. |
| 17 | Convenções tipográficas | Mantidos os marcadores XML e a notação; notas editoriais explicitamente rotuladas. |
| 18 | Integridade de elementos não textuais | Inventário estrutural: mesmos 65 elementos de figura e 709 blocos Sage. Não houve inspeção visual de PDF/HTML renderizados nesta rodada. |
| 19 | Paratextos | Inventariados os paratextos ativos; histórico brasileiro é específico da tradução. A decisão sobre a versão da GFDL segue pendente. |
| 20 | Citações e referências bibliográficas | Nenhuma divergência bibliográfica nova foi confirmada; a verificação anterior não foi expandida a uma auditoria exaustiva de disponibilidade e paginação. |
| 21 | Nomes próprios, instituições e títulos | Nenhuma inconsistência nova confirmada nos trechos reabertos. |
| 22 | Números, unidades, medidas e datas | Corrigada a pontuação de ciclo que simulava um decimal; os demais achados numéricos anteriores foram mantidos. |
| 23 | Intenção pedagógica/didática | Corrigidos o passo inválido da dica e a lacuna de uma das direções da caracterização por torres. |
| 24 | Adaptação cultural/contextual | Adaptações e correções da fonte foram registradas como intervenções editoriais. |
| 25 | Anglicismos e falsos cognatos | Nenhum anglicismo ou falso cognato novo confirmado; a revisão terminológica anterior permanece como referência. |
| 26 | Equivalência de expressões idiomáticas | Nenhuma nova expressão idiomática problemática confirmada nesta rodada. |
| 27 | Coerência entre texto e elementos não textuais | Cotejadas as fórmulas e notações dos achados; inventário de figuras preservado. Não houve inspeção visual de saída renderizada. |
| 28 | Notas do tradutor | As notas de intervenção identificadas foram rotuladas como notas editoriais; autoria humana dessas decisões ainda requer aprovação editorial. |
| 29 | Fidelidade semântico-conceitual contextual | Refeita a leitura contextual dos pontos matemáticos, distinguindo conteúdo-fonte, correção editorial e tradução. |
| 30 | Validade matemática e consistência do conteúdo | Dez defeitos da fonte corrigidos nesta rodada; dois defeitos já corrigidos em T0 agora foram explicitamente sinalizados. |

## Defeitos de fonte ainda encaminhados

Os seguintes itens da revisão anterior permanecem separados das correções deste PR e exigem revisão editorial ou validação especializada: divergências entre parâmetros e fórmulas de translação e escolha da origem em matrix.xml; formulação histórica sobre grupos cristalográficos; ponto de notação/expoente em um lema de p-grupos; e a discrepância entre a permissão GFDL 1.2 ou posterior na fonte e a versão 1.3 incorporada à edição brasileira. A lista completa e o histórico permanecem em audit/third-review-2026-10-16/report.md.

## Gate separado de confiabilidade do revisor de IA

O gate não foi aprovado nem quantificado. Não foi aplicado um benchmark cego com casos positivos e negativos adjudicados independentemente; portanto, não há taxas defensáveis de falsos positivos, falsos negativos ou calibração. A identificação dos problemas matemáticos deste relatório demonstra análise contextual em casos específicos, mas uma nova passada do mesmo modelo não constitui revisão independente. O registro completo está em ai-reviewer-gate.md.

## Validação e limitações

- A validação automatizada de XML, a compilação oficial, os workflows do PR e a inspeção visual de HTML/PDF devem ser registrados após a abertura do PR; não são declarados como aprovados neste relatório.
- Não houve execução do código Sage nesta rodada.
- Os arquivos GFDL e o índice são idênticos entre S e T0; history.xml não existe na fonte consultada e é paratexto da edição brasileira.
- A aprovação das emendas matemáticas e das notas editoriais depende de leitura humana independente.
- A tabela de cobertura distingue a revisão cumulativa anterior da reavaliação adicional desta rodada.
