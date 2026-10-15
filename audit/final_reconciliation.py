from __future__ import annotations

from pathlib import Path
import json, re, subprocess, xml.etree.ElementTree as ET

ROOT = Path('.')
AUD = ROOT / 'audit' / 'second-review-2026-10-15'
changed: set[str] = set()
new_findings: list[dict] = []


def replace(path: str, old: str, new: str, fid: str, origin='T', severity='MINOR', category='LANG', unit=None, count=None):
    p = ROOT / path
    s = p.read_text(encoding='utf-8')
    n = s.count(old)
    if count is not None and n != count:
        raise RuntimeError(f'{fid}: expected {count}, found {n} in {path}')
    if n == 0:
        raise RuntimeError(f'{fid}: pattern not found in {path}: {old[:100]}')
    p.write_text(s.replace(old, new), encoding='utf-8')
    changed.add(path)
    new_findings.append({
        'schema_version':3,'finding_id':fid,'unit_id':unit or f'{path}::{fid}','path':path,
        'origin':origin,'category':category,'severity':severity,'confidence':'high',
        'priority':'P1' if severity=='MAJOR' else 'P2','source_span':old[:1200],
        'target_t0_span':old[:1200],'target_t1_span':new[:1200],
        'evidence':'Reconciliação final da Issue #31 com inspeção direta do contexto ativo.',
        'disposition':'corrected_final_reconciliation'
    })


def sub(path: str, pattern: str, repl: str, fid: str, origin='T', severity='MINOR', category='LANG', unit=None, count=1):
    p = ROOT / path
    s = p.read_text(encoding='utf-8')
    ns, n = re.subn(pattern, repl, s, count=count, flags=re.S)
    if n != count:
        raise RuntimeError(f'{fid}: expected {count}, found {n} regex matches in {path}')
    p.write_text(ns, encoding='utf-8')
    changed.add(path)
    new_findings.append({
        'schema_version':3,'finding_id':fid,'unit_id':unit or f'{path}::{fid}','path':path,
        'origin':origin,'category':category,'severity':severity,'confidence':'high',
        'priority':'P1' if severity=='MAJOR' else 'P2','source_span':pattern[:1200],
        'target_t0_span':pattern[:1200],'target_t1_span':repl[:1200],
        'evidence':'Reconciliação final da Issue #31 com inspeção direta do contexto ativo.',
        'disposition':'corrected_final_reconciliation'
    })

# Achados que a aplicação inicial não encontrou por pequenas diferenças de marcação/redação.
replace('src/sets.xml',
        '<term>injetiva</term><idx><h>Função</h><h>injetiva</h></idx> ou\n        <term>injetiva</term><idx><h>Função</h><h>injetiva</h></idx>',
        '<term>injetora</term><idx><h>Função</h><h>injetora</h></idx> ou\n        <term>injetiva</term><idx><h>Função</h><h>injetiva</h></idx>',
        'SETS-T-01-FINAL', unit='sets::injective-definition')
replace('src/groups.xml',
        'Um dos primeiros tratamentos modernos da teoria dos grupos apareceu em\n        William Burnside',
        'Um dos primeiros tratamentos modernos da teoria dos grupos apareceu na obra de\n        William Burnside',
        'GRP-T-02-FINAL', unit='groups::historical-burnside')
replace('src/permute.xml','Encontre o grupo de movimentos rígidos de um tetraedro.','Encontre o grupo de rotações de um tetraedro.',
        'PERM-SRC-02A-FINAL',origin='SRC',severity='MAJOR',category='ACC',unit='permute-exercise-rigid-motions-tetrahedron')
replace('src/permute.xml','Construa o grupo de simetrias do tetraedro\n          (que também é o grupo alternado sobre 4 símbolos, <m>A_4</m>)',
        'Construa o grupo de simetrias rotacionais do tetraedro\n          (que também é o grupo alternado sobre 4 símbolos, <m>A_4</m>)',
        'PERM-SRC-02B-FINAL',origin='SRC',severity='MAJOR',category='ACC',unit='permute-sage-exercise-create-A4')
replace('src/isomorph.xml','Como <q>ser isomorfo a</q> é uma relação de equivalência pelo',
        'Como a relação <q>ser isomorfo a</q> é uma relação de equivalência pelo',
        'ISO-T-03A-FINAL',unit='isomorph-sage::is-isomorphic')
replace('src/isomorph.xml','Observe que, como <q>ser isomorfo a</q>\n        é uma relação de equivalência,',
        'Observe que, como a relação <q>ser isomorfo a</q>\n        é uma relação de equivalência,',
        'ISO-T-03B-FINAL',unit='isomorph-sage::finite-groups')
replace('src/isomorph.xml','Para as ordens primas <m>1,2,3,5,7,11</m> e <m>13</m>',
        'Para a ordem <m>1</m> e para as ordens primas <m>2,3,5,7,11</m> e <m>13</m>',
        'ISO-SRC-01-FINAL',origin='SRC',severity='MAJOR',category='ACC',unit='isomorph-sage::finite-groups')
