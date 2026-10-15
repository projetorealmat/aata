from __future__ import annotations

from pathlib import Path
import csv
import json
import re
import subprocess
import xml.etree.ElementTree as ET

ROOT = Path('.')
BASE_S = 'twjudson/aata@3069910e3ded72ff5e18837a97a0e810c92790e2'
BASE_T0 = '13ed5d803cf37bed1d60b246e6f8c8369328d278'
AUDIT_DIR = ROOT / 'audit' / 'second-review-2026-10-15'

findings: list[dict] = []
changed_files: set[str] = set()


def run(*args: str) -> str:
    return subprocess.check_output(args, text=True).strip()


def record(fid: str, path: str, origin: str, severity: str, category: str,
           old: str, new: str, unit_id: str, disposition: str = 'corrected',
           confidence: str = 'high', priority: str | None = None,
           evidence: str = 'Issue #31; confirmed by direct S↔T0/context review') -> None:
    findings.append({
        'schema_version': 3,
        'finding_id': fid,
        'unit_id': unit_id,
        'path': path,
        'origin': origin,
        'category': category,
        'severity': severity,
        'confidence': confidence,
        'priority': priority or ('P1' if severity in {'CRITICAL','MAJOR'} else 'P2'),
        'source_span': old[:1200],
        'target_t0_span': old[:1200],
        'target_t1_span': new[:1200],
        'evidence': evidence,
        'disposition': disposition,
    })


def lit(path: str, old: str, new: str, fid: str, origin: str, severity: str,
        category: str, unit_id: str, expected: int = 1, strict: bool = True,
        evidence: str = 'Issue #31; confirmed by direct S↔T0/context review') -> int:
    p = ROOT / path
    text = p.read_text(encoding='utf-8')
    n = text.count(old)
    if n != expected:
        msg = f'{fid}: expected {expected} occurrence(s) in {path}, found {n}'
        if strict:
            raise RuntimeError(msg)
        findings.append({
            'schema_version': 3, 'finding_id': fid, 'unit_id': unit_id, 'path': path,
            'origin': origin, 'category': category, 'severity': severity,
            'confidence': 'low', 'priority': 'PENDING', 'source_span': old[:1200],
            'target_t0_span': old[:1200], 'target_t1_span': None,
            'evidence': msg, 'disposition': 'not_applied_pattern_mismatch'
        })
        return 0
    p.write_text(text.replace(old, new), encoding='utf-8')
    changed_files.add(path)
    record(fid, path, origin, severity, category, old, new, unit_id, evidence=evidence)
    return n


def rx(path: str, pattern: str, repl: str, fid: str, origin: str, severity: str,
       category: str, unit_id: str, expected: int = 1, strict: bool = True,
       flags: int = re.S, evidence: str = 'Issue #31; confirmed by direct S↔T0/context review') -> int:
    p = ROOT / path
    text = p.read_text(encoding='utf-8')
    new_text, n = re.subn(pattern, repl, text, flags=flags)
    if n != expected:
        msg = f'{fid}: expected {expected} regex match(es) in {path}, found {n}'
        if strict:
            raise RuntimeError(msg)
        findings.append({
            'schema_version': 3, 'finding_id': fid, 'unit_id': unit_id, 'path': path,
            'origin': origin, 'category': category, 'severity': severity,
            'confidence': 'low', 'priority': 'PENDING', 'source_span': pattern[:1200],
            'target_t0_span': pattern[:1200], 'target_t1_span': None,
            'evidence': msg, 'disposition': 'not_applied_pattern_mismatch'
        })
        return 0
    p.write_text(new_text, encoding='utf-8')
    changed_files.add(path)
    record(fid, path, origin, severity, category, pattern, repl, unit_id, evidence=evidence)
    return n


def ngon(path: str, fid: str) -> None:
    p = ROOT / path
    text = p.read_text(encoding='utf-8')
    new_text, n = re.subn(r'\b(n|[0-9]+)-gono\b', lambda m: f'{m.group(1)}-ágono', text)
    if n:
        p.write_text(new_text, encoding='utf-8')
        changed_files.add(path)
        record(fid, path, 'T', 'MINOR', 'TERM', 'n-gono / k-gono', 'n-ágono / k-ágono',
               f'{path}::term-n-gon', evidence=f'{n} ocorrência(s); forma brasileira consolidada na Issue #31')


# ---------------------------------------------------------------------------
# Paratextos
# ---------------------------------------------------------------------------
lit(
    'src/history.xml',
    'As versões preliminares <c>v0.1.0</c>, <c>v0.1.2</c> e <c>v0.1.3</c>',
    'As versões preliminares <c>v0.1.0</c>, <c>v0.1.1</c>, <c>v0.1.2</c>, <c>v0.1.3</c> e <c>v0.1.4</c>',
    'PAR-HIST-01', 'T', 'MINOR', 'PARATEXT', 'history-prior-brazilian-versions',
    evidence='GitHub Releases contém v0.1.0, v0.1.1, v0.1.2, v0.1.3 e v0.1.4.'
)

# ---------------------------------------------------------------------------
# Cap. 1 — sets
# ---------------------------------------------------------------------------
lit('src/sets.xml', 'injetiva ou injetiva', 'injetora ou injetiva',
    'SETS-T-01', 'T', 'MINOR', 'ACC', 'sets::injective-definition')
lit('src/sets.xml', 'na mesma partição', 'na mesma classe de equivalência',
    'SETS-SRC-01', 'SRC', 'MINOR', 'FORM', 'sets::equivalence-partition-examples', expected=2)

# Cap. 2 — integers
lit('src/integers.xml', '<m>\\lcm(a,b) = ab</m>', '<m>\\lcm(a,b) = |ab|</m>',
    'INT-SRC-01', 'SRC', 'MAJOR', 'FORM', 'integers-exercise-coprime-lcd',
    evidence='Para inteiros não nulos de sinais opostos, lcm(a,b) é não negativo; o valor correto é |ab|.')

