# Quarta revisão da tradução de AATA — critérios 1–30

## Baselines

- Original, S: twjudson/aata, commit 3069910e3ded72ff5e18837a97a0e810c92790e2.
- Texto de partida, T0: projetorealmat/aata, master, commit f48b7db5b2251afc01918f8de85cfeb93f6fa295, após o merge do PR #34.
- Texto com as emendas desta rodada, T1: ramo review/fourth-round-30-criteria-2026-10-16.
- Issue de acompanhamento: #35; PR: #36.

## Escopo e método

A revisão é cumulativa: usa como base o cotejo integral S↔T0 documentado em audit/third-review-2026-10-16 e reabre a versão pós-merge. Foram conferidos os 23 capítulos ativos e os paratextos inventariados, as correções anteriores, a estrutura de IDs, os marcadores matemáticos, as figuras e os blocos Sage. Nesta rodada, o foco incluiu os critérios 1, 18, 27–30 e a adjudicação aprofundada de todas as alegações de problema herdado da fonte.

O inventário dos 23 capítulos encontrou 1.582 IDs XML em cada edição, sem ID faltante ou excedente; 65 elementos de figura em cada edição; e 709 blocos Sage em cada edição. A contagem mecânica de marcadores matemáticos foi de 17.419 no original e 17.436 na tradução; inclui marcadores aninhados e serve somente como indicador de inventário, não como teste de equivalência matemática. Os IDs dos objetos leitor-facing coincidem. Os resultados por arquivo estão em coverage.csv.

Esta rodada não repete do zero a leitura frase a frase dos 23 capítulos: os critérios linguísticos 2–26 são transportados da revisão integral anterior, com revalidação das correções registradas e das áreas alteradas. Assim, este relatório não apresenta uma nova medição independente de toda a fluência lexical. A revisão matemática e contextual foi refeita nos pontos identificados, separando defeitos da fonte, erros de tradução e explicitações editoriais.

## Resultado

O ledger contém 13 registros desta rodada: sete problemas da fonte confirmados e emendados; um exercício-fonte objetivamente tautológico, cuja correção exata permanece interpretação editorial a confirmar; duas alegações revistas e rejeitadas como erros (SRC-20 e SRC-21), com as explicitações revertidas; duas correções herdadas já presentes em T0 agora sinalizadas ao leitor; e uma nota de convenção previamente adicionada à tradução cuja proveniência está explícita.

Na adjudicação cumulativa dos IDs SRC-01–SRC-26, 23 problemas da fonte foram confirmados, um permanece provável quanto à emenda pretendida (SRC-18) e dois não se confirmaram como erros (SRC-20 e SRC-21). Os 23 incluem três inconsistências de descrição acessível de figuras, não defeitos nos desenhos. Os IDs identificam achados, não uma medida de qualidade; alguns reúnem mais de uma expressão afetada. A análise detalhada e as evidências constam em [source-error-adjudication.md](source-error-adjudication.md).

### Achados novos confirmados e tratados nesta rodada

- Em matrix.xml, corrigidos e sinalizados o sinal na dica da identidade de polarização e a transposta indevida do vetor-coluna na prova sobre matrizes ortogonais.
- Em actions.xml, corrigida e sinalizada a pontuação que tornava inválida uma notação de ciclo.
- Em struct.xml, acrescentada a hipótese de finitude ao exercício sobre séries com fatores de ordem prima; a mudança do grupo ambiente no exercício da série derivada foi mantida apenas como interpretação explicitamente assinalada.
- Em fields.xml, incluído o caso de tangência com discriminante zero e completada a direção recíproca da prova do teorema da torre. A restrição isolada da raiz quadrada foi revertida após a análise por ser convenção implícita da raiz real; a torre do teorema foi identificada em nota como interpretação de uma torre real.
- Em normal.xml, revertida a exclusão explícita de i e j no índice k: a expressão “3-ciclo” já implica índices distintos.
- Em galois.xml, restringido o enunciado do Teorema Fundamental da Álgebra a polinômios não constantes; mantida e ampliada a nota sobre fatores com multiplicidade.
- A nota de permute.xml sobre reflexões do grupo diédrico foi refinada. Correções de descrições acessíveis foram sinalizadas junto à dica ou legenda, sem inserir comentários editoriais no texto alternativo.

### Critérios considerados

