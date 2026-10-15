from pathlib import Path
import json
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]


def replace_exact(path, old, new, expected=1):
    p = ROOT / path
    text = p.read_text(encoding="utf-8")
    count = text.count(old)
    if count != expected:
        raise SystemExit(f"{path}: esperado {expected} ocorrência(s), encontrado {count}: {old!r}")
    p.write_text(text.replace(old, new), encoding="utf-8")
    print(f"{path}: {count} substituição(ões)")


def replace_all(path, old, new, minimum=1):
    p = ROOT / path
    text = p.read_text(encoding="utf-8")
    count = text.count(old)
    if count < minimum:
        raise SystemExit(f"{path}: esperado pelo menos {minimum} ocorrência(s), encontrado {count}: {old!r}")
    p.write_text(text.replace(old, new), encoding="utf-8")
    print(f"{path}: {count} substituição(ões) globais")


# 1–3. fields.xml: forma lexical correta e duas regressões gramaticais.
replace_all("src/fields.xml", "trissectar", "trissecar")
replace_exact(
    "src/fields.xml",
    "Em vez de construir o todo o anel de polinômios,",
    "Em vez de construir todo o anel de polinômios,",
)
replace_exact(
    "src/fields.xml",
    "construímos um todo o anel de polinômios <c>R</c> sobre <c>N</c>, com a indeterminada <c>z</c>.",
    "construímos todo o anel de polinômios <c>R</c> sobre <c>N</c>, com a indeterminada <c>z</c>.",
)

# 4. crypt.xml: recíproco natural em português.
replace_exact(
    "src/crypt.xml",
    "escolha um colega de estudos e envie mensagens um ao outro da mesma maneira.",
    "escolha um colega de estudos e troque mensagens com essa pessoa da mesma maneira.",
)

# 5. domains.xml: índice coerente com a terminologia adotada no texto.
replace_exact(
    "src/domains.xml",
    "<idx><h>Valoração euclidiana</h></idx><term>função euclidiana</term>",
    "<idx><h>Função euclidiana</h></idx><term>função euclidiana</term>",
)

# 6. groups.xml: singularidade dos dois subgrupos canônicos.
replace_exact(
    "src/groups.xml",
    "existem outros subgrupos além dos subgrupos triviais e impróprios.",
    "existem outros subgrupos além do subgrupo trivial e do subgrupo impróprio.",
)

# 7. isomorph.xml: uma bijeção é entre elementos e deve preservar a operação.
replace_exact(
    "src/isomorph.xml",
    "<m>{\\mathbb Z}_4</m> e o subgrupo do grupo circular\n      <m>{\\mathbb T}</m> gerado por <m>i</m> podemos mostrar que são isomorfos exibindo uma correspondência bijetiva entre os elementos dos dois grupos e entre as operações de grupo.",
    "<m>{\\mathbb Z}_4</m> e o subgrupo do grupo circular\n      <m>{\\mathbb T}</m> gerado por <m>i</m> são isomorfos, como se vê por uma correspondência bijetiva entre seus elementos que preserva as operações de grupo.",
)

# 8. matrix.xml: regência/naturalidade.
replace_exact(
    "src/matrix.xml",
    "o caso pelo qual estamos mais interessados.",
    "o caso que mais nos interessa.",
)

# 9a. galois.xml: distinção das potências decorre da ordem p de omega.
replace_exact(
    "src/galois.xml",
    "Claramente <m>\\omega, \\omega^2, \\ldots, \\omega^{p - 1}</m> são distintos, pois <m>\\omega \\neq 1</m> e <m>\\omega \\neq 0</m>.",
    "Como <m>\\omega</m> é uma raiz <m>p</m>-ésima primitiva da unidade, sua ordem multiplicativa é <m>p</m>; portanto, <m>\\omega, \\omega^2, \\ldots, \\omega^{p - 1}</m> são distintos.",
)

# 9b. galois.xml: phi_2 não gera o grupo para todo primo p.
replace_exact(
    "src/galois.xml",
    "Mostre que <m>\\phi_2</m> gera <m>G({\\mathbb Q}(\\omega)/{\\mathbb Q})</m>.",
    "Mostre que <m>\\phi_i \\circ \\phi_j = \\phi_k</m>, em que <m>k \\equiv ij \\pmod p</m>, e conclua que <m>G({\\mathbb Q}(\\omega)/{\\mathbb Q}) \\cong U_p</m>; em particular, esse grupo é abeliano de ordem <m>p-1</m>.",
)