replace('src/isomorph.xml','expresso univocamente como <m>z^m y^n</m> para alguns inteiros não negativos <m>m, n</m>.',
        'expresso univocamente como <m>z^m y^n</m>, com <m>0 \\leq m \\lt p</m> e <m>0 \\leq n \\lt 2</m>.',
        'ISO-SRC-02-FINAL',origin='SRC',severity='MAJOR',category='FORM',unit='isomorph::order-2p-exercise')
replace('src/matrix.xml','para <m>{\\mathbb R}^6</m> e além','para <m>{\\mathbb R}^6</m> e dimensões superiores',
        'MATRIX-T-02-FINAL',category='CALQUE',unit='matrix::crystallographic-groups')
replace('src/matrix.xml','As formas possíveis das células são paralelogramo,\n        retangular, quadrada, rômbica,\n        e hexagonal',
        'As formas possíveis das células são paralelogramo,\n        retângulo, quadrado, losango\n        e hexágono',
        'MATRIX-T-03-FINAL',unit='matrix::lattice-types')
sub('src/struct.xml',r'Sejam (<m>G</m>, <m>H</m> e <m>K</m>)\s+sejam grupos abelianos finitamente gerados\.',
    r'Sejam \1 grupos abelianos finitamente gerados.', 'STRUCT-T-01-FINAL', unit='struct-exercise-finitely-generated-abelian-group:statement')
replace('src/actions.xml','Seja <m>|G| = p^n</m> um grupo não abeliano, com <m>p</m> primo.',
        'Seja <m>G</m> um grupo não abeliano de ordem <m>p^n</m>, com <m>p</m> primo.',
        'ACT-SRC-04-FINAL',origin='SRC',severity='MINOR',category='FORM',unit='actions-exercise-ZG')
replace('src/actions.xml','Se você não vir o singleton <c>[4]</c> em sua saída,',
        'Se você não vir a lista com um único elemento, <c>[4]</c>, em sua saída,',
        'ACT-T-03-FINAL',category='CALQUE',unit='actions:sage-stabilizer-note')
sub('src/domains.xml',r'\bAnéis comuns\b', 'Anéis em geral', 'DOM-T-02-FINAL',category='TERM',unit='domains::sage-rings')
replace('src/galois.xml','Lembre que a era', 'Lembre-se de que a era', 'GAL-T-02-FINAL',unit='galois::historical-note')

# Erros matemáticos/factuais adicionais confirmados no fechamento da segunda passagem.
replace('src/finite.xml','a_{i_1} (\\omega^{r + 1})^{i_2}', 'a_{i_1} (\\omega^{r + 1})^{i_1}',
        'FINITE-SRC-03-FINAL',origin='SRC',severity='MAJOR',category='FORM',unit='finite::BCH-Vandermonde')
replace('src/finite.xml','x_{n - 1}', 'x_{s - 1}',
        'FINITE-SRC-04-FINAL',origin='SRC',severity='MAJOR',category='FORM',unit='finite::BCH-Vandermonde',count=3)
replace('src/finite.xml','<m>1 \\leq i \\leq d</m>', '<m>1 \\leq i \\lt d</m>',
        'FINITE-SRC-05-FINAL',origin='SRC',severity='MAJOR',category='FORM',unit='finite::BCH-characterization')
replace('src/galois.xml','pois <m>\\omega</m> é um gerador do grupo de Galois.',
        'pois <m>\\sigma_2</m> é um gerador do grupo de Galois.',
        'GAL-SRC-03-FINAL',origin='SRC',severity='MAJOR',category='FORM',unit='galois-example-group-x4')
replace('src/galois.xml','pois <m>\\omega \\neq 1</m> ou 0.',
        'pois <m>\\omega \\neq 1</m> e <m>\\omega \\neq 0</m>.',
        'GAL-SRC-04-FINAL',origin='SRC',severity='MAJOR',category='FORM',unit='galois::cyclotomic-polynomial')
replace('src/galois.xml','+ c_{p - 2} (\\omega^i)^{p - 2}', '+ a_{p - 2} (\\omega^i)^{p - 2}',
        'GAL-SRC-05-FINAL',origin='SRC',severity='MAJOR',category='FORM',unit='galois::phi-i-map')

# Correções linguísticas confirmadas em fields.xml.
replace('src/fields.xml',"prova de Gerd Faltings'",'prova de Gerd Faltings','FIELDS-T-01-FINAL',unit='fields::historical-note')
replace('src/fields.xml','é um corpo de decomposição de <m>F</m> para algum polinômio <m>f(x) \\in F[x]</m>.',
        'é um corpo de decomposição, sobre <m>F</m>, de algum polinômio <m>f(x) \\in F[x]</m>.',
        'FIELDS-T-02-FINAL',category='ACC',unit='fields-exercise-extension-degree-2')