| Nº | Critério | Resultado desta rodada |
|---:|---|---|
| 1 | Inclusão indevida de trecho | Reexaminadas correções herdadas da fonte e notas editoriais. Emendas confirmadas agora são sinalizadas; duas explicitações sem erro confirmado foram revertidas. |
| 2 | Omissão indevida de trecho | Sem nova omissão de tradução confirmada; revalidado o registro da auditoria integral anterior. |
| 3 | Alteração de significado | Separados erro da fonte, erro de tradução e interpretação editorial; a emenda SRC-18 tem ressalva explícita. |
| 4 | Consistência interna | Revalidadas as emendas e convenções dos trechos reabertos; sem inconsistência nova confirmada. |
| 5 | Consistência externa | Terminologia herdada da pesquisa direcionada da revisão anterior; não houve nova busca exaustiva. |
| 6 | Repetição | Nenhuma repetição nova confirmada nos trechos reabertos. |
| 7 | Coesão textual | Nenhuma quebra nova de encadeamento confirmada. |
| 8 | Coerência textual | Corrigidos defeitos de fórmula, hipótese e prova; ver adjudicação por ID. |
| 9 | Referenciação e anáfora | Nenhuma ambiguidade nova confirmada; achados anteriores permanecem no relatório da rodada precedente. |
| 10 | Ambiguidade | Analisados o domínio da raiz real, os índices do 3-ciclo e a tangência; duas explicitações foram revertidas e a tangência, corrigida. |
| 11 | Clareza | Completada a prova recíproca da torre e sinalizadas as emendas interpretativas. |
| 12 | Naturalidade e fluência | Revalidação cumulativa da revisão linguística anterior; sem ocorrência nova confirmada nesta rodada. |
| 13 | Registro e estilo acadêmico | Mantido o registro formal; as intervenções aparecem como notas editoriais. |
| 14 | Gramática | Nenhum desvio novo confirmado nos trechos reabertos. |
| 15 | Ortografia | Nenhum erro ortográfico novo confirmado. |
| 16 | Pontuação | Corrigido o ponto que invalidava a notação de ciclo na tabela de ações. |
| 17 | Convenções tipográficas | Marcadores XML e notação mantidos; notas editoriais rotuladas. |
| 18 | Integridade de elementos não textuais | Inventário estrutural preservado; descrições acessíveis cotejadas com os ativos. Não houve inspeção visual de PDF/HTML renderizados. |
| 19 | Paratextos | Paratextos ativos inventariados; a escolha da versão GFDL permanece pendente. |
| 20 | Citações e referências bibliográficas | Nenhuma divergência bibliográfica nova confirmada; não houve auditoria exaustiva de disponibilidade/paginação. |
| 21 | Nomes próprios, instituições e títulos | Nenhuma inconsistência nova confirmada nos trechos reabertos. |
| 22 | Números, unidades, medidas e datas | Corrigidos a notação do ciclo e os extremos do discriminante; demais números foram preservados. |
| 23 | Intenção pedagógica/didática | Corrigida a lacuna na prova da torre; a intenção exata do exercício tautológico permanece pendente. |
| 24 | Adaptação cultural/contextual | Intervenções matemáticas e de acessibilidade registradas como editoriais, sem adaptação cultural indevida identificada. |
| 25 | Anglicismos e falsos cognatos | Nenhum caso novo confirmado; terminologia herdada da rodada anterior. |
| 26 | Equivalência de expressões idiomáticas | Nenhum caso novo confirmado. |
| 27 | Coerência entre texto e elementos não textuais | Conferidas fórmulas e descrições acessíveis dos achados. Não houve inspeção visual de saída renderizada. |
| 28 | Notas do tradutor | Notas editoriais incluídas nas emendas confirmadas e na interpretação provável; sinalização fica fora do texto alternativo. |
| 29 | Fidelidade semântico-conceitual contextual | Todas as alegações de erro na fonte das duas rodadas foram reexaminadas com contexto e evidência matemática. |
| 30 | Validade matemática e consistência do conteúdo | Sete problemas novos confirmados, uma emenda provável e duas alegações rejeitadas; as correções preexistentes foram também adjudicadas. |

## Problemas de fonte que continuam pendentes

Permanecem separados das correções desta rodada e exigem validação editorial ou especializada: inconsistências entre parâmetros e fórmulas de translação e a escolha da origem em matrix.xml; formulação histórica sobre grupos cristalográficos; notação/expoente em um lema de p-grupos; e a divergência entre a permissão GFDL 1.2 ou posterior na fonte e a versão 1.3 incorporada à edição brasileira. A decisão jurídica sobre a licença continua com os responsáveis pela edição.

## Gate separado de confiabilidade do revisor de IA

O gate não foi aprovado nem quantificado. Não houve benchmark cego com casos positivos e negativos adjudicados independentemente; portanto, não há taxas defensáveis de falsos positivos, falsos negativos ou calibração. A adjudicação cuidadosa dos casos deste relatório demonstra evidência contextual em exemplos específicos, mas não constitui validação independente do revisor. O registro está em ai-reviewer-gate.md.

## Validação e limitações

- A validação automatizada de XML, a compilação oficial, os workflows do PR e a inspeção visual de HTML/PDF devem ser consultados após a atualização do PR; não são declarados como aprovados neste relatório.
- Não houve execução do código Sage nesta rodada.
- Os arquivos GFDL e o índice são idênticos entre S e T0; history.xml não existe na fonte consultada e é paratexto específico da edição brasileira.
- A aprovação das emendas matemáticas e das notas editoriais depende de leitura humana independente, em particular da interpretação SRC-18.
- A tabela de cobertura distingue a revisão cumulativa anterior da reavaliação adicional desta rodada.
