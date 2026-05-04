# Definition of Done

The Definition of Done (DoD) is the third component of a Sprint Contract 𝕮ₙ. It answers: **"How do we know the sprint is done?"**

It does not explain *how* to do the work. It defines *how to decide that it is finished*.

---

## Core Logic

Done is a logical AND, not a feeling:

```
Done(C) ⟺ ∧ᵢ check(dᵢ) = pass
```

No fuzzy aggregation. Binary. Strict.

---

## Five Proof Types (mutually exclusive)

Each DoD criterion must belong to exactly one type:

### D1 — URL
> Validation by external access

```
[D1] Public URL is reachable — PROOF: https://myapp.vercel.app loads
```

### D2 — Command
> Validation by local/CI execution

```
[D2] All tests pass — PROOF: `npm test` returns exit code 0
```

### D3 — Artifact
> Validation by file existence/conformity

```
[D3] Export file exists — PROOF: dist/report.json exists and matches schema
```

### D4 — Repo
> Validation by Git traceability

```
[D4] Changes pushed — PROOF: commit abc123 on main branch
```

### D5 — Human
> Disciplinary validation (never alone)

```
[D5] Human signature recorded — PROOF: date + name
```

**Hard rule: D5 can never be the only criterion.** It must accompany at least one of D1–D4.

---

## Invariants

1. **Each DoD criterion has ONE main proof** (not "URL + tests + feeling")
2. **No narrative words** — "correct", "clean", "documented" without a proof → invalid
3. **Context-independent** — a third party can validate without talking to you
4. **Order-independent** — the DoD validates the final result, not the phase sequence

---

## Stability Tests

A criterion is **unstable** if:
- The proof is not directly executable or clickable
- It depends on judgment ("readable", "up to date", "clear")
- It depends on an unbounded future ("will be monitored", "will be optimized")

A criterion is **stable** if:
- The proof is immediate (URL, command, file)
- Verification takes < 1 minute
- The result is binary

---

## Scoring (μA and μV for D)

**Ambiguity per criterion μA(dⱼ):**

| Check | Test |
|-------|------|
| A₁ | Does it contain an unbounded human judgment? |
| A₂ | Does it mix multiple proofs? |
| A₃ | Is the proof not directly executable? |

`μA(dⱼ) = (A₁ + A₂ + A₃) / 3`

`μA(D) = (1/m) Σ μA(dⱼ)`

**Validation μV(D):**

| Check | Condition |
|-------|-----------|
| V₁ | ≥1 automatic criterion (URL or CMD) |
| V₂ | All proofs are traceable |
| V₃ | DoD is independent of phase order |

`μV(D) = (V₁ + V₂ + V₃) / 3`

---

## Mapping to task_plan.md

- DoD does **not** become a phase
- DoD **constrains** the `complete` status of every phase
- A phase cannot be marked `complete` if it makes the DoD impossible to reach

In progress.md, DoD acts as the final exit barrier: all criteria must be checked before closing.

---

## Examples

**Good**

```
## Definition of Done

- [D1] Public URL is reachable — PROOF: https://myapp.vercel.app loads
- [D2] All tests pass — PROOF: `npm test` returns exit code 0
- [D4] Changes pushed to main — PROOF: commit hash on GitHub
```

**Bad**

```
- App works correctly
- Code is clean
- Documentation updated
```
→ No proof type. No executable evidence. Not validatable by a third party.