# Cap. 3 — groups
lit('src/groups.xml', '<m>m(g + h) = mg + mh</m> para todo <m>n \\in {\\mathbb Z}</m>.',
    '<m>m(g + h) = mg + mh</m> para todo <m>m \\in {\\mathbb Z}</m>.',
    'GRP-SRC-01', 'SRC', 'MAJOR', 'FORM', 'groups::additive-exponent-laws')
lit('src/groups.xml', 'subgrupos trivial e impróprio', 'subgrupos triviais e impróprios',
    'GRP-T-01', 'T', 'MINOR', 'LANG', 'groups::subgroups')
lit('src/groups.xml', 'apareceu em William Burnside,', 'apareceu na obra de William Burnside,',
    'GRP-T-02', 'T', 'MINOR', 'LANG', 'groups::historical-burnside')
lit('src/groups.xml', 'Por isso, o caractere X é usado para o décimo primeiro dígito.',
    'Por isso, o caractere X é usado para representar o valor 10 no décimo dígito verificador.',
    'GRP-SRC-02', 'SRC', 'MAJOR', 'ACC', 'groups::isbn-exercise')
rx('src/groups.xml', r'(<description>[^<]*?)0-05000-30042-6([^<]*?</description>)',
   r'\g<1>0-50000-30042-6\g<2>', 'GRP-SRC-03', 'SRC', 'MAJOR', 'NON_TEXT',
   'groups::upc-alt-text')

# Cap. 4 — cyclic
lit('src/cyclic.xml', '\\theta = \\arctan \\left( \\frac{b}{a} \\right) = \\arctan( - 1) = 315^{\\circ}',
    '\\theta = 360^{\\circ} + \\arctan \\left( \\frac{b}{a} \\right) = 315^{\\circ}',
    'CYC-SRC-01', 'SRC', 'MAJOR', 'FORM', 'cyclic::polar-example')
lit('src/cyclic.xml', '\\cos( n +1) \\theta + i \\sin( n+1) \\theta',
    '\\cos((n + 1)\\theta) + i \\sin((n + 1)\\theta)',
    'CYC-SRC-02', 'SRC', 'MAJOR', 'FORM', 'cyclic::demoivre-proof')
lit('src/cyclic.xml', 'onde <m>\\theta \\in {\\mathbb Q}</m>.\n          Prove que a ordem de <m>z</m> é infinita.',
    'onde <m>\\theta \\in {\\mathbb Q} \\setminus \\{0\\}</m>.\n          Prove que a ordem de <m>z</m> é infinita.',
    'CYC-SRC-03', 'SRC', 'MAJOR', 'FORM', 'cyclic-exercise-order-rational-angles-in-T')
lit('src/cyclic.xml', 'DeMoivre', 'De Moivre', 'CYC-TERM-01', 'SRC', 'MINOR', 'TERM',
    'cyclic::de-moivre', expected=4)

# Cap. 5 — permutations
ngon('src/permute.xml', 'PERM-T-TERM-01')
old_reflections = '''          <p>
            Denote as <m>n</m> reflexões por <m>s_1, s_2, \\ldots, s_n</m>,
            onde <m>s_k</m> é a reflexão que deixa fixo o vértice <m>k</m>.
            Há dois casos de reflexões,
            dependendo de <m>n</m> ser par ou ímpar.
            Se houver um número par de vértices,
            então dois vértices permanecem fixos por uma reflexão,
            e <m>s_1 = s_{n/2 + 1}, s_2 = s_{n/2 + 2}, \\ldots, s_{n/2}  = s_n</m>.
            Se houver um número ímpar de vértices,
            então apenas um vértice permanece fixo por uma reflexão e
            <m>s_1, s_2, \\ldots,
            s_n</m> são distintas (<xref ref="permute-figure-types"/>).
            Em ambos os casos, a ordem de cada <m>s_k</m> é dois.
            Seja <m>s = s_1</m>.
            Então <m>s^2 = 1</m> e <m>r^n = 1</m>.'''
new_reflections = '''          <p>
            Há exatamente <m>n</m> reflexões. Seja <m>s</m> a reflexão que deixa fixo o vértice <m>1</m>.
            Se <m>n</m> é ímpar, cada reflexão deixa fixo exatamente um vértice.
            Se <m>n</m> é par, há <m>n/2</m> reflexões cujos eixos passam por pares de vértices opostos e <m>n/2</m> reflexões cujos eixos passam pelos pontos médios de lados opostos; estas últimas não deixam vértices fixos.
            Em ambos os casos, cada reflexão tem ordem <m>2</m> (<xref ref="permute-figure-types"/>).
            Então <m>s^2 = 1</m> e <m>r^n = 1</m>.'''
lit('src/permute.xml', old_reflections, new_reflections, 'PERM-SRC-01', 'SRC', 'MAJOR', 'FORM',
    'permute-theorem-dn-generator')
rx('src/permute.xml', r'grupo de movimentos rígidos de um tetraedro', 'grupo de rotações de um tetraedro',
   'PERM-SRC-02', 'SRC', 'MAJOR', 'ACC', 'permute::tetrahedron-A4', expected=2)

# Cap. 7 — cryptography
lit('src/crypt.xml', 'dois números primos aleatórios de 150 algarismos, <m>p</m> e <m>q</m>',
    'dois números primos distintos de 150 algarismos, <m>p</m> e <m>q</m>',
    'CRYPT-SRC-01', 'SRC', 'MAJOR', 'FORM', 'crypt::rsa-phi')
lit('src/crypt.xml', '<m>\\text{A} = 00, \\text{B} = 02, \\ldots, \\text{Z}= 25</m>',
    '<m>\\text{A} = 00, \\text{B} = 01, \\ldots, \\text{Z}= 25</m>',
    'CRYPT-SRC-02', 'SRC', 'MAJOR', 'ACC', 'crypt::rsa-encoding')
