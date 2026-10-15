# Registro de outputs

| Output/gate | Estado | Evidência |
|---|---|---|
| XML local (ElementTree) | PASS | todos os `src/*.xml` analisados após as correções |
| Marcadores de conflito | PASS | nenhum `<<<<<<<`/`>>>>>>>` em `src/*.xml` |
| runner.cli validate | NOT_RUN | `runner.cli` não existe no repositório |
| runner.cli negative-evidence | NOT_RUN | `runner.cli` não existe no repositório |
| runner.cli gate | NOT_RUN | `runner.cli` não existe no repositório |
| GitHub Actions do PR | PENDING | preencher após abertura do PR |
| HTML oficial/preview | PENDING | preencher após workflows |
| PDF oficial/preview | PENDING | preencher após workflows |
| Revisão humana independente | PENDING | gate externo obrigatório |
