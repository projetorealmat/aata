# Outputs e validações

## Revisão de conteúdo

- O cotejo das 26 alegações sobre problemas na fonte está registrado em source-error-adjudication.md; as notas e reversões de T1 estão relacionadas em interventions.md.
- Os 13 registros do ledger JSONL foram parseados e classificados por adjudicação.
- Os 11 arquivos XML alterados passaram por uma verificação estrutural leve de abertura/fechamento e aninhamento de tags, ignorando comentários XML. Isso não substitui um parser XML/validador PreTeXt.
- O inventário cumulativo registra 1.582 IDs XML correspondentes, 65 figuras e 709 blocos Sage em cada edição.
- Não houve inspeção humana de HTML/PDF nem execução de Sage nesta rodada.

## Workflows do commit de conteúdo

Commit: da3966f1fde17699c72726853bbdc3bf1232ecb2

- Publicar HTML traduzido — Álgebra Abstrata, execução #142 (ID 38932528084): concluída com sucesso no commit de conteúdo acima. A compilação PreTeXt e a validação da saída HTML passaram; a implantação do Pages foi ignorada por se tratar de execução de PR.
- REALMat — verificar AATA, execução #182 (ID 38932528551): ainda em andamento na última consulta. A etapa "Instalar dependências de compilação" permanecia ativa; validação de conteúdo, compilação e verificação do PDF ainda não haviam começado.

Este registro distingue o resultado do HTML do build do backend/PDF, que continua pendente. Os workflows de sucesso do commit anterior não foram usados como evidência.
