# Sprint Backlog

The Sprint Backlog is the second component of a Sprint Contract 𝕮ₙ. It is not a list of ideas — it is a **decomposition of the Goal into transformation units**.

---

## Core Invariant

```
1 backlog item ⟺ 1 phase in task_plan.md
```

If an item cannot become a phase directly, it is invalid.

**Formal definition:**

`decompose : Goal → {b₁, b₂, ..., bₙ}`

with the constraint: `∀bᵢ, compile(bᵢ) = Phaseᵢ`

---

## Three Categories (mutually exclusive)

Every item must belong to exactly one:

### B1 — Build
> Create or modify an executable artifact

```
[BUILD] Create POST /api/leads endpoint
[BUILD] Implement score calculation logic
[BUILD] Add signup form to landing page
```

### B2 — Integrate
> Connect two existing elements

```
[INTEGRATE] Connect signup form with /api/leads
[INTEGRATE] Wire endpoint to sqlite database
[INTEGRATE] Add Stripe webhook to order flow
```

### B3 — Verify
> Make observable / testable

```
[VERIFY] Deploy app and expose public URL
[VERIFY] Add test for lead creation
[VERIFY] Run npm test on CI
```

**Rule:** Documentation alone is never a valid backlog item. It is a task inside a phase, not an item.

---

## Invariants

### Invariant 1 — Strict bijection
- Number of backlog items = number of phases in task_plan.md
- Order preserved (backlog → chronological phases)

### Invariant 2 — Action, not theme

❌ `"Auth"`, `"Frontend"`, `"API"`, `"Security"`

✅ `"[BUILD] Implement POST /login endpoint"`, `"[BUILD] Create static signup page"`

### Invariant 3 — Sprint-sized
- Achievable without depending on another sprint
- Verifiable before the final DoD

---

## Stability Tests

An item is **unstable** if:
- You have to explain orally what it means
- It can be interpreted as more than one possible phase

An item is **stable** if:
- It can be renamed automatically to `Phase N: [verb + precise object]`
- A task checklist follows from it without invention

---

## Scoring (μA and μV for B)

**Ambiguity per item μA(bᵢ):**

| Check | Test |
|-------|------|
| A₁ | Is the item a theme rather than an action? |
| A₂ | Can the item map to more than 1 possible phase? |
| A₃ | Is the size not implicitly bounded? |

`μA(bᵢ) = (A₁ + A₂ + A₃) / 3`

`μA(B) = (1/n) Σ μA(bᵢ)`

**Validation μV(B):**

| Check | Test |
|-------|------|
| V₁ | Number of items = number of planned phases |
| V₂ | Strict order is preservable |
| V₃ | Each item contributes to at least one DoD criterion |

`μV(B) = (V₁ + V₂ + V₃) / 3`

---

## Mapping to task_plan.md

| Sprint Backlog | task_plan.md |
|----------------|--------------|
| Item i | Phase i |
| Item title | Phase title |
| Category (B1/B2/B3) | Nature of tasks |
| Backlog order | Chronological order |

The **Key Questions**, **Decisions**, and **Errors** sections in task_plan.md do **not** come from the backlog — they are execution residues.

---

## Examples

**Good**

```
## Sprint Backlog

1. [BUILD] Create POST /api/leads endpoint
2. [INTEGRATE] Connect signup form with /api/leads
3. [VERIFY] Deploy app and expose public URL
```

**Bad**

```
1. Auth
2. Frontend
3. Tests
```