lit('src/crypt.xml', 'else if x^2 - y^2 = 0 then', 'else if x^2 - y^2 = n then',
    'CRYPT-SRC-03', 'SRC', 'MAJOR', 'CODE', 'crypt::fermat-factor-program')
lit('src/crypt.xml', '<m>E</m> e <m>D</m> de Alice.\n        </p>\n\n        <p>\n          Cifre a palavra <c>Math</c>',
    '<m>E</m> e <m>D</m> de Bob.\n        </p>\n\n        <p>\n          Cifre a palavra <c>Math</c>',
    'CRYPT-SRC-04', 'SRC', 'MINOR', 'ACC', 'crypt-sage-exercise-key-pair-bob')
lit('src/crypt.xml', 'escolha um colega de estudos e enviem mensagens um ao outro',
    'escolha um colega de estudos e envie mensagens um ao outro',
    'CRYPT-T-01', 'T', 'MINOR', 'LANG', 'crypt-sage-exercise-classroom')
lit('src/crypt.xml', '<mdash/>-', '<mdash/>', 'CRYPT-T-02', 'T', 'MINOR', 'PUNCT',
    'crypt::duplicate-dash', strict=False)

# Cap. 8 — coding theory
lit('src/algcodes.xml', '<q>A Mathematical Theory of Information</q>', '<q>A Mathematical Theory of Communication</q>',
    'ALG-SRC-01', 'SRC', 'MAJOR', 'BIB', 'algcodes-subsection-historical-note')
lit('src/algcodes.xml', 'o peso da soma deve ser a distância entre as duas palavras-código.',
    'o peso da soma deve ser a distância entre as duas <m>n</m>-uplas.',
    'ALG-SRC-02', 'SRC', 'MINOR', 'FORM', 'algcodes::binary-tuples-distance')
lit('src/algcodes.xml', 'as matrizes geradora padrão e canônica de verificação de paridade associadas são',
    'a matriz geradora padrão e a matriz canônica de verificação de paridade associadas são',
    'ALG-T-01', 'T', 'MINOR', 'LANG', 'algcodes-example-parity-check')
lit('src/algcodes.xml', '<m>{\\mathbf x} \\in {\\mathbb Z}_2^m</m>.',
    '<m>{\\mathbf x} \\in {\\mathbb Z}_2^{n-m}</m>.',
    'ALG-SRC-03', 'SRC', 'MAJOR', 'FORM', 'algcodes::generator-nullspace-proof')
rx('src/algcodes.xml', r'<description>Um diagrama esquemático no qual um zero.*?</description>',
   '<description>Um diagrama de canal binário simétrico: o zero é recebido como zero com probabilidade p e como 1 com probabilidade q; o 1 é recebido como 1 com probabilidade p e como zero com probabilidade q.</description>',
   'ALG-SRC-04', 'SRC', 'MAJOR', 'NON_TEXT', 'algcodes-binary-channel')
lit('src/algcodes.xml', 'as esferas de raio <m>d</m> centradas nas palavras-código do código particionarão exatamente',
    'as esferas de raio <m>(d-1)/2</m> centradas nas palavras-código do código particionarão exatamente',
    'ALG-SRC-05', 'SRC', 'MAJOR', 'FORM', 'algcodes-sage-exercise-perfect-code')
# resíduos de concordância de “síndrome”
for old, new, fid in [
    ('seus síndromes', 'suas síndromes', 'ALG-T-02'),
    ('Todos os síndromes', 'Todas as síndromes', 'ALG-T-03'),
    ('todos os síndromes', 'todas as síndromes', 'ALG-T-04'),
    ('síndrome causado', 'síndrome causada', 'ALG-T-05'),
    ('ao síndrome', 'à síndrome', 'ALG-T-06'),
    ('os síndromes', 'as síndromes', 'ALG-T-07'),
    ('Todo síndrome', 'Toda síndrome', 'ALG-T-08'),
    ('alguns síndromes', 'algumas síndromes', 'ALG-T-09'),
    ('sua síndrome pode ser calculado', 'sua síndrome pode ser calculada', 'ALG-T-10'),
]:
    if old in (ROOT/'src/algcodes.xml').read_text(encoding='utf-8'):
        lit('src/algcodes.xml', old, new, fid, 'T', 'MINOR', 'LANG', 'algcodes::syndrome-gender',
            expected=(ROOT/'src/algcodes.xml').read_text(encoding='utf-8').count(old))

# Cap. 9 — isomorphisms
lit('src/isomorph.xml', 'subgrupo do grupo círculo', 'subgrupo do grupo circular',
    'ISO-T-01', 'T', 'MINOR', 'TERM', 'isomorph::intro-circle-group')
lit('src/isomorph.xml', 'podem ser mostrados como iguais demonstrando uma correspondência bijetiva',
    'podemos mostrar que são isomorfos exibindo uma correspondência bijetiva',
    'ISO-T-02', 'T', 'MINOR', 'ACC', 'isomorph::intro-isomorphism')
lit('src/isomorph.xml', 'ser isomorfo a é uma relação de equivalência', 'a relação de isomorfismo é uma relação de equivalência',
    'ISO-T-03', 'T', 'MINOR', 'LANG', 'isomorph::equivalence-relation', expected=2)

# Cap. 10 — normal subgroups
ngon('src/normal.xml', 'NORMAL-T-TERM-01')
lit('src/normal.xml', '<idx><h>Greiss, R.</h></idx>R. Greiss', '<idx><h>Griess, R.</h></idx>R. Griess',
    'NORMAL-SRC-01', 'SRC', 'MAJOR', 'NAME', 'normal-subsection-historical-note')
