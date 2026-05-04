# Operators Reference

All operators (morphisms) in the CPE pipeline. Each operator has a defined input, output, and execution protocol.

---

## Complete Operator Table

| Symbol | Name | Input | Output | When |
|--------|------|-------|--------|------|
| φ₀ | Clarification | 𝕀₀ | (𝕮₀, 𝕋ᴳ, Δ₀) | Once, at project start |
| 𝕍 | Validation | 𝕮ₙ | PASS / FAIL + scores | Before every sprint |
| μₙ | Instantiation | (𝕮ₙ, 𝕄ₙ₋₁, 𝕡ₙ₋₁, 𝕋ᴳ, 𝕋ₙ, Δ₀ \| 𝕽) | 𝕊ₙ | Sprint opening |
| εₙ | Production | (𝕊ₙ \| 𝕽) | (𝕡ₙ, 𝔸ₙ) | During sprint |
| τₙ | Distillation | (𝔸ₙ, 𝕡ₙ, 𝕋ₙ) | 𝕄ₙ | Sprint closing |
| κₙ | Evolution | (𝕮ₙ, 𝔸ₙ, 𝕄ₙ, 𝕋ᴳ) | (𝕮ₙ₊₁, 𝕋ₙ₊₁) | Sprint closing |

---

## Operator Details

### φ₀ — Clarification

**The only operator that runs once.**

Takes the raw intention 𝕀₀ and produces three outputs simultaneously:
- **𝕮₀** — The first sprint contract (Goal + Backlog + DoD)
- **𝕋ᴳ** — The global attractor (the finished project vision)
- **Δ₀** — The drift sensor (anti-illusion checks for the whole project)

**Protocol:**
1. Read 𝕀₀ completely
2. Ask: "What does the finished project look like?" → 𝕋ᴳ
3. Ask: "What is the smallest first step that produces something observable?" → 𝕮₀
4. Define 3–5 drift checks → Δ₀
5. Validate 𝕮₀ with 𝕍 before proceeding

**Failure mode:** Producing 𝕮₀ without 𝕋ᴳ. The global attractor is not optional.

---

### 𝕍 — Validator

**A gate, not a filter.** Output is binary: PASS or FAIL.

Scores the contract on two independent dimensions:
- **μA(C)** — Ambiguity score (lower is better, threshold: < 0.5)
- **μV(C)** — Validation score (higher is better, threshold: ≥ 0.4)

See [docs/scoring.md](scoring.md) for the full algorithm.

**Protocol:**
1. Score Goal: μA(G) and μV(G)
2. Score Backlog: μA(B) and μV(B)
3. Score DoD: μA(D) and μV(D)
4. Aggregate: μA(C) = (μA(G) + μA(B) + μA(D)) / 3
5. Decision:
   - μA(C) ≥ 0.5 → FAIL, return to 𝕮ₙ for rewrite
   - μA(C) < 0.5 and μV(C) ≥ 0.4 → PASS

**Invariant:** No sprint executes without 𝕍 = PASS.

---

### μₙ — Instantiation

Opens the sprint. Takes all available context and instantiates the execution environment.

**Inputs explained:**
| Input | Role |
|-------|------|
| 𝕮ₙ | What to do (Goal, Backlog, DoD) |
| 𝕄ₙ₋₁ | What the previous sprint produced |
| 𝕡ₙ₋₁ | The previous artifact (to build on) |
| 𝕋ᴳ | The global constraint |
| 𝕋ₙ | The sprint-local vision |
| Δ₀ | Anti-drift checks |
| 𝕽 | Planning-With-Files filter (always active) |

**Protocol:**
1. Read 𝕄ₙ₋₁ and 𝕡ₙ₋₁ to restore context
2. Verify sprint goal is aligned with 𝕋ᴳ
3. Create/update task_plan.md from 𝕮ₙ backlog
4. Open sprint

**At n=0:** 𝕄₋₁ and 𝕡₋₁ are empty. Start fresh.

---

### εₙ — Production

The sprint execution itself. Runs under the 𝕽 filter at all times.

**Outputs:**
- **𝕡ₙ** — The shippable artifact (code, URL, file, report...)
- **𝔸ₙ** — The frozen archive (findings.md + progress.md at sprint close)

**Protocol:**
1. Work in phases as defined in 𝕮ₙ backlog
2. Update findings.md after every 2 research operations
3. Update progress.md after every phase
4. At close: freeze 𝔸ₙ (no further modifications)

**Invariant:** 𝔸ₙ must exist before κₙ runs. A sprint without an archive cannot chain.

---

### τₙ — Distillation

Compresses the sprint archive into a compact, inheritable memory.

**Input:** The full archive 𝔸ₙ (findings + progress) + the product 𝕡ₙ + the sprint attractor 𝕋ₙ

**Output:** 𝕄ₙ — a document readable in under 2 minutes

**Protocol:**
1. Read 𝔸ₙ fully
2. Extract: what was built, what was decided, what remains open
3. Measure distance to 𝕋ᴳ
4. Write 𝕄ₙ — no more than one page

**Failure mode:** Copying 𝔸ₙ verbatim into 𝕄ₙ. Distillation requires loss — keep only what the next sprint needs.

---

### κₙ — Evolution

Generates the next sprint's contract from the current sprint's outcomes.

**Inputs:**
| Input | Role |
|-------|------|
| 𝕮ₙ | What was planned |
| 𝔸ₙ | What actually happened |
| 𝕄ₙ | What was learned |
| 𝕋ᴳ | What the destination still is |

**Outputs:**
- **𝕮ₙ₊₁** — The next sprint contract
- **𝕋ₙ₊₁** — The next sprint attractor (updated local vision)

**Protocol:**
1. Compare 𝕮ₙ (planned) with 𝔸ₙ (actual)
2. Identify what remains toward 𝕋ᴳ
3. Write the next Goal, Backlog, DoD
4. Validate with 𝕍 before opening sprint n+1

**Invariant:** κₙ must take all four inputs. A contract produced without 𝔸ₙ is speculation, not evolution.
