# Goal Format

The Sprint Goal is the first component of a Sprint Contract 𝕮ₙ. It must be **non-interpretable**: a third party can validate it without asking you a single question.

---

## Format

```
[VERB] [OBJECT] so that [USER/USE] — PROOF: [ONE proof]
```

With three mandatory bounds:

```
SCOPE:     [max 1 screen OR 1 endpoint OR 1 script]
TIMEBOX:   [<= 1 sprint]
NON-GOALS: [2 bullets max]
```

---

## The Three Operators

A valid goal contains exactly three operators:

| Operator | Rule | Examples |
|----------|------|---------|
| **VERB** (action) | One action verb | create, expose, deploy, calculate, connect |
| **OBJECT** (what) | One precise target | page, endpoint, workflow, file, report |
| **PROOF** (how we know) | One binary, executable proof | URL, command, file path, commit hash |

**Formula:** `g := Action + Object + Proof`

---

## Invariants

1. **1 sprint = 1 result** — not 3 features disguised as 1
2. **0 vague words** — "improve", "optimize", "clean", "intuitive", "robust" are banned
3. **1 main proof** — multiple proofs = ambiguity

---

## Categories

Choose exactly one:

| Category | Pattern | Example |
|----------|---------|---------|
| **URL/Product** | "A public URL that does X" | `Deploy landing page — PROOF: https://... loads` |
| **Function** | "A command that returns Y" | `Expose POST /api/leads — PROOF: curl returns 201` |
| **CI/Quality** | "Tests pass on Z" | `Make npm test pass — PROOF: GitHub Actions green` |
| **Artifact** | "A generated file" | `Export report.json — PROOF: file matches schema` |

---

## Stability Test

A goal is **stable** if:
- One person can validate it in under 2 minutes
- No explanation is needed
- A third party can check "done" without talking to you

A goal is **unstable** if:
- Validation takes more than 2 minutes → too much implicit content
- You need to explain it → goal is malformed
- The proof is negotiable → rewrite

---

## Scoring (μA and μV for G)

**Ambiguity μA(G)** — 4 binary checks (0=OK, 1=problem):

| Check | Question |
|-------|----------|
| A₁ | Does the goal contain a vague word? |
| A₂ | Does the goal contain more than one action verb? |
| A₃ | Can the result be interpreted in 2 different ways? |
| A₄ | Is the proof not explicitly named? |

`μA(G) = (A₁ + A₂ + A₃ + A₄) / 4`

**Validation μV(G)** — 3 binary checks (1=yes):

| Check | Condition |
|-------|-----------|
| V₁ | One unique proof is mentioned |
| V₂ | The proof is binary (URL/command/file) |
| V₃ | A third party can verify in < 2 minutes |

`μV(G) = (V₁ + V₂ + V₃) / 3`

---

## Examples

**Good**

```
Create a public landing page with one CTA button — PROOF: URL loads and CTA scrolls to signup section.
SCOPE: 1 page
TIMEBOX: 1 sprint
NON-GOALS: payments, auth
```

```
Expose POST /api/leads that stores email in sqlite — PROOF: curl returns 201 and row exists.
SCOPE: 1 endpoint + 1 table
TIMEBOX: 1 sprint
NON-GOALS: email verification, analytics
```

**Bad**

```
Build a better user experience for the dashboard
```
→ No verb of transformation. No object. No proof. Entirely interpretable.

```
Improve the API performance and add error handling and write tests
```
→ Three verbs. Three objects. No proof. μA(G) = 1.0.
