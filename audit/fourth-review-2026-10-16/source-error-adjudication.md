# Adjudicação das alegações de erro na fonte

## Escopo e decisão geral

Reexaminamos todos os IDs SRC-01–SRC-26 registrados nas auditorias cumulativas da terceira e da quarta rodada, cotejando o original congelado em `twjudson/aata@3069910e3ded72ff5e18837a97a0e810c92790e2`, a tradução-base pós-PR #34 e a versão proposta neste PR. A conferência combinou leitura do contexto, cálculo matemático, inspeção dos ativos vinculados e contraexemplos quando aplicáveis.

| Resultado da adjudicação | IDs | Decisão |
|---|---|---|
| Problema da fonte confirmado | SRC-01–SRC-17, SRC-19, SRC-22–SRC-26 | Emenda mantida; nota editorial localizada no livro. Três desses casos são erros nas descrições acessíveis de figuras, não nos desenhos. |
| Problema pedagógico provável; intenção exata não confirmada | SRC-18 | A fonte pede provar uma tautologia. A redação de T1 é uma interpretação editorial plausível, sinalizada no próprio exercício; requer confirmação humana. |
| Alegação não confirmada como erro da fonte | SRC-20 e SRC-21 | As condições são implícitas na notação de 3-ciclo e de raiz quadrada real. As explicitações de T1 foram revertidas para preservar a redação da fonte. |

Os 23 IDs confirmados não representam 23 erros de tradução: identificam problemas preexistentes no original ou em seus metadados. SRC-08 e SRC-23 tratam de defeitos diferentes no mesmo teorema: uma afirmação de grau falsa e uma lacuna na prova do bicondicional.

## Casos adjudicados

### SRC-01 — Produto da matriz de verificação pela matriz geradora

**Veredito: confirmado.** Com H = (A | Iₘ) e G = (Iₙ₋ₘ; A), a segunda soma da entrada cᵢⱼ deve usar δᵢ,ₖ₋₍ₙ₋ₘ₎ Aₖ₋₍ₙ₋ₘ₎,ⱼ. A fórmula original desloca os índices da delta e usa uma linha de A indexada pelo bloco inteiro de H; por isso, o cálculo não é válido como impresso. Com a mudança, cada uma das duas somas vale aᵢⱼ e a soma é zero em ℤ₂. A emenda está acompanhada de nota editorial na prova.

### SRC-02 — Alcance da detecção por paridade

**Veredito: confirmado.** Um bit de paridade detecta qualquer quantidade ímpar de inversões de bits e não detecta uma quantidade par. O exemplo da fonte, que inverte dois bits, demonstra apenas um padrão múltiplo não detectado; não justifica a afirmação universal de que múltiplos erros nunca são detectáveis. A tradução agora diz “nem sempre” e a nota explicita o alcance correto.

### SRC-03 — Índices dos subgrupos no argumento de ordem 1645

**Veredito: confirmado.** A unicidade do subgrupo H₁ de ordem 47 e a abelianidade de G/H₁ implicam G′ ≤ H₁. Depois, os quocientes por H₂ e H₃, de ordens 5 e 7, são abelianos; logo G′ está contido em ambos e sua ordem divide 5 e 7. A fonte escreveu H sem índice na primeira inclusão e i=1,2 na segunda referência, embora os subgrupos relevantes fossem H₂ e H₃. T1 corrige as duas referências e a nota as identifica.

### SRC-04 — Identidade no exercício de álgebra booleana

**Veredito: confirmado.** Pela distributividade e pelas leis de complemento, a′ ∧ [(a ∧ b′) ∨ b] = a′ ∧ b. Já a ∧ (a ∨ b) = a. Portanto, a igualdade da fonte é falsa em geral. A dica foi corrigida e a nota informa a simplificação que justifica a emenda.

### SRC-05 — Descrição acessível do circuito

