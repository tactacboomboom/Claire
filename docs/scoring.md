# Scoring Algorithm

The scoring algorithm evaluates a Sprint Contract **before execution**. It is a pre-filter, not a post-mortem.

A contract is only executable if it passes both thresholds.

---

## Two Independent Scores

| Score | What it measures | Direction |
|-------|-----------------|-----------|
| **μA(C)** | Ambiguity — proportion of interpretable zones | Lower is better |
| **μV(C)** | Validation — proportion of verifiable zones | Higher is better |

These scores are **not opposites**. A contract can be low-ambiguity but low-validation (precise but unverifiable) or high-validation but high-ambiguity (verifiable but unclear).

---

## Structure

A contract C has three components: Goal (G), Backlog (B), Definition of Done (D).

Each is scored independently, then aggregated:

```
μA(C) = (μA(G) + μA(B) + μA(D)) / 3
μV(C) = (μV(G) + μV(B) + μV(D)) / 3
```

---

## Scoring the Goal

### μA(G) — Ambiguity of Goal (4 binary checks)

| Check | Question | 0=OK | 1=Problem |
|-------|----------|------|-----------|
| A₁ | Does the goal contain a vague word? | No vague words | "improve", "optimize", etc. |
| A₂ | Does the goal contain more than one action verb? | 1 verb | 2+ verbs |
| A₃ | Can the result be interpreted in 2 ways? | Unambiguous | Ambiguous |
| A₄ | Is the proof not explicitly named? | Proof named | Proof missing |

`μA(G) = (A₁ + A₂ + A₃ + A₄) / 4`

### μV(G) — Validation of Goal (3 binary checks)

| Check | Condition | 1=Yes |
|-------|-----------|-------|
| V₁ | One unique proof is mentioned | ✓ |
| V₂ | The proof is binary (URL/command/file) | ✓ |
| V₃ | A third party can verify in < 2 minutes | ✓ |

`μV(G) = (V₁ + V₂ + V₃) / 3`

---

## Scoring the Backlog

### μA(bᵢ) — Ambiguity per item (3 binary checks)

| Check | Test |
|-------|------|
| A₁ | Is the item a theme rather than an action? |
| A₂ | Can the item map to more than 1 possible phase? |
| A₃ | Is the size not implicitly bounded? |

`μA(bᵢ) = (A₁ + A₂ + A₃) / 3`

`μA(B) = (1/n) Σ μA(bᵢ)` (average over all items)

### μV(B) — Validation of Backlog (3 binary checks)

| Check | Test |
|-------|------|
| V₁ | Number of items = number of planned phases |
| V₂ | Strict order is preservable |
| V₃ | Each item contributes to at least one DoD criterion |

`μV(B) = (V₁ + V₂ + V₃) / 3`

---

## Scoring the Definition of Done

### μA(dⱼ) — Ambiguity per criterion (3 binary checks)

| Check | Test |
|-------|------|
| A₁ | Does it contain an unbounded human judgment? |
| A₂ | Does it mix multiple proofs? |
| A₃ | Is the proof not directly executable? |

`μA(dⱼ) = (A₁ + A₂ + A₃) / 3`

`μA(D) = (1/m) Σ μA(dⱼ)`

### μV(D) — Validation of DoD (3 binary checks)

| Check | Condition |
|-------|-----------|
| V₁ | ≥1 automatic criterion (URL or command) |
| V₂ | All proofs are traceable |
| V₃ | DoD is independent of phase order |

`μV(D) = (V₁ + V₂ + V₃) / 3`

---

## Aggregation

```
μA(C) = (μA(G) + μA(B) + μA(D)) / 3
μV(C) = (μV(G) + μV(B) + μV(D)) / 3
```

---

## Decision Thresholds

### Ambiguity μA(C)

| Zone | Value | Interpretation |
|------|-------|----------------|
| Stable | μA(C) < 0.25 | Contract is compilable |
| Fragile | 0.25 ≤ μA(C) < 0.5 | Rewrite recommended |
| Non-compilable | μA(C) ≥ 0.5 | **FAIL** — do not execute |

### Validation μV(C)

| Zone | Value | Interpretation |
|------|-------|----------------|
| Robust | μV(C) ≥ 0.7 | Strong validation |
| Partial | 0.4 ≤ μV(C) < 0.7 | Acceptable, watch DoD |
| Weak | μV(C) < 0.4 | **FAIL** — proofs insufficient |

---

## Gate Decision

```
IF μA(C) < 0.5 AND μV(C) ≥ 0.4 → PASS (execute sprint)
ELSE → FAIL (return to contract, identify which component failed)
```

---

## Why Score Before Executing?

A contract that scores μA(C) ≥ 0.5 will produce a bloated, unstable task_plan.md — too many phases, too much ambiguity, constant reinterpretation during execution.

Scoring before executing is cheaper than rewriting mid-sprint. The algorithm is a pre-compiler, not a grading system.
