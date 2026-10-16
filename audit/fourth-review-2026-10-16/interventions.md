# Intervenções editoriais e adjudicação de correções da fonte

## Regra aplicada

Correções confirmadas de fórmulas, hipóteses, afirmações, provas ou descrições acessíveis recebem nota editorial próxima ao trecho. As descrições acessíveis permanecem estritamente descritivas; a nota explicativa fica na dica ou legenda. Uma interpretação incerta é apresentada como tal. Clarificações que não corrigiam erro não foram mantidas como alterações silenciosas.

## Emendas confirmadas com nota editorial no livro

| IDs | Local | Tratamento em T1 e evidência resumida |
|---|---|---|
| SRC-01 | algcodes.xml, lema da matriz de verificação | Corrigidos os índices da delta e da entrada de A; a segunda soma volta a ser aᵢⱼ. Nota junto à prova. |
| SRC-02 | algcodes.xml, paridade par | “Erros múltiplos nem sempre são detectáveis”; paridade detecta quantidades ímpares e falha em quantidades pares. Nota junto à afirmação. |
| SRC-03 | sylow.xml, grupo de ordem 1645 | Corrigidos H para H₁ e o índice i=1,2 para i=2,3; os quocientes indicados implicam G′≤H₂,H₃. Nota no exemplo. |
| SRC-04 | boolean.xml, dica do circuito | Corrigido o segundo membro para a′∧b; os lados originais simplificam-se para a′∧b e a. Nota na dica. |
| SRC-05 | boolean.xml, circuito parte a | Descrição alternativa corrigida de b′ para a′ em confronto com o rótulo TikZ. Nota junto à dica; descrição acessível não contém comentário editorial. |
| SRC-06 | fields.xml, base com ⁶√5 | Removida a alternativa falsa, pois (⁶√5)⁷i=5·⁶√5i. Nota no exemplo. |
| SRC-07 | fields.xml, duas circunferências | Corrigidos e₁x para e₁y e os coeficientes/sinais da equação da corda. Nota no parágrafo. |
| SRC-08 | fields.xml, grau de número construtível | Substituída a igualdade exata por “potência de 2”; o grau divide o grau da torre e pode ser 1. Nota no enunciado. |
| SRC-09 | fields.xml, Sage sobre ℤ₃ | Substituído “corpo de números” por “corpo finito”; o quociente anterior tem ordem 3⁵. Nota no exercício. |
| SRC-10 | finite.xml, definição de código corretor | Substituída sobrejetividade de D por recuperação para um conjunto declarado de erros; ajustados dimensão e posto de H. Nota na definição. |
| SRC-11 | finite.xml, prova dos códigos BCH | Removido o v excedente de aₙ₋₁v tⁿ⁻¹. Nota na prova. |
| SRC-12 | finite.xml, reticulado de subcorpos | Descrição corrigida de p¹⁶ para p⁶; 16 não divide 24. Nota na legenda, não no texto alternativo. |
| SRC-13 | galois.xml, lema gerador de Sₚ | Intervalo corrigido para 2≤j≤p; o original incluía identidade e omitia (1,p). Nota na prova. |
| SRC-14 | galois.xml, gráfico da quíntica | Descrição alternativa corrigida: máximo local no lado x≈−2,177. Nota na legenda. |
| SRC-15 | matrix.xml, dica da identidade | Sinal da norma de x corrigido de positivo para negativo. Nota na dica. |
| SRC-16 | matrix.xml, prova sobre matriz ortogonal | Removida a transposta final de eⱼ; eᵢᵀMeⱼ recupera Mᵢⱼ. Nota na prova. |
| SRC-17 | actions.xml, tabela de permutações | Ciclo inválido (3,6.12,9) corrigido para (3,6,12,9). Nota no parágrafo que introduz a tabela. |
| SRC-19 | struct.xml, séries de grupos solúveis | Acrescentada hipótese de grupo finito, necessária para a equivalência. Nota com contraexemplo ℤ. |
| SRC-22 | fields.xml, interseções de retas/circunferências | Discriminante ≥0 inclui a tangência omitida pela desigualdade estrita. Nota junto à derivação. |
| SRC-23 | fields.xml, teorema da torre | Acrescentada a direção recíproca por indução; a leitura como torre real com radicandos não negativos é identificada como interpretação editorial. Duas notas, uma no enunciado e outra na prova. |
| SRC-24 | galois.xml, Teorema Fundamental da Álgebra | Acrescentada a hipótese “não constante”; constantes não nulas não têm raízes. Nota no enunciado. |
| SRC-25 | galois.xml, introdução ao teorema | Preservada a correção para fatores contando multiplicidades; a nota já presente em T0 identifica a emenda e a restrição a polinômios não constantes. |
| SRC-26 | permute.xml, reflexões de Dₙ | Mantida a classificação dos eixos pelos vértices e pelos pontos médios dos lados; a nota esclarece que o argumento gerador posterior não depende da rotulagem defeituosa da fonte. |

## Interpretação editorial provável, sujeita a confirmação

| ID | Local | Tratamento |
|---|---|---|
| SRC-18 | struct.xml, série derivada | A fonte pede provar normalidade de G⁽ⁱ⁺¹⁾ em si mesmo, pois G⁽ⁱ⁺¹⁾=(G⁽ⁱ⁾)′. T1 interpreta o grupo ambiente como G⁽ⁱ⁾, mas a nota declara que a intenção autoral não foi confirmada. A aprovação humana dessa emenda continua pendente. |

## Alegações rejeitadas após o cotejo; alterações revertidas

| ID | Local | Decisão |
|---|---|---|
| SRC-20 | normal.xml, lema sobre 3-ciclos | “3-ciclo” já implica três índices distintos; foi restaurado o intervalo original 1≤k≤n. A exclusão explícita de i,j não é registrada como correção da fonte. |
| SRC-21 | fields.xml, lema da raiz quadrada | No contexto de números reais, √α só está definido para α≥0; a restrição isolada foi revertida por ser uma explicitação de domínio implícita, não uma correção confirmada. |

## Nota editorial de convenção

EDT-02 mantém identificada como nota editorial a convenção de multiplicação da esquerda para a direita em permute.xml. A nota não é atribuída ao original.