**Veredito: confirmado como erro de metadado acessível.** A descrição textual original chama o terceiro caminho de b′, mas o TikZ da própria fonte o rotula a′; os outros rótulos são a e b. A descrição portuguesa acompanha o diagrama. A nota foi colocada junto à dica, e não dentro do texto alternativo, para não fazer a explicação editorial ser lida como parte da figura.

### SRC-06 — Potência de uma raiz sexta

**Veredito: confirmado.** (⁶√5)⁷ i = 5·⁶√5 i, pois 5⁷ᐟ⁶ = 5·5¹ᐟ⁶. A alternativa ⁶√5 i apresentada pela fonte não é igual a essa potência. T1 remove apenas a alternativa falsa e explica a conta em nota.

### SRC-07 — Interseção de duas circunferências

**Veredito: confirmado.** Na primeira equação, o termo linear em y deve ser e₁y, não e₁x. Subtraindo as equações das circunferências, obtém-se (d₁−d₂)x + (e₁−e₂)y + (f₁−f₂)=0. A fórmula original para a corda contém um b não definido e sinais incompatíveis com essa subtração. T1 corrige ambas as fórmulas; a nota discrimina os dois problemas.

### SRC-08 — Grau de um número construtível

**Veredito: confirmado.** Se α pertence ao último corpo Fₖ da torre, então ℚ(α) ⊆ Fₖ e [ℚ(α):ℚ] divide [Fₖ:ℚ]. Como o grau da torre é uma potência de 2, o grau de α também é uma potência de 2, possivelmente 1. A fonte afirmava que ele era exatamente 2ᵏ para algum k>0; por exemplo, α=1 tem grau 1. T1 dá a conclusão divisória correta, com nota editorial.

### SRC-09 — “Corpo de números” no exercício com ℤ₃

**Veredito: confirmado.** O exercício anterior constrói o quociente ℤ₃[x]/(p), isomorfo a um corpo finito de ordem 3⁵. Esse corpo tem característica 3 e não é um corpo de números, que é uma extensão finita de ℚ. A expressão foi corrigida e a nota informa a distinção.

### SRC-10 — Definição de código corretor de erros

**Veredito: confirmado.** A sobrejetividade de D só garante que todos os símbolos de mensagem aparecem como saídas; não garante sequer que D(E(x))=x quando nenhum erro ocorreu, nem que D recupere a mensagem após um erro admissível. A caracterização precisa declarar o conjunto de erros e exigir D(E(x)+e)=x para cada mensagem e erro permitido, incluindo e=0. Além disso, para um código linear de dimensão k em ℤ₂ⁿ, uma matriz de verificação H deve ter posto n−k; a dimensão (n−k)×n é a apresentação usual de posto completo. T1 substitui a definição insuficiente por essa condição e registra a intervenção em nota.

### SRC-11 — Símbolo excedente no polinômio de código BCH

**Veredito: confirmado.** A fonte escreve o termo final como aₙ₋₁ v tⁿ⁻¹, embora v não tenha sido definido e a representação do elemento de Rₙ seja f(t)=a₀+a₁t+⋯+aₙ₋₁tⁿ⁻¹. O v é um caractere excedente, não um fator do polinômio. T1 o remove e sinaliza a correção.

### SRC-12 — Descrição acessível do reticulado de subcorpos

**Veredito: confirmado como erro de metadado acessível.** O desenho ativo tem Fₚ⁶ no quarto nível; a descrição original diz Fₚ¹⁶. A divergência também pode ser detectada estruturalmente: Fₚ¹⁶ não é subcorpo de Fₚ²⁴, pois 16 não divide 24. T1 mantém a descrição compatível com o desenho e a nota fica na legenda, fora do texto alternativo.

### SRC-13 — Intervalo das transposições em Sₚ

**Veredito: confirmado.** O conjunto gerador pretendido é formado pelas p−1 transposições (1,j), para 2≤j≤p. O intervalo original 1≤n<p inclui (1,1), que é a identidade, e exclui (1,p). T1 corrige os extremos e a nota explica por que.

### SRC-14 — Máximo local na descrição do gráfico