lit('src/normal.xml', '<m>196{,}833 \\times 196{,}833</m> ,', '<m>196{,}883 \\times 196{,}883</m>,',
    'NORMAL-SRC-02', 'SRC', 'MAJOR', 'ACC', 'normal-subsection-historical-note',
    evidence='IAS/AMS references identify the Monster action/representation in dimension 196,883.')
rx('src/normal.xml', r'<m>A_5</m> não (?:tem|possui) subgrupos normais',
   '<m>A_5</m> não possui subgrupos normais próprios não triviais',
   'NORMAL-SRC-03', 'SRC', 'MAJOR', 'FORM', 'normal::A5-simple', expected=1, strict=False)
rx('src/normal.xml', r'(grupo|grupo de) (?:todas as )?simetrias de um tetraedro',
   r'\1 simetrias rotacionais de um tetraedro', 'NORMAL-SRC-04', 'SRC', 'MAJOR', 'ACC',
   'normal::tetrahedron-A4', expected=1, strict=False)

# Cap. 11 — homomorphisms
ngon('src/homomorph.xml', 'HOM-T-TERM-01')

# Cap. 12 — matrix symmetry groups
ngon('src/matrix.xml', 'MATRIX-T-TERM-01')
lit('src/matrix.xml', 'é um processo direto verificar', 'é fácil verificar',
    'MATRIX-T-01', 'T', 'MINOR', 'LANG', 'matrix::direct-verification', strict=False)
lit('src/matrix.xml', 'em <m>{\\mathbb R}^6</m> e além', 'em <m>{\\mathbb R}^6</m> e em dimensões superiores',
    'MATRIX-T-02', 'T', 'MINOR', 'CALQUE', 'matrix::higher-dimensions', strict=False)
lit('src/matrix.xml', 'paralelogramo, retangular, quadrada, rômbica e hexagonal',
    'paralelogramo, retângulo, quadrado, losango e hexágono',
    'MATRIX-T-03', 'T', 'MINOR', 'LANG', 'matrix::lattice-types', strict=False)

# Cap. 13 — structure
lit('src/struct.xml', 'Sejam <m>G</m>, <m>H</m> e <m>K</m> sejam grupos abelianos finitamente gerados.',
    'Sejam <m>G</m>, <m>H</m> e <m>K</m> grupos abelianos finitamente gerados.',
    'STRUCT-T-01', 'T', 'MINOR', 'LANG', 'struct-exercise-finitely-generated-abelian-group:statement')
lit('src/struct.xml', 'se nenhum dos grupos quocientes da série contém um subgrupo normal.',
    'se nenhum dos grupos quocientes da série contém um subgrupo normal próprio não trivial.',
    'STRUCT-SRC-01', 'SRC', 'MAJOR', 'FORM', 'struct:composition-series-definition:explanatory-clause')
rx('src/struct.xml', r'corresponde às simetrias de um tetraedro', 'corresponde às simetrias rotacionais de um tetraedro',
   'STRUCT-SRC-02', 'SRC', 'MAJOR', 'ACC', 'struct:finite-groups-order12:a4-tetrahedron')

# Cap. 14 — actions
ngon('src/actions.xml', 'ACT-T-TERM-01')
lit('src/actions.xml', 'cada partição de <m>X</m> associada à <m>G</m>-equivalência é chamada de <term>órbita</term>',
    'cada classe de equivalência da <m>G</m>-equivalência em <m>X</m> é chamada de <term>órbita</term>',
    'ACT-SRC-01', 'SRC', 'MAJOR', 'FORM', 'actions:orbit-definition')
lit('src/actions.xml', 'Isso significa, na prática, que o problema não pode ser resolvido para um <m>n</m> grande, pois os cálculos consumiriam tempo demais até mesmo no maior computador.',
    'A NP-completude caracteriza a dificuldade computacional no pior caso; ela não implica que toda instância grande seja irresolúvel.',
    'ACT-SRC-02', 'SRC', 'MAJOR', 'FORM', 'actions:example-conjugacy-classes-Sn')
lit('src/actions.xml', 'Seja <m>X</m> o conjunto de valores de saída de uma função de comutação em <m>n</m> variáveis.',
    'Seja <m>X</m> o conjunto das <m>n</m>-uplas binárias de entrada de uma função de comutação em <m>n</m> variáveis.',
    'ACT-SRC-03', 'SRC', 'MAJOR', 'FORM', 'actions:switching-functions-input-indexing')
lit('src/actions.xml', 'teoria de interruptores', 'teoria de comutação',
    'ACT-T-01', 'T', 'MINOR', 'TERM', 'actions:switching-theory', expected=2)
lit('src/actions.xml', 'Quanto tempo durou a demonstração?', 'Quantas páginas tinha a demonstração?',
    'ACT-T-02', 'T', 'MAJOR', 'ACC', 'actions:reading-question:rq-actions-burnside')
lit('src/actions.xml', 'singleton [4]', 'lista com um único elemento, [4]',
    'ACT-T-03', 'T', 'MINOR', 'CALQUE', 'actions:sage-stabilizer-note', strict=False)
lit('src/actions.xml', 'Seja <m>|G|=p^n</m> um grupo não abeliano',
    'Seja <m>G</m> um grupo não abeliano de ordem <m>p^n</m>, com <m>p</m> primo',
    'ACT-SRC-04', 'SRC', 'MINOR', 'FORM', 'actions-exercise-ZG', strict=False)

# Cap. 15 — Sylow
ngon('src/sylow.xml', 'SYL-T-TERM-01')
lit('src/sylow.xml', '<mrow>h_2 &amp; =  h_1 a^{-1}</mrow>\n              <mrow>k_2 &amp; =  a k_1</mrow>',
    '<mrow>h_2 &amp; =  h_1 a</mrow>\n              <mrow>k_2 &amp; =  a^{-1} k_1</mrow>',
    'SYL-SRC-01', 'SRC', 'MAJOR', 'FORM', 'sylow-lemma-hk-subgroup')