# Registra os nove achados da varredura no ledger estruturado do PR.
findings_path = ROOT / "audit/second-review-2026-10-15/findings.jsonl"
existing = findings_path.read_text(encoding="utf-8")
new_findings = [
    {
        "schema_version": 3, "finding_id": "XCHK-GAL-01", "unit_id": "galois::cyclotomic-hint-distinct-powers",
        "path": "src/galois.xml", "origin": "SRC", "category": "FORM", "severity": "MAJOR", "confidence": "high", "priority": "P1",
        "source_span": "omega, omega^2, ..., omega^(p-1) are distinct since omega != 1 or 0",
        "target_t0_span": "omega != 1 e omega != 0", "target_t1_span": "omega tem ordem multiplicativa p; portanto as potências são distintas",
        "evidence": "A distinção decorre de ord(omega)=p, não apenas de omega ser diferente de 0 e 1.", "disposition": "corrected"
    },
    {
        "schema_version": 3, "finding_id": "XCHK-FLD-01", "unit_id": "fields::angle-trisection-terminology",
        "path": "src/fields.xml", "origin": "T", "category": "LANG", "severity": "MINOR", "confidence": "high", "priority": "P2",
        "source_span": "trisect", "target_t0_span": "trissectar", "target_t1_span": "trissecar",
        "evidence": "Forma portuguesa dicionarizada: trissecar.", "disposition": "corrected"
    },
    {
        "schema_version": 3, "finding_id": "XCHK-FLD-02", "unit_id": "fields::whole-entire-polynomial-ring",
        "path": "src/fields.xml", "origin": "T", "category": "LANG", "severity": "MINOR", "confidence": "high", "priority": "P2",
        "source_span": "the whole polynomial ring / an entire polynomial ring", "target_t0_span": "o todo o / um todo o anel", "target_t1_span": "todo o anel de polinômios",
        "evidence": "Duas regressões gramaticais introduzidas no PR #32.", "disposition": "corrected"
    },
    {
        "schema_version": 3, "finding_id": "XCHK-CRYPT-01", "unit_id": "crypt::study-buddy-reciprocal",
        "path": "src/crypt.xml", "origin": "T", "category": "LANG", "severity": "MINOR", "confidence": "high", "priority": "P2",
        "source_span": "grab a study buddy and send each other messages", "target_t0_span": "envie mensagens um ao outro", "target_t1_span": "troque mensagens com essa pessoa",
        "evidence": "A construção anterior combinava sujeito singular com expressão recíproca plural.", "disposition": "corrected"
    },
    {
        "schema_version": 3, "finding_id": "XCHK-DOM-01", "unit_id": "domains::euclidean-function-index",
        "path": "src/domains.xml", "origin": "T", "category": "TERM", "severity": "MINOR", "confidence": "high", "priority": "P2",
        "source_span": "Euclidean valuation", "target_t0_span": "índice: Valoração euclidiana / termo: função euclidiana", "target_t1_span": "índice e termo: Função euclidiana",
        "evidence": "O índice deve acompanhar a terminologia adotada no texto traduzido.", "disposition": "corrected"
    },
    {
        "schema_version": 3, "finding_id": "XCHK-GRP-01", "unit_id": "groups::trivial-improper-subgroups",
        "path": "src/groups.xml", "origin": "T", "category": "LANG", "severity": "MINOR", "confidence": "high", "priority": "P2",
        "source_span": "the trivial and improper subgroups", "target_t0_span": "subgrupos triviais e impróprios", "target_t1_span": "do subgrupo trivial e do subgrupo impróprio",
        "evidence": "O contexto se refere aos dois subgrupos canônicos específicos.", "disposition": "corrected"
    },
    {
        "schema_version": 3, "finding_id": "XCHK-ISO-01", "unit_id": "isomorph::intro-operation-preservation",
        "path": "src/isomorph.xml", "origin": "T", "category": "ACC", "severity": "MINOR", "confidence": "high", "priority": "P2",
        "source_span": "one-to-one correspondence between the elements ... and between the group operations", "target_t0_span": "correspondência bijetiva ... entre as operações", "target_t1_span": "correspondência bijetiva entre elementos que preserva as operações",
        "evidence": "Isomorfismo é uma bijeção entre conjuntos subjacentes compatível com as operações.", "disposition": "corrected"
    },
    {
        "schema_version": 3, "finding_id": "XCHK-MAT-01", "unit_id": "matrix::linear-algebra-regency",
        "path": "src/matrix.xml", "origin": "T", "category": "LANG", "severity": "MINOR", "confidence": "high", "priority": "P2",
        "source_span": "the case with which we are most concerned", "target_t0_span": "o caso pelo qual estamos mais interessados", "target_t1_span": "o caso que mais nos interessa",
        "evidence": "Correção de regência e naturalidade sem alteração de sentido.", "disposition": "corrected"
    },
    {
        "schema_version": 3, "finding_id": "XCHK-GAL-02", "unit_id": "galois::cyclotomic-hint-phi2-generator",
        "path": "src/galois.xml", "origin": "SRC", "category": "FORM", "severity": "MAJOR", "confidence": "high", "priority": "P1",
        "source_span": "Show that phi_2 generates G(Q(omega)/Q)", "target_t0_span": "Mostre que phi_2 gera G(Q(omega)/Q)", "target_t1_span": "phi_i o phi_j = phi_k, k == ij mod p; G ~= U_p",
        "evidence": "phi_2 não gera o grupo para todo primo; p=7 fornece contraexemplo, pois ord_7(2)=3 enquanto |G|=6.", "disposition": "corrected"
    },
]
with findings_path.open("a", encoding="utf-8") as fh:
    for finding in new_findings:
        if f'"finding_id": "{finding["finding_id"]}"' not in existing:
            fh.write(json.dumps(finding, ensure_ascii=False) + "\n")