**Veredito: confirmado como erro de metadado acessível.** Para f(x)=x⁵−6x³−27x−3, f′(x)=5x⁴−18x²−27. As raízes críticas reais satisfazem x²=1,8+1,2√6, logo x≈±2,177. O ponto negativo é o máximo local, perto de 68,8; o positivo é o mínimo, perto de −74,8. A descrição original atribui o máximo ao lado positivo. T1 corrige o texto alternativo e a nota aparece na legenda.

### SRC-15 — Sinal na dica da identidade de polarização

**Veredito: confirmado.** A identidade exige ½(‖x+y‖²−‖x‖²−‖y‖²). Expandir ‖x+y‖² confirma os dois sinais de subtração. A fonte traz sinal positivo diante de ‖x‖² na primeira expressão da dica, tornando inválida a igualdade seguinte. T1 corrige o sinal e acrescenta nota.

### SRC-16 — Dimensões na recuperação da entrada Mᵢⱼ

**Veredito: confirmado.** Para vetores da base padrão, Mᵢⱼ=eᵢᵀMeⱼ: o primeiro fator é vetor-linha e o último é vetor-coluna. A fonte transpõe também eⱼ, produzindo um produto linha–matriz–linha que não está definido. T1 remove a transposta final; a nota mostra a razão dimensional.

### SRC-17 — Ciclo com pontuação decimal na tabela

**Veredito: confirmado como erro de notação.** A entrada “(3,6.12,9)” não é um ciclo de permutação, pois 6.12 não é um símbolo inteiro. A ação da permutação de variáveis fornece (3,6,12,9), cuja órbita tem comprimento 4; com os demais ciclos e dois pontos fixos, a tabela totaliza os seis ciclos indicados. T1 insere a vírgula faltante e sinaliza a emenda.

### SRC-18 — Normalidade na série derivada

**Veredito: defeito pedagógico confirmado; emenda exata provável, não confirmada.** Pela definição, G⁽ⁱ⁺¹⁾=(G⁽ⁱ⁾)′. Portanto, a instrução original pede provar que um grupo é normal em si mesmo, o que é sempre verdadeiro e não demonstra que a série derivada é uma série normal. A troca do grupo ambiente por G⁽ⁱ⁾ é matematicamente natural, pois o subgrupo derivado é característico em G⁽ⁱ⁾, mas a intenção autoral não pode ser deduzida com certeza apenas do texto. T1 mantém essa interpretação somente com uma nota que declara a tautologia e a incerteza; a decisão final deve ser confirmada por um editor humano ou pelos autores.

### SRC-19 — Hipótese de finitude na caracterização dos grupos solúveis

**Veredito: confirmado.** O grupo aditivo ℤ é abeliano e, portanto, solúvel, mas não pode ter uma série finita cujos fatores tenham todos ordem prima: índices finitos sucessivos tornariam o grupo total finito. Para grupos finitos, a caracterização por fatores de ordem prima é válida via uma série de composição. T1 acrescenta “grupo finito” e a nota registra o contraexemplo que exige a hipótese.

### SRC-20 — Índices distintos no lema sobre 3-ciclos

**Veredito: alegação de erro não confirmada.** A fonte afirma que os 3-ciclos (i,j,k) variam com 1≤k≤n. A expressão “3-ciclo (i,j,k)” já restringe o domínio a três símbolos distintos; a faixa 1≤k≤n é entendida dentro desse domínio. Excluir i e j explicita essa convenção e evita interpretar a fórmula de conjugação fora de seu domínio, mas não corrige uma conclusão falsa. T1 restaura a faixa original. T1 volta à formulação da fonte, sem nota de erro.

### SRC-21 — Domínio da raiz quadrada de número construtível

**Veredito: alegação de erro não confirmada.** O capítulo trata de números construtíveis reais e usa √α como raiz quadrada real; a expressão só está definida quando α≥0. A restrição está implícita na convenção do radical real. A inclusão explícita de “não negativo” era uma clarificação possível, mas não corrige uma afirmação falsa. T1 restaura a redação sem essa inclusão. No teorema da torre, a edição declara separadamente que interpreta os radicandos como não negativos para deixar explícita a leitura por corpos reais.