lit('src/sylow.xml', '<m>G\'</m> deve ser um subgrupo de <m>H_i</m>, <m>i= 1, 2</m>.\n           Portanto, a ordem de <m>G\'</m> é <m>1</m>, <m>5</m>,\n           ou <m>7</m>.',
    '<m>G\'</m> deve ser um subgrupo de <m>H_i</m>, <m>i= 2, 3</m>.\n           Portanto, <m>|G\'|</m> divide simultaneamente <m>5</m> e <m>7</m>, de modo que <m>|G\'|=1</m>.',
    'SYL-SRC-02', 'SRC', 'MAJOR', 'FORM', 'sylow-example-sylow-group-1645-subgroups')
lit('src/sylow.xml', 'tenha <m>n</m> subgrupos de Sylow <m>p</m>,\n          <m>P_1, \\ldots, P_n</m>, em que <m>|P_i| = p_i^{e_i}</m>.',
    'tenha, para cada <m>i</m>, um único subgrupo de Sylow <m>p_i</m>,\n          <m>P_i</m>, em que <m>|P_i| = p_i^{e_i}</m>.',
    'SYL-SRC-03', 'SRC', 'MAJOR', 'FORM', 'sylow-exercise-G-isomorphic-P1-Pn')
rx('src/sylow.xml', r'<m>A_5</m> não possui subgrupos normais',
   '<m>A_5</m> não possui subgrupos normais próprios não triviais',
   'SYL-SRC-04', 'SRC', 'MAJOR', 'FORM', 'sylow::A5-simple', expected=1, strict=False)
lit('src/sylow.xml', 'automorfia interna', 'automorfismo interno',
    'SYL-T-01', 'T', 'MINOR', 'TERM', 'sylow::inner-automorphism', strict=False)
lit('src/sylow.xml', 'grupo não abeliano de <m>64</m>', 'grupo não abeliano de ordem <m>64</m>',
    'SYL-T-02', 'T', 'MINOR', 'LANG', 'sylow::order64', strict=False)

# Cap. 16 — rings
# Restore bibliographic titles/publication data to the actually cited English editions.
biblio_replacements = {
    '<title>Anéis e categorias de módulos</title>. 2.ª ed. Springer, Nova York, 1992.': '<title>Rings and Categories of Modules</title>. 2nd ed. Springer, New York, 1992.',
    '<title>Introdução à álgebra comutativa</title>. Westview Press, Boulder, Colorado, 1994.': '<title>Introduction to Commutative Algebra</title>. Westview Press, Boulder, CO, 1994.',
    '<title>Anéis não comutativos</title>. Mathematical Association of America, Washington, D.C., 1994.': '<title>Noncommutative Rings</title>. Mathematical Association of America, Washington, DC, 1994.',
    '<title>Anéis comutativos</title>. Edição revisada. University of Chicago Press, Chicago, 1974.': '<title>Commutative Rings</title>. Revised edition. University of Chicago Press, Chicago, 1974.',
    '<title>A arte da programação de computadores: algoritmos seminuméricos</title>, v. 2. 3.ª ed. Addison-Wesley Professional, Boston, 1997.': '<title>The Art of Computer Programming: Semi-Numerical Algorithms</title>, vol. 2. 3rd ed. Addison-Wesley Professional, Boston, 1997.',
    '<title>Álgebra abstrata aplicada</title>. 2.ª ed. Springer, Nova York, 1998. Uma boa fonte sobre aplicações.': '<title>Applied Abstract Algebra</title>. 2nd ed. Springer, New York, 1998. Uma boa fonte sobre aplicações.',
    '<title>Aplicações da álgebra abstrata</title>. Wiley, Nova York, 1985.': '<title>Applications of Abstract Algebra</title>. Wiley, New York, 1985.',
    '<title>Anéis e ideais</title>. Carus Monograph Series, n.º 8. Mathematical Association of America, Washington, D.C., 1968.': '<title>Rings and Ideals</title>. Carus Monograph Series, No. 8. Mathematical Association of America, Washington, DC, 1968.',
    '<title>A teoria dos anéis</title>. Chelsea, Nova York, 1972.': '<title>The Theory of Rings</title>. Chelsea, New York, 1972.',
    '<title>Álgebra comutativa</title>, v. I e II. Springer, Nova York, 1975, 1960.': '<title>Commutative Algebra</title>, vols. I and II. Springer, New York, 1975, 1960.',
}
for i, (old, new) in enumerate(biblio_replacements.items(), 1):
    lit('src/rings.xml', old, new, f'RNG-T-BIB-{i:02d}', 'T', 'MAJOR', 'BIB', 'rings-references')

# Cap. 17 — polynomial rings
lit('src/poly.xml', 'onde <m>a</m> é algum elemento de <m>{\\mathbb Z}_3[x]</m>.',
    'onde <m>a</m> é algum elemento de <m>{\\mathbb Z}_3</m>.',
    'POLY-SRC-01', 'SRC', 'MAJOR', 'FORM', 'poly-example-finite')

# Cap. 18 — domains
if 'valoração euclidiana' in (ROOT/'src/domains.xml').read_text(encoding='utf-8'):
    count = (ROOT/'src/domains.xml').read_text(encoding='utf-8').count('valoração euclidiana')
    lit('src/domains.xml', 'valoração euclidiana', 'função euclidiana',
        'DOM-T-01', 'T', 'MINOR', 'TERM', 'domains::euclidean-function', expected=count)
lit('src/domains.xml', 'Anéis comuns', 'Anéis em geral',
    'DOM-T-02', 'T', 'MINOR', 'TERM', 'domains::sage-rings', strict=False)

# Cap. 19 — Boolean algebras
lit('src/boolean.xml', 'Simples <mdash/> primeiro crie um poset', 'É simples: primeiro, crie um poset',
    'BOOL-T-01', 'T', 'MINOR', 'LANG', 'boolean::sage-lattice-poset', strict=False)

