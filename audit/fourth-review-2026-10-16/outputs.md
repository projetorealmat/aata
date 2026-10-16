# Outputs e validações

## Estado no momento da abertura do PR

- A inspeção de PDF/HTML renderizados não foi executada.
- O código Sage não foi executado.
- A estrutura foi inventariada em S e T0; os 65 elementos de figura e 709 blocos Sage coincidem em contagem.
- A validação XML e a compilação oficial desta rodada ficam condicionadas aos workflows acionados pelo PR. Não declarar aprovação antes de consultar os resultados do commit do PR.
- A consulta de workflows ao commit-base f48b7db5 retornou lista vazia no endpoint usado, que mostra apenas execuções acionadas por pull request; isso não é evidência de compilação aprovada ou reprovada.

Atualizar este arquivo após verificar o status dos workflows do PR. Se não houver renderização oficial disponível, registrar a limitação e encaminhar a inspeção visual aos responsáveis editoriais.