replace('src/fields.xml','corpo inteiro dos números algébricos','corpo formado por todos os números algébricos',
        'FIELDS-T-03-FINAL',category='CALQUE',unit='fields::sage-algebraic-field')
replace('src/fields.xml','anel de polinômios inteiro','todo o anel de polinômios',
        'FIELDS-T-04-FINAL',category='CALQUE',unit='fields::sage-polynomial-ring')
replace('src/fields.xml','Qual é a extensão menor que contém todas as raízes?',
        'Qual é a menor extensão que contém todas as raízes?',
        'FIELDS-T-05-FINAL',unit='fields::splitting-field-question')
# Padronização ortográfica comprovada no próprio capítulo.
pf = ROOT/'src/fields.xml'
s = pf.read_text(encoding='utf-8')
if 'trisectar' in s:
    n=s.count('trisectar'); pf.write_text(s.replace('trisectar','trissectar'),encoding='utf-8'); changed.add('src/fields.xml')
    new_findings.append({'schema_version':3,'finding_id':'FIELDS-T-06-FINAL','unit_id':'fields::trisect','path':'src/fields.xml','origin':'T','category':'TERM','severity':'MINOR','confidence':'high','priority':'P2','source_span':'trisectar','target_t0_span':'trisectar','target_t1_span':'trissectar','evidence':f'{n} ocorrência(s), consistência interna e uso acadêmico brasileiro documentado na Issue #31.','disposition':'corrected_final_reconciliation'})

# Criptografia: naturalidade e terminologia técnica confirmadas.
replace('src/crypt.xml','convertemos para ASCII algarismos','convertemos as letras em valores ASCII','CRYPT-T-03-FINAL',category='CALQUE',unit='crypt::ascii-conversion')
replace('src/crypt.xml','mantendo <m>D</m> muito privado e seguro','mantendo <m>D</m> em sigilo e protegido','CRYPT-T-04-FINAL',category='CALQUE',unit='crypt::private-key')

# Integridade XML.
for p in sorted((ROOT/'src').glob('*.xml')):
    ET.parse(p)

# Commit de conteúdo.
subprocess.run(['git','add',*sorted(changed)],check=True)
subprocess.run(['git','commit','-m','revisão: reconcilia achados finais da auditoria'],check=True)
content_sha = subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()

# Atualizar ledger/artefatos, reclassificando todos os pattern mismatches da primeira aplicação.
fp = AUD/'findings.jsonl'
items=[]
for line in fp.read_text(encoding='utf-8').splitlines():
    if not line.strip(): continue
    x=json.loads(line)
    if x.get('disposition')=='not_applied_pattern_mismatch':
        x['disposition']='superseded_by_final_reconciliation'
        x['priority']='not_applicable'
        x['confidence']='medium'
        x['evidence'] += ' O trecho foi reinspecionado na reconciliação final; quando a correção permanecia necessária, foi registrada em um finding FINAL separado.'
    items.append(x)
items.extend(new_findings)
fp.write_text('\n'.join(json.dumps(x,ensure_ascii=False) for x in items)+'\n',encoding='utf-8')

manifest=json.loads((AUD/'manifest.json').read_text(encoding='utf-8'))
manifest['target_t1']=content_sha
manifest['final_reconciliation']='completed'
manifest['independent_human_review']='PENDING'
(AUD/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

report=(AUD/'report.md').read_text(encoding='utf-8')
report=re.sub(r'T1 \(último commit que altera o conteúdo traduzido\): `[^`]+`',f'T1 (último commit que altera o conteúdo traduzido): `{content_sha}`',report)
report += '\n## Reconciliação final\nOs casos em que a aplicação inicial não encontrou o padrão literal foram reinspecionados. As correções ainda pertinentes foram aplicadas em uma passagem final, incluindo índices BCH, afirmações em teoria de Galois, limites de expoentes e correções linguísticas de `fields.xml`. Os registros antigos de mismatch foram marcados como superseded e os achados finais foram adicionados ao ledger.\n'
(AUD/'report.md').write_text(report,encoding='utf-8')

outputs=(AUD/'outputs.md').read_text(encoding='utf-8')
outputs=outputs.replace('| XML local (ElementTree) | PASS | todos os `src/*.xml` analisados após as correções |','| XML local (ElementTree) | PASS | todos os `src/*.xml` analisados após a reconciliação final |')
(AUD/'outputs.md').write_text(outputs,encoding='utf-8')

# Remover a infraestrutura temporária desta passagem antes do commit de evidências.
for tmp in [ROOT/'audit'/'final_reconciliation.py', ROOT/'.github'/'workflows'/'final-reconciliation.yml']:
    if tmp.exists(): tmp.unlink()
subprocess.run(['git','add','-A'],check=True)
subprocess.run(['git','commit','-m','auditoria: fecha reconciliação e atualiza evidências'],check=True)
print('CONTENT_SHA='+content_sha)
print('HEAD='+subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip())