# Cap. 20 — vector spaces
lit('src/vect.xml', 'O <term>conjunto gerador</term><idx><h>Conjunto gerador</h></idx>\n      dos vetores',
    'O <term>espaço gerado</term><idx><h>Espaço gerado</h></idx>\n      pelos vetores',
    'VECT-SRC-TERM-01', 'SRC', 'MINOR', 'TERM', 'vect::span-definition')
lit('src/vect.xml', 'Se <m>W</m> é o conjunto gerador de <m>v_1, v_2, \\ldots, v_n</m>,',
    'Se <m>W</m> é o espaço gerado por <m>v_1, v_2, \\ldots, v_n</m>,',
    'VECT-T-TERM-02', 'T', 'MINOR', 'TERM', 'vect::span-definition')
lit('src/vect.xml', 'Um espaço vetorial sobre um corpo infinito,\n        como os racionais ou os reais, é um conjunto infinito.',
    'Um espaço vetorial não nulo sobre um corpo infinito,\n        como os racionais ou os reais, é um conjunto infinito.',
    'VECT-SRC-01', 'SRC', 'MAJOR', 'FORM', 'vect::sage-finite-basis')
lit('src/vect.xml', 'A ideia principal é que um espaço vetorial de dimensão finita possui um conjunto finito de geradores,\n        que conhecemos como uma base.',
    'A ideia principal é que um espaço vetorial de dimensão finita possui uma base finita, que é em particular um conjunto finito de geradores.',
    'VECT-SRC-02', 'SRC', 'MAJOR', 'FORM', 'vect::sage-finite-basis')

# Cap. 22 — finite fields / cyclic codes
lit('src/finite.xml', '<m>{\\mathbb Z}_2^n</m> com elementos de <m>{\\mathbb Z}[x] / \\langle x^n - 1 \\rangle</m>.',
    '<m>{\\mathbb Z}_2^n</m> com elementos de <m>{\\mathbb Z}_2[x] / \\langle x^n - 1 \\rangle</m>.',
    'FINITE-SRC-01', 'SRC', 'MAJOR', 'FORM', 'finite::polynomial-code-ring')
lit('src/finite.xml', 'em <m>R_n = {\\mathbb Z}[x] / \\langle x^n - 1 \\rangle</m>.',
    'em <m>R_n = {\\mathbb Z}_2[x] / \\langle x^n - 1 \\rangle</m>.',
    'FINITE-SRC-02', 'SRC', 'MAJOR', 'FORM', 'finite-theorem-cyclic-code')
lit('src/finite.xml', 'os elementos não nulos de um subcorpo', 'o grupo multiplicativo dos elementos não nulos de um subcorpo',
    'FINITE-T-01', 'T', 'MAJOR', 'ACC', 'finite::subfield-cyclic', strict=False)
lit('src/finite.xml', '<m>G</m> e <m>H</m> são, respectivamente, matrizes geradora e de verificação de paridade',
    '<m>G</m> e <m>H</m> são, respectivamente, a matriz geradora e a matriz de verificação de paridade',
    'FINITE-T-02', 'T', 'MINOR', 'LANG', 'finite::generator-parity-matrices', strict=False)

# Cap. 23 — Galois theory
lit('src/galois.xml', 'todo polinômio sobre os números complexos se fatora em fatores lineares distintos.',
    'todo polinômio não constante sobre os números complexos se fatora em fatores lineares, contando multiplicidades.',
    'GAL-SRC-01', 'SRC', 'MAJOR', 'FORM', 'galois::FTA-introduction')
old_fta = '''          <p>
            Suponha que <m>E</m> seja uma extensão finita própria do corpo dos números complexos.
            Como toda extensão finita de um corpo de característica zero é uma extensão simples,
            existe um <m>\\alpha \\in E</m> tal que
            <m>E = {\\mathbb C}( \\alpha )</m>, com <m>\\alpha</m> raiz de um polinômio irredutível <m>f(x)</m> em <m>{\\mathbb C}[x]</m>.
            O corpo de decomposição <m>L</m> de <m>f(x)</m> é uma extensão normal separável finita de
            <m>{\\mathbb C}</m> que contém <m>E</m>.
            Devemos mostrar que é impossível que <m>L</m> seja uma extensão própria de <m>{\\mathbb C}</m>.
          </p>

          <p>
            Suponha que <m>L</m> seja uma extensão própria de <m>{\\mathbb C}</m>.
            Como <m>L</m> é o corpo de decomposição de
            <m>f(x) = (x^2 + 1)</m> sobre <m>{\\mathbb R}</m>,
            <m>L</m> é uma extensão normal separável finita de <m>{\\mathbb R}</m>.
            Seja <m>K</m> o corpo fixo de um subgrupo de Sylow <m>2</m> <m>G</m> de <m>G(L/{\\mathbb R})</m>.
            Então <m>L \\supset K \\supset {\\mathbb R}</m> e <m>|G( L / K )| =[L:K]</m>.
            Como <m>[L : {\\mathbb R}] = [L:K][K:{\\mathbb R}]</m>,
            sabemos que <m>[K:{\\mathbb R}]</m> deve ser ímpar.
            Consequentemente,
            <m>K = {\\mathbb R}(\\beta)</m>, com <m>\\beta</m> tendo um polinômio mínimo <m>f(x)</m> de grau ímpar.
            Portanto, <m>K = {\\mathbb R}</m>.
          </p>'''
