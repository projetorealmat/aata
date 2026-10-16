# Relatório — terceira revisão da tradução de AATA

## Baselines e escopo

- Original (S): `twjudson/aata@3069910e3ded72ff5e18837a97a0e810c92790e2`
- Tradução examinada (T0): `projetorealmat/aata@913a92dc0078fc0b702e69fda1cd1d31fcaf1b88`
- Commit de conteúdo revisado (T1): `e68f39b190bf8845e898f18dd70002e8994a28cb`
- Issue de acompanhamento: [#33 — revisão integral da tradução (29 critérios)](https://github.com/projetorealmat/aata/issues/33)

O cotejo cobre os 23 capítulos ativos ligados por src/aata.xml, além de frontmatter, backmatter, metadados, colofão, histórico, notas, índice, notação e apêndices/licenças ativos. Foram examinados prosa, definições, enunciados, demonstrações, exemplos, exercícios, dicas e respostas, referências e remissões, fórmulas, código Sage e seus resultados, figuras, diagramas, legendas e descrições alternativas. Comentários XML inativos foram excluídos do conteúdo leitor-facing. A cobertura por arquivo está em coverage.csv; os achados estão em findings.jsonl.

A revisão comparou S e T0 por unidade e fez uma reconciliação global de terminologia, notação, referências, fórmulas e elementos visuais. As intervenções feitas em T1 distinguem defeitos da tradução de correções de erros que já existiam na fonte. O ledger não transforma preferências estilísticas em defeitos.

## Resultado

A rodada confirmou problemas localizados de omissão, sentido, gramática, clareza, terminologia e coerência entre texto e matemática. Corrigi-os em 13 arquivos XML. Também corrigi erros matemáticos herdados do inglês quando a solução era demonstrável no próprio contexto, e marquei como nota editorial uma intervenção substancial que já estava no T0 sem sinalização.

Os critérios foram considerados ao longo de todo o escopo:

| Nº | Critério | Resultado da verificação |
|---:|---|---|
| 1 | Inclusão indevida | Uma intervenção sobre NP-completude já constava em T0 sem rótulo; T1 a identifica como nota editorial. Créditos e datas brasileiros são apresentados como dados da edição brasileira. |
| 2 | Omissão indevida | Reposto “Escrevemos” no exemplo de conjuntos; restaurada a pergunta sobre dimensão das matrizes de códigos. |
| 3 | Alteração de significado | Ajustadas a formulação sobre publicar resultados, a instrução de criptografia e a referência a “um dos” subgrupos de Sylow. |
| 4 | Consistência interna | Uniformizados imperativo singular, plural dos símbolos matemáticos, uso de GAP e terminologia de corpos. |
| 5 | Consistência externa | Adotado “p-subgrupo maximal”, forma registrada em textos acadêmicos brasileiros de álgebra. Mantida a distinção entre corpo finito e corpo de números. |
| 6 | Repetição | Removida a repetição de “parte” em Sylow e a duplicação “a relação é ‘é subconjunto de’”. |
| 7 | Coesão textual | Repostos verbo e encadeamento em Sets; reestruturada a frase sobre decodificação por classes laterais. |
| 8 | Coerência textual | Conferidas proposições e fórmulas; corrigidos erros herdados em álgebra de códigos, corpos, álgebra booleana e Galois. |
| 9 | Referenciação e anáfora | Conferidas remissões e antecedentes no texto matemático; corrigida a referência a H₁ no trecho de Sylow. |
| 10 | Ambiguidade | Desfeita a leitura de unicidade de gerador para corpos finitos; preservada explicitamente a noção de tamanho da matriz. |
| 11 | Clareza | Reescritas frases truncadas sobre decodificação e dimensões de matrizes; explicitado o conjunto de erros admissíveis na definição de código corretor. |
| 12 | Naturalidade e fluência | Corrigidos calques em “GAP console” e “muita pressa em publicar”; removidas terminações plurais copiadas do inglês. |
| 13 | Registro acadêmico | O tom formal e expositivo foi mantido; as instruções de atividade foram alinhadas em pessoa e número. |
| 14 | Gramática | Corrigidos “Sejam … sejam”, concordância das instruções e sufixos plurais indevidos após símbolos. |
| 15 | Ortografia | Não foi confirmado erro ortográfico adicional nos trechos ativos examinados. |
| 16 | Pontuação | Conferida no XML original; candidatos de travessão eram falsos positivos de extração: o marcador <mdash/> está presente em cosets, crypt e isomorph. |
| 17 | Convenções tipográficas | Verificados marcadores XML, matemática, aspas, ênfases e siglas. Os travessões já marcados foram preservados. |
| 18 | Elementos não textuais | Corrigidas descrições alternativas de figura de corpos finitos, gráfico de Galois e diagrama de circuito; fórmulas e ativos vinculados foram cotejados. |
| 19 | Paratextos | Corrigida a remissão da licença de “seção” para “apêndice”; comparados os paratextos ativos. A nota da licença continua sujeita a validação jurídica da versão. |
| 20 | Citações e referências | Conferidas as referências e remissões ativas. O título de Shannon e outros dados já tinham sido corrigidos na edição-base; nenhuma nova divergência bibliográfica foi confirmada nesta rodada. |
| 21 | Nomes próprios, instituições e títulos | Conferidos nomes, siglas e títulos; “GAP” e títulos bibliográficos foram tratados de forma consistente. |
| 22 | Números e notação | Corrigidos índices, dimensões e expoentes contextualizados; não foi confirmado problema adicional de convenção decimal ou de unidades. |
| 23 | Intenção didática | Mantidos exercícios e progressão; restaurada a pergunta que orienta a escolha do tamanho da matriz e esclarecido o alcance da correção de erros. |
| 24 | Adaptação cultural | Créditos, histórico e data da edição brasileira são identificados como adaptações editoriais; não foi necessária localização cultural adicional. |
| 25 | Anglicismos e falsos cognatos | Substituído “GAP console” por “console do GAP”; revista a distinção técnica entre corpo finito e corpo de números. |
| 26 | Expressões idiomáticas | “Very eager to publish” foi traduzido como interesse em publicar, e não como pressa. |
| 27 | Texto e elementos não textuais | Conferidas remissões e descrições contra fórmulas e diagramas; corrigidos p⁶ e a posição do máximo local no gráfico. |
| 28 | Notas do tradutor | A intervenção sobre NP-completude foi rotulada “Nota editorial” e explica a imprecisão da frase-fonte. |
| 29 | Competência contextual da IA | A revisão exigiu leitura matemática contextual: unicidade de Sylow em D₁₈, graus de extensões, matrizes de códigos, índices de transposições, simplificação booleana e compatibilidade de descrições de figuras. |

## Achados e correções em T1

### Erros de tradução ou redação do T0

| ID | Local | Problema confirmado | Tratamento em T1 |
|---|---|---|---|
| T-01 | src/sets.xml, sets-subsection-set-theory | O original diz “We write 2 ∈ E”; T0 começa a frase diretamente pela fórmula. | Reposto “Escrevemos”. |
| T-02 | src/crypt.xml, crypt-exercise-classroom-exercise | “Verifique se conseguem” mistura imperativo singular com verbo no plural e não deixa claro que os participantes quebram os códigos dos demais. | “Verifique se consegue quebrar os códigos dos demais participantes.” |
| T-03 | src/algcodes.xml, algcodes-exercise-ascii-characters | Nas perguntas sobre ASCII, T0 pergunta qual matriz usar; o original pergunta qual deve ser o tamanho da matriz. | A dimensão/tamanho voltou a ser o objeto explícito das duas perguntas. |
| T-04 | src/algcodes.xml, algcodes-subsection-coset-decoding | “Classe lateral ou decodificação padrão usa...” não forma uma construção natural nem nomeia o processo. | Reescrito como “A decodificação por classes laterais (ou decodificação padrão) usa...”. |
| T-05 | src/algcodes.xml, lema e teorema de verificação de paridade | A posição de “n × (n−m)” torna as frases sintaticamente truncadas. | Dimensões integradas como “matriz … de dimensão …”. |
| T-06 | src/struct.xml, plural de símbolos em grupos abelianos finitamente gerados | Em oito ocorrências, o sufixo inglês ’s foi anexado ao fechamento MathML, gerando formas como “gᵢ s”; o artigo plural já faz o trabalho em português. | Removidos os oito sufixos espúrios. |
| T-07 | src/struct.xml, struct-exercise-finitely-generated-abelian-group | “Sejam G, H e K sejam...” duplica o verbo. | Removido o segundo “sejam”. |
| T-08 | src/sylow.xml, exercício com D₁₈ | “Um dos subgrupos de Sylow 3” sugere vários; em D₁₈ há um único Sylow 3-subgrupo. | “O único subgrupo de Sylow 3”. |
| T-09 | src/sylow.xml, instrução do Sage | “GAP console” é calque desnecessário. | “Console do GAP”. |
| T-10 | src/sylow.xml, definição de subgrupo de Sylow | “p-subgrupo máximo” não é a forma técnica mais usada neste contexto brasileiro. | “p-subgrupo maximal”. |
| T-11 | src/sylow.xml, exercício sobre congruência | “a parte … parte da conclusão” repete “parte”. | Removida a repetição. |
| T-12 | src/poly.xml, nota histórica | “Very eager to publish” indica interesse/entusiasmo, não necessariamente pressa. | “Geralmente estão muito interessados em publicar seus resultados.” |
| T-13 | src/boolean.xml, parágrafo sobre posets | “A relação é ‘é subconjunto de’” duplica “é”. | “A relação é ‘a de inclusão’.” |
| T-14 | src/vect.xml, explicação de corpos finitos | “Corpos finitos possuem um único gerador” pode ser lido como unicidade do gerador. | Explicita que todo corpo finito é extensão simples do corpo primo e que as potências de um elemento gerador formam uma base. |
| T-15 | src/frontmatter.xml, aviso de licença | O texto chama de seção o local em que a cópia integral da licença aparece como apêndice; a divergência também aparece na versão inglesa do aviso da edição brasileira. | Corrigidos os dois avisos, em português e inglês, para “apêndice”. |

### Correções matemáticas/editoriais de problemas herdados da fonte

| ID | Local | Problema de origem | Tratamento em T1 |
|---|---|---|---|
| SRC-01 | src/algcodes.xml, lema da matriz de verificação de paridade | Índices incompatíveis na segunda soma de HG: a matriz A é m × (n−m), mas a soma usa linhas fora desse intervalo. | Ajustados os índices para δᵢ,ₖ₋₍ₙ₋ₘ₎ aₖ₋₍ₙ₋ₘ₎,ⱼ. |
| SRC-02 | src/algcodes.xml, paridade par | “Não é possível detectar erros múltiplos” é absoluto demais: alguns padrões múltiplos são detectados, outros não. | “Erros múltiplos nem sempre são detectáveis.” |
| SRC-03 | src/sylow.xml, demonstração sobre grupo de ordem 1645 | A referência a H ficou sem o índice que distingue os subgrupos. | Corrigida para H₁. |
| SRC-04 | src/boolean.xml, dica de circuito | A igualdade final da dica é falsa; a expressão simplifica para a′ ∧ b. | Corrigida a igualdade. |
| SRC-05 | src/boolean.xml, descrição alternativa do circuito | A descrição diz b′, enquanto o diagrama apresenta a′. | Alinhada a descrição ao rótulo a′ do diagrama. |
| SRC-06 | src/fields.xml, exemplo com raiz sexta | A expressão oferece uma alternativa falsa para o valor de (√[6]5)⁷ i. | Mantida a identidade correta, sem a alternativa errada. |
| SRC-07 | src/fields.xml, construção por interseção de círculos | A equação da circunferência repete e₁x em vez de e₁y; a equação da corda contém b indefinido e diferenças incoerentes. | Corrigidas as duas fórmulas pela subtração das equações das circunferências. |
| SRC-08 | src/fields.xml, caracterização dos números construtíveis | O grau foi afirmado igual a 2ᵏ com k>0. O grau pode ser 1, e em geral divide o grau da torre, que é uma potência de 2. | A afirmação foi corrigida para “é uma potência de 2”; a demonstração explicita o limite dos graus das etapas e a divisibilidade pelo grau de Fₖ. A prova da equivalência completa ainda precisa de revisão editorial (ver pendências). |
| SRC-09 | src/fields.xml, exercício sobre GF(3⁵) | “Corpo de números” designa outra classe de corpos; o objeto construído é finito. | “Corpo finito construído no problema anterior.” |
| SRC-10 | src/finite.xml, introdução aos códigos polinomiais | Sobrejetividade de D não caracteriza correção de erros; para dimensão k, a matriz de verificação tem posto n−k e dimensão (n−k)×n. | A definição agora explicita um conjunto de padrões admissíveis que contém o vetor nulo, a condição D(E(x)+e)=x e a dimensão/posto corretos de H. |
| SRC-11 | src/finite.xml, demonstração para códigos polinomiais | Há um v excedente no coeficiente aₙ₋₁v. | Removido. |
| SRC-12 | src/finite.xml, descrição da rede de corpos | A descrição menciona p¹⁶, mas o diagrama contém p⁶. | Corrigida a descrição para p⁶. |
| SRC-13 | src/galois.xml, lema sobre transposições em Sₚ | A família (1 n), com 1≤n<p, inclui a identidade e deixa de fora (1 p). | Corrigida para (1 j), 2≤j≤p. |
| SRC-14 | src/galois.xml, descrição de gráfico | O máximo local em torno de 68 ocorre para x≈−2, não x≈2. | Corrigido o sinal na descrição alternativa. |
| EDT-01 | src/actions.xml, exemplo de classe de conjugação | T0 acrescentava uma ressalva sobre NP-completude sem marcar a intervenção; a frase-fonte também confundia dificuldade no pior caso com impossibilidade de resolver toda instância grande. | A ressalva foi identificada como “Nota editorial” e agora explica a imprecisão da fonte. |

A correção do termo “p-subgrupo maximal” segue usos brasileiros como [UFV](https://posmatematica.ufv.br/wp-content/uploads/2018/01/Dissertacao-Carlos-Henrique-Alves-Costa..pdf) e [UnB](https://repositorio.unb.br/bitstream/10482/15427/1/2013_FranciscoEniodoNascimentoLima.pdf). Para “corpo finito” e “corpo de números”, consultei também o uso que distingue as duas noções em material acadêmico brasileiro, como [SciELO](https://books.scielo.org/id/7jqhc/pdf/alves-9788568334393-02.pdf) e [IMPA](https://w3.impa.br/~library/cbm/26CBM/26CBM_13.pdf). A verificação terminológica externa foi direcionada, não uma busca exaustiva em toda a bibliografia brasileira.

## Emendas corretas já existentes em T0 e preservadas

A revisão não reverteu correções matemáticas úteis que já estavam na edição brasileira: valor absoluto em m.m.c. de inteiros; quantificador correto nas leis de expoentes; verificação ISBN como valor 10 no décimo dígito; ramo correto de arctan e parênteses em De Moivre; condição θ≠0 no exercício sobre ordem infinita; distinção entre simetrias rotacionais do tetraedro e todas as simetrias; códigos RSA/Fermat; dimensão do núcleo de G; raio de código perfeito; sinais no lema de Sylow; correções de polinômios em corpos finitos; e qualificações de teoremas de Galois. A lista de intervenções anteriores consta da auditoria da edição-base e foi considerada nesta reconciliação.

## Pendências identificadas que exigem decisão ou validação adicional

Estas pendências foram separadas de erros de tradução confirmados e não foram alteradas automaticamente neste PR:

- src/matrix.xml: sinal do item sobre matriz identidade; transposta inválida em matrix-theorem-orthnormal-matrix; divergências entre parâmetros e fórmulas de translação na seção sobre isometrias; uso de origem que não precisa ser fixada por grupos finitos de simetrias; formulação histórica ambígua sobre grupos cristalográficos.
- src/struct.xml e src/normal.xml: expoente sem índice em lema de p-grupos; formulação sobre a ordem de hᵖ; hipótese de finitude ausente em exercício de série solúvel; subgrupo mencionado incorretamente em exercício sobre comutadores; índices/pontuação em lema de 3-ciclos.
- src/actions.xml: tupla (3,6.12,9) na tabela de permutações parece conter separador ou índice incorreto.
- src/permute.xml: possível deslocamento de índice entre vértices e reflexões em Dₙ; depende da convenção de ação e orientação adotada.
- src/fields.xml: a prova da caracterização por torre não desenvolve as duas direções da equivalência e convém explicitar as hipóteses sobre as raízes quadradas reais.
- src/galois.xml: uma afirmação do Teorema Fundamental da Álgebra não explicita “não constante”.
- Aviso de licença em src/frontmatter.xml: a edição-fonte permite GFDL 1.2 ou posterior, enquanto o aviso brasileiro cita 1.3 e o texto incorporado é 1.3. A remissão ao apêndice foi corrigida, mas a escolha da versão exige validação dos responsáveis pelos direitos autorais.

## Validação e limites

- O cotejo textual e matemático da revisão foi concluído nos arquivos relacionados em coverage.csv.
- A comparação direta confirmou que os textos completos de src/gfdl.xml e src/gfdl-mathbook.xml são idênticos entre S e T0. src/index.xml também é idêntico. O histórico brasileiro em src/history.xml é um paratexto específico da tradução.
- A compilação-base do projeto passou na rodada anterior. A compilação e os workflows do novo PR ainda precisam rodar; seus resultados serão registrados em outputs.md.
- Não houve inspeção visual de PDF renderizado nem execução do código Sage nesta rodada; conferimos o código e a coerência das saídas textuais disponíveis.
- Links externos e referências bibliográficas não foram submetidos a verificação exaustiva de disponibilidade, edição e paginação.
- A revisão não substitui a leitura editorial humana independente exigida pelo processo do projeto. A decisão sobre emendas da fonte e a validação jurídica permanecem com os responsáveis pela edição.