### SRC-22 — Discriminante e tangência

**Veredito: confirmado como lacuna de caso na prova.** Para a equação quadrática obtida ao eliminar uma coordenada, discriminante zero corresponde à raiz dupla da tangência. O ponto de interseção continua real e pertence ao corpo anterior, pois √0=0. A fonte exige discriminante estritamente positivo e omite esse caso da descrição geral; T1 usa α≥0 e a nota aponta a tangência.

### SRC-23 — Recíproca do teorema da torre

**Veredito: lacuna confirmada.** A prova original parte de uma construção geométrica e produz uma torre; isso demonstra somente uma direção, não o “se, e somente se”. A recíproca requer indução: se Fᵢ₋₁ está no corpo dos construtíveis e αᵢ≥0 é construtível, √αᵢ também é; como os construtíveis formam subcorpo, Fᵢ continua contido nele. T1 acrescenta essa indução e inclui nota que atribui a prova suplementar à edição. A condição αᵢ≥0 é explicitada como interpretação da torre real, não apresentada como uma segunda falsidade demonstrada no original.

### SRC-24 — Raiz de polinômio constante

**Veredito: confirmado.** Um polinômio constante não nulo em ℂ[x] não tem raiz. A afirmação de que todo polinômio de ℂ[x] tem uma raiz exige a hipótese de não constância. T1 a acrescenta ao enunciado do Teorema Fundamental da Álgebra e informa a razão em nota.

### SRC-25 — Fatores distintos no Teorema Fundamental da Álgebra

**Veredito: confirmado e já corrigido em T0; a nota foi mantida e ampliada.** Por exemplo, (x−a)² não se fatora em fatores lineares distintos; a formulação correta conta multiplicidades e não exige raízes distintas. A edição diz “contando multiplicidades” e a nota identifica a emenda da fonte, além de apontar a hipótese de não constância tratada no enunciado do teorema.

### SRC-26 — Reflexões do grupo diédrico para n par

**Veredito: confirmado e já corrigido em T0; a nota foi refinada.** Para n par existem n/2 eixos por pares de vértices opostos e n/2 eixos pelos pontos médios de lados opostos. Só as reflexões do primeiro tipo fixam vértices. A fonte rotula as reflexões por vértices fixos e, assim, não representa o segundo tipo nessa descrição. Isso não invalida o argumento posterior que gera o grupo a partir de uma rotação e uma reflexão; o defeito está na classificação/rotulagem das reflexões. T1 explicita os dois tipos e preserva uma nota com essa delimitação.

## Regra editorial aplicada no livro

Toda correção confirmada que altera uma fórmula, hipótese, conclusão, argumento ou descrição acessível recebe uma nota editorial próxima ao trecho. A nota identifica o que a fonte dizia ou omitia e resume a evidência que justifica a emenda. Nos erros de descrição acessível, o texto alternativo descreve apenas a figura efetiva; a explicação editorial fica na dica ou legenda, sem poluir a descrição lida por tecnologias assistivas. A emenda SRC-18 é marcada como interpretação provável, e não como intenção autoral certa. Quando a alegação não se confirmou (SRC-20 e SRC-21), a alteração foi revertida e não se atribuiu erro à fonte.

## Pontos que continuam pendentes

A nota de SRC-18 exige validação editorial humana da interpretação. Outros itens já separados no relatório da rodada anterior continuam fora desta adjudicação: inconsistências entre parâmetros e fórmulas de translação e a escolha da origem em matrix.xml; formulação histórica sobre grupos cristalográficos; notação/expoente em um lema de p-grupos; e a divergência entre a licença GFDL “1.2 ou posterior” da fonte e a versão 1.3 da edição brasileira. Nenhum desses pontos foi alterado nesta etapa.