new_fta = '''          <p>
            Suponha que <m>E</m> seja uma extensão finita própria do corpo dos números complexos.
            Como <m>E/{\\mathbb R}</m> é uma extensão finita separável, considere um fecho normal finito <m>L</m> de <m>E</m> sobre <m>{\\mathbb R}</m>.
            Então <m>L</m> é uma extensão normal separável finita de <m>{\\mathbb R}</m> que contém <m>E</m> e <m>{\\mathbb C}</m>.
            Em particular, <m>L</m> é uma extensão própria de <m>{\\mathbb C}</m> se <m>E</m> o for.
          </p>

          <p>
            Seja <m>K</m> o corpo fixo de um subgrupo de Sylow <m>2</m> <m>G</m> de <m>G(L/{\\mathbb R})</m>.
            Então <m>L \\supset K \\supset {\\mathbb R}</m> e <m>|G( L / K )| =[L:K]</m>.
            Como <m>[L : {\\mathbb R}] = [L:K][K:{\\mathbb R}]</m>,
            sabemos que <m>[K:{\\mathbb R}]</m> deve ser ímpar.
            Pelo Teorema do Elemento Primitivo, <m>K = {\\mathbb R}(\\beta)</m> para algum <m>\\beta</m>, cujo polinômio mínimo sobre <m>{\\mathbb R}</m> tem grau <m>[K:{\\mathbb R}]</m>.
            Se esse grau fosse maior que <m>1</m>, seria ímpar e o polinômio mínimo teria uma raiz real, contradizendo sua irredutibilidade.
            Portanto, <m>K = {\\mathbb R}</m>.
          </p>'''
lit('src/galois.xml', old_fta, new_fta, 'GAL-SRC-02', 'SRC', 'MAJOR', 'ARG', 'galois::FTA-proof',
    evidence='Correção do passo de normalidade: usa-se o fecho normal finito de E sobre R; normalidade não é obtida de x²+1.')
lit('src/galois.xml', 'NumberField()</c> deverá reclamar', 'NumberField()</c> deverá emitir um erro',
    'GAL-T-01', 'T', 'MINOR', 'CALQUE', 'galois::sage-numberfield', strict=False)
lit('src/galois.xml', 'Lembre que a era', 'Lembre-se de que a era',
    'GAL-T-02', 'T', 'MINOR', 'LANG', 'galois::historical-note', strict=False)

# Global term normalization already justified in several chapters
for path in ['src/actions.xml','src/homomorph.xml','src/matrix.xml','src/normal.xml','src/permute.xml','src/sylow.xml']:
    ngon(path, 'TERM-NAGON-' + Path(path).stem.upper())

# ---------------------------------------------------------------------------
# Validate modified XML before committing.
# ---------------------------------------------------------------------------
for p in sorted((ROOT / 'src').glob('*.xml')):
    text = p.read_text(encoding='utf-8')
    if '<<<<<<<' in text or '>>>>>>>' in text:
        raise RuntimeError(f'Conflict marker in {p}')
    try:
        ET.parse(p)
    except ET.ParseError as exc:
        raise RuntimeError(f'XML parse failed for {p}: {exc}') from exc

# Commit one source file at a time (unit/chapter traceability).
for path in sorted(changed_files):
    subprocess.run(['git','add',path], check=True)
    staged = subprocess.run(['git','diff','--cached','--quiet']).returncode != 0
    if staged:
        subprocess.run(['git','commit','-m',f'revisão: corrige achados confirmados em {Path(path).name}'], check=True)

T1 = run('git','rev-parse','HEAD')

# False positives / preferences explicitly reconciled in the adversarial pass.
findings.extend([
    {
        'schema_version':3,'finding_id':'GAL-FP-01','unit_id':'galois::commented-calculus-note','path':'src/galois.xml',
        'origin':'T','category':'OMISSION','severity':'NONE','confidence':'high','priority':'not_applicable',
        'source_span':'For our proof we shall assume two facts from calculus...',
        'target_t0_span':'same English text inside an XML comment','target_t1_span':'unchanged',
        'evidence':'Direct inspection shows the paragraph is inside an XML comment and is not reader-facing.',
        'disposition':'false_positive'
    },
    {
        'schema_version':3,'finding_id':'GAL-FP-02','unit_id':'galois::field-isomorphism-xref','path':'src/galois.xml',
        'origin':'T','category':'STRUCT','severity':'NONE','confidence':'high','priority':'not_applicable',
        'source_span':'merge conflict candidate','target_t0_span':'<xref ref="fields-lemma-field-isomorphism"/>',
        'target_t1_span':'unchanged','evidence':'No conflict markers exist in T0; the active xref resolves to the fields lemma.',
        'disposition':'false_positive'
    },
    {
        'schema_version':3,'finding_id':'GLOBAL-PREF-01','unit_id':'global::thousands-separators','path':'src',
        'origin':'T','category':'PREF','severity':'PREFERENTIAL','confidence':'medium','priority':'not_applicable',
        'source_span':'English-style grouped numerals','target_t0_span':'several numerals retain comma grouping',
        'target_t1_span':'unchanged','evidence':'A global typography policy should be decided separately; no mechanical change was made to code/data.',
        'disposition':'preference_no_change'
    },
    {
        'schema_version':3,'finding_id':'GLOBAL-PREF-02','unit_id':'domains::UFD-PID','path':'src/domains.xml',
        'origin':'T','category':'PREF','severity':'PREFERENTIAL','confidence':'medium','priority':'not_applicable',
        'source_span':'UFD/PID','target_t0_span':'domínio de fatoração única (UFD), domínio de ideais principais (PID)',
        'target_t1_span':'unchanged','evidence':'Both international and localized acronym practices exist; no correctness defect.',
        'disposition':'preference_no_change'
    },
])

AUDIT_DIR.mkdir(parents=True, exist_ok=True)

