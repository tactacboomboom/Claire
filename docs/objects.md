# Objects Reference

All objects in the CPE pipeline. Each object has a type, a role, and a concrete equivalent.

---

## Complete Object Table

| Symbol | Name | Type | Produced by | Consumed by | File equivalent |
|--------|------|------|-------------|-------------|-----------------|
| 𝕀₀ | Raw Intention | String (unconstrained) | Human | φ₀ | — |
| 𝕮ₙ | Sprint Contract | Structured document | φ₀ (n=0), κₙ₋₁ (n>0) | 𝕍, μₙ, κₙ | task_plan.md |
| 𝕋ᴳ | Global Attractor | Vision statement | φ₀ | μₙ, κₙ | Section in task_plan.md |
| 𝕋ₙ | Sprint Attractor | Local vision | κₙ₋₁ | μₙ, τₙ | Sprint goal header |
| Δ₀ | Drift Sensor | Rule set | φ₀ | μₙ, εₙ | Anti-patterns checklist |
| 𝕽 | Reference Invariant | Filter (always active) | Human (defined once) | μₙ, εₙ | task_plan.md + findings.md + progress.md |
| 𝕍 | Contract Validator | Gate (pass/fail) | CPE method | 𝕮ₙ | Scoring algorithm |
| 𝕊ₙ | Sprint | Execution context | μₙ | εₙ | The work itself |
| 𝕡ₙ | Product | Shippable artifact | εₙ | τₙ | Code, doc, URL, file |
| 𝔸ₙ | Archive | Frozen record | εₙ | τₙ, κₙ | findings.md + progress.md |
| 𝕄ₙ | Sprint Memory | Compressed context | τₙ | μₙ₊₁, κₙ | sprint-memory.md |

---

## Object Details

### 𝕀₀ — Raw Intention

The unfiltered idea. No format required. Can be a sentence, a paragraph, a voice note transcription.

**Invariant:** 𝕀₀ is consumed exactly once (by φ₀). It is never modified after that. The original intention is preserved as-is.

```
Example:
"I want to build a tool that turns raw intentions into structured sprint contracts."
```

---

### 𝕮ₙ — Sprint Contract

The central object of CPE. Every sprint starts with a valid contract. A contract has exactly three components:

| Component | Symbol | Format reference |
|-----------|--------|------------------|
| Goal | G | [docs/goal.md](goal.md) |
| Backlog | B | [docs/backlog.md](backlog.md) |
| Definition of Done | D | [docs/dod.md](dod.md) |

**Invariant:** A contract is only executable if 𝕍(𝕮ₙ) = PASS, i.e. μA(C) < 0.5 and μV(C) ≥ 0.4.

---

### 𝕋ᴳ — Global Attractor

The answer to: *"What does the finished project look like?"*

Produced once by φ₀. Constrains every subsequent μₙ and κₙ. A sprint that drifts from 𝕋ᴳ is invalid.

**Type:** One paragraph maximum. Must be answerable by a binary: "does this sprint move toward 𝕋ᴳ?"

```
Example:
"A public web app where any user can paste a raw intention and receive
a scored, ready-to-execute sprint contract in under 30 seconds."
```

---

### Δ₀ — Drift Sensor

A set of anti-illusion checks, defined at project start and applied throughout. Detects cognitive drift, scope creep, and false progress.

**Default checks:**
- Is the sprint goal still aligned with 𝕋ᴳ?
- Is there a shippable artifact at the end?
- Is the archive written before closing the sprint?
- Is the next contract based on real outcomes (not on intentions)?

---

### 𝕽 — Reference Invariant

The Planning-With-Files filter. Always active during μₙ and εₙ. Enforces that nothing important exists only in working memory.

**Concrete form:** The three persistent files.

| File | Role |
|------|------|
| task_plan.md | Phases, goal, decisions, errors |
| findings.md | Research, discoveries, technical decisions |
| progress.md | Session log, test results, error log |

---

### 𝕄ₙ — Sprint Memory

The compressed output of τₙ. It is what the next sprint *inherits* from this one.

**Must contain:**
- What was built (𝕡ₙ summary)
- What was decided (key decisions from 𝔸ₙ)
- What remains open (blockers, deferred items)
- How close the project is to 𝕋ᴳ (distance estimate)

**Invariant:** 𝕄ₙ must be readable in under 2 minutes. If it takes longer, τₙ was not applied correctly.