# Registra o fechamento textual no relatório/intervenções.
report = ROOT / "audit/second-review-2026-10-15/report.md"
report_text = report.read_text(encoding="utf-8")
marker = "## Varredura cruzada final do PR #32"
if marker not in report_text:
    report.write_text(
        report_text.rstrip() + "\n\n" + marker + "\n\n"
        "Uma nova comparação hunk a hunk das alterações do PR #32 com o baseline inglês identificou nove pendências editoriais/semânticas. "
        "Todas foram corrigidas nesta rodada: terminologia e gramática em `fields.xml`, `crypt.xml`, `domains.xml`, `groups.xml`, `isomorph.xml` e `matrix.xml`, "
        "além de duas correções matemáticas em `galois.xml` relativas às potências de uma raiz ciclotômica e à falsa afirmação de que `phi_2` gera o grupo de Galois para todo primo.\n",
        encoding="utf-8",
    )

interventions = ROOT / "audit/second-review-2026-10-15/interventions.md"
inter_text = interventions.read_text(encoding="utf-8")
marker2 = "## Adendo — varredura cruzada final"
if marker2 not in inter_text:
    interventions.write_text(
        inter_text.rstrip() + "\n\n" + marker2 + "\n\n"
        "- `galois.xml`: a distinção de `omega, omega^2, ..., omega^(p-1)` foi justificada corretamente pela ordem multiplicativa `p` de `omega`.\n"
        "- `galois.xml`: a instrução herdada da fonte para provar que `phi_2` gera todo o grupo foi substituída pela lei de composição `phi_i o phi_j = phi_k` (`k ≡ ij mod p`) e pela identificação com `U_p`. A afirmação anterior falha, por exemplo, para `p=7`.\n",
        encoding="utf-8",
    )

# Verificações pós-correção.
checks = {
    "src/fields.xml": ["trissectar", "o todo o anel de polinômios", "um todo o anel de polinômios"],
    "src/crypt.xml": ["envie mensagens um ao outro"],
    "src/domains.xml": ["<idx><h>Valoração euclidiana</h></idx><term>função euclidiana</term>"],
    "src/groups.xml": ["além dos subgrupos triviais e impróprios"],
    "src/isomorph.xml": ["entre os elementos dos dois grupos e entre as operações de grupo"],
    "src/matrix.xml": ["o caso pelo qual estamos mais interessados"],
    "src/galois.xml": ["pois <m>\\omega \\neq 1</m> e <m>\\omega \\neq 0</m>", "<m>\\phi_2</m> gera <m>G({\\mathbb Q}(\\omega)/{\\mathbb Q})</m>"],
}
for rel, forbidden in checks.items():
    text = (ROOT / rel).read_text(encoding="utf-8")
    for item in forbidden:
        if item in text:
            raise SystemExit(f"resíduo não corrigido em {rel}: {item!r}")

for xml in sorted((ROOT / "src").glob("*.xml")):
    ET.parse(xml)
print("Todos os src/*.xml estão bem-formados.")
print("Varredura final aplicada e verificada.")