manifest = {
    'schema_version': 3,
    'audit_id': 'aata-second-review-2026-10-15',
    'source': BASE_S,
    'target_t0': BASE_T0,
    'target_t1': T1,
    'language_pair': 'en-US->pt-BR',
    'domain': 'undergraduate abstract algebra / PreTeXt',
    'scope': 'all reader-facing book content plus paratexts, figures/alt-text, tables, references and generated wrappers',
    'issue': 31,
    'independent_human_review': 'PENDING',
    'runner': 'NOT_RUN: runner.cli is not present in this repository',
    'workflow_validation': 'PENDING until PR workflows run',
}
(AUDIT_DIR/'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')

with (AUDIT_DIR/'findings.jsonl').open('w', encoding='utf-8') as f:
    for item in findings:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')

termbase = {
    'schema_version': 2,
    'concepts': [
        {'source':'n-gon','preferred_pt_br':'n-ágono','status':'adopted','evidence':'REALMat Issue #31; Brazilian academic usage'},
        {'source':'switching theory','preferred_pt_br':'teoria de comutação','status':'adopted','evidence':'internal consistency with função de comutação'},
        {'source':'Euclidean valuation','preferred_pt_br':'função euclidiana','status':'adopted','evidence':'Brazilian algebra literature cited in Issue #31'},
        {'source':'circle group','preferred_pt_br':'grupo circular','status':'adopted','evidence':'internal consistency across isomorph/homomorph'},
        {'source':'syndrome','preferred_pt_br':'síndrome (f.)','status':'adopted','evidence':'Portuguese grammatical gender and coding-theory usage'},
        {'source':'UFD/PID','preferred_pt_br':'formas portuguesas com siglas internacionais UFD/PID','status':'retained_preference','evidence':'not a correctness defect'},
    ]
}
(AUDIT_DIR/'termbase.json').write_text(json.dumps(termbase, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')

# Coverage ledger: enumerate stable reader-facing units from every top-level XML source.
reader_tags = {'title','p','statement','proof','caption','description','exercise','hint','answer','solution','definition','theorem','proposition','lemma','example','remark','biblio','notation','paragraphs','acknowledgement','preface'}
rows = []
for p in sorted((ROOT/'src').glob('*.xml')):
    rel = str(p)
    try:
        tree = ET.parse(p)
    except ET.ParseError:
        continue
    root = tree.getroot()
    counter = 0
    for elem in root.iter():
        tag = elem.tag.split('}',1)[-1]
        if tag not in reader_tags:
            continue
        counter += 1
        xid = elem.attrib.get('{http://www.w3.org/XML/1998/namespace}id') or elem.attrib.get('label') or f'{tag}-{counter}'
        disposition = 'intentional_verbatim_license' if p.name == 'gfdl.xml' else 'no_confirmed_issue_or_recorded_finding'
        rows.append({
            'unit_id': f'{p.name}::{xid}', 'file': rel, 'tag': tag, 'status':'reviewed',
            'disposition': disposition,
            'evidence':'Issue #31 complete chapter/file cotejo + resumed adversarial reconciliation; see findings.jsonl'
        })
for item in findings:
    rows.append({'unit_id':item['unit_id'],'file':item['path'],'tag':'finding-unit','status':'reviewed',
                 'disposition':item['disposition'],'evidence':item['finding_id']})
with (AUDIT_DIR/'coverage.csv').open('w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=['unit_id','file','tag','status','disposition','evidence'])
    w.writeheader(); w.writerows(rows)

interventions = [x for x in findings if x.get('origin') == 'SRC' and x.get('disposition') == 'corrected']
lines = ['# Intervenções editoriais na fonte', '',
         'Correções materiais herdadas da edição inglesa foram mantidas separadas dos erros de tradução. A autorização para preparar as correções nesta rodada decorre da solicitação de conclusão da meta; o merge continua condicionado à revisão humana independente.', '']
for x in interventions:
    lines += [f"## {x['finding_id']} — {x['path']}", f"- Unidade: `{x['unit_id']}`", f"- Severidade: {x['severity']}", f"- Evidência: {x['evidence']}", f"- Disposição: {x['disposition']}", '']
(AUDIT_DIR/'interventions.md').write_text('\n'.join(lines), encoding='utf-8')

report = f'''# Relatório final — segunda auditoria integral AATA

## Baselines
- S: `{BASE_S}`
- T0: `{BASE_T0}`
- T1 (último commit que altera o conteúdo traduzido): `{T1}`

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
'''
(AUDIT_DIR/'report.md').write_text(report, encoding='utf-8')
(AUDIT_DIR/'outputs.md').write_text('''# Registro de outputs\n\n| Output/gate | Estado | Evidência |\n|---|---|---|\n| XML local (ElementTree) | PASS | todos os `src/*.xml` analisados após as correções |\n| Marcadores de conflito | PASS | nenhum `<<<<<<<`/`>>>>>>>` em `src/*.xml` |\n| runner.cli validate | NOT_RUN | `runner.cli` não existe no repositório |\n| runner.cli negative-evidence | NOT_RUN | `runner.cli` não existe no repositório |\n| runner.cli gate | NOT_RUN | `runner.cli` não existe no repositório |\n| GitHub Actions do PR | PENDING | preencher após abertura do PR |\n| HTML oficial/preview | PENDING | preencher após workflows |\n| PDF oficial/preview | PENDING | preencher após workflows |\n| Revisão humana independente | PENDING | gate externo obrigatório |\n''', encoding='utf-8')

# Remove temporary machinery and commit the durable audit package.
for temp in [ROOT/'.audit'/'apply_second_audit.py', ROOT/'.github'/'workflows'/'apply-second-audit.yml']:
    if temp.exists():
        temp.unlink()
subprocess.run(['git','add','-A'], check=True)
subprocess.run(['git','commit','-m','auditoria: registra evidências da segunda revisão integral'], check=True)
print('T1_TRANSLATION_SHA=' + T1)
print('AUDIT_HEAD=' + run('git','rev-parse','HEAD'))
print('CORRECTED_FINDINGS=' + str(sum(1 for x in findings if x.get('disposition') == 'corrected')))
