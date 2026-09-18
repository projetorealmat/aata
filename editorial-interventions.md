# Registro de intervenções editoriais

Este arquivo registra divergências deliberadas entre a tradução brasileira e o texto-fonte em inglês. As intervenções abaixo não são alterações feitas silenciosamente no original upstream.

## REV-AATA-002 — Teorema sobre ideais maximais em $F[x]$

- **Arquivo:** `src/poly.xml`
- **Elemento:** `poly-theorem-max-ideal`
- **Fonte upstream:** `twjudson/aata`, commit `3069910e3ded72ff5e18837a97a0e810c92790e2`
- **Base da tradução:** `projetorealmat/aata`, commit `eb7cbda7f754917a7a61ebfb51ce01e26bd451a6`
- **Localização:** parágrafo da prova correspondente às linhas 1068–1069 da base da tradução.

### Redação da fonte

> If $g(x)$ is constant, then $f(x)$ is a constant multiple of $I$ and $I = \langle p(x) \rangle$.

### Redação adotada na tradução

> Se $g(x)$ é constante, então $f(x)$ é um múltiplo constante de $p(x)$ e $I = \langle p(x) \rangle$.

### Justificativa

No parágrafo anterior, a prova estabelece

\[
p(x)=f(x)g(x).
\]

Como $p(x)$ é irredutível, um dos fatores é constante. No caso em que $g(x)$ é constante, esse fator deve ser uma constante não nula, portanto uma unidade de $F[x]$. Consequentemente, $f(x)$ é um múltiplo constante de $p(x)$, e os ideais gerados coincidem:

\[
\langle f(x)\rangle=\langle p(x)\rangle.
\]

A expressão inglesa “a constant multiple of $I$” não é adequada nesse ponto: $I$ é um ideal, enquanto $f(x)$ é um polinômio; além disso, ela não corresponde à fatoração estabelecida nem justifica corretamente a conclusão. A redação portuguesa preserva a inferência matemática necessária e diverge do original para corrigir esse provável erro tipográfico ou editorial da fonte.

Essa correção foi registrada neste arquivo para manter a rastreabilidade da divergência; o texto original upstream não foi alterado.
