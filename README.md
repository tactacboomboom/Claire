# Claire

> **Clarity for every project.** An AI-powered agile method that transforms a raw intention into a structured, executable sprint contract — and chains each sprint to the next so no project ever loses its thread.

---

## The Problem

You start a project with a clear idea. Three sprints later, you've lost the original intention, accumulated debt, and can't remember why you made half your decisions.

**Claire solves this** by formalizing the full lifecycle: from raw intention to shipped product, sprint by sprint, with memory that persists.

---

## The Pipeline

```
𝕀₀ ──φ₀──► (𝕮₀, 𝕋ᴳ, Δ₀) ──𝕍──► PASS ──μ₀──► 𝕊₀ ──ε₀──► (𝕡₀, 𝔸₀) ──τ₀──► 𝕄₀ ──κ₀──► (𝕮₁, 𝕋₁) ──► ...
```

| Symbol | Name | Role |
|--------|------|------|
| 𝕀₀ | Raw Intention | Your idea, unfiltered |
| φ₀ | Clarification | Turns intention into a contract |
| 𝕮ₙ | Sprint Contract | Goal + Backlog + Definition of Done |
| 𝕋ᴳ | Global Attractor | The vision that never changes |
| Δ₀ | Drift Sensor | Anti-illusion checks |
| 𝕍 | Validator | Scores ambiguity (μA) and validation (μV) |
| μₙ | Instantiation | Opens the sprint |
| 𝕊ₙ | Sprint | Execution |
| εₙ | Production | Delivers product + archive |
| 𝕡ₙ | Product | The shippable artifact |
| 𝔸ₙ | Archive | findings.md + progress.md |
| τₙ | Distillation | Compresses archive into memory |
| 𝕄ₙ | Sprint Memory | What the next sprint inherits |
| κₙ | Evolution | Generates the next contract from this sprint |
| 𝕽 | Reference | Planning-With-Files (the 3 persistent files) |

---

## Quick Start

**Step 1 — Write your raw intention**
```
I want to build a tool that turns raw intentions into sprint contracts.
```

**Step 2 — Run φ₀ (clarification)**

Ask an AI to apply `φ₀`: produce a Sprint Contract with a Goal, Backlog, and Definition of Done.
See [docs/goal.md](docs/goal.md), [docs/backlog.md](docs/backlog.md), [docs/dod.md](docs/dod.md).

**Step 3 — Validate with 𝕍 (scoring)**

Score your contract before executing. If μA(C) ≥ 0.5, the contract is too ambiguous — rewrite it.
See [docs/scoring.md](docs/scoring.md).

**Step 4 — Execute the sprint**

Copy the templates. Work. Update your three files.
See [templates/](templates/).

**Step 5 — Close and chain (κₙ)**

At sprint end, run `κₙ`: generate the next contract from `(𝕮ₙ, 𝔸ₙ, 𝕄ₙ, 𝕋ᴳ)`.
The chain never breaks.

---

## Documentation

| File | Content |
|------|---------|
| [docs/method.md](docs/method.md) | Full pipeline explanation |
| [docs/objects.md](docs/objects.md) | All objects — typed and named |
| [docs/operators.md](docs/operators.md) | All operators — input/output |
| [docs/goal.md](docs/goal.md) | Goal format (Verb + Object + Proof) |
| [docs/backlog.md](docs/backlog.md) | Backlog categories B1/B2/B3 |
| [docs/dod.md](docs/dod.md) | Definition of Done D1–D5 |
| [docs/scoring.md](docs/scoring.md) | Ambiguity + validation scoring |

## Templates

| File | Use |
|------|-----|
| [templates/sprint-contract.md](templates/sprint-contract.md) | Start every sprint here |
| [templates/task_plan.md](templates/task_plan.md) | Track phases and decisions |
| [templates/findings.md](templates/findings.md) | Log research and discoveries |
| [templates/progress.md](templates/progress.md) | Log actions and test results |

## Examples

| Example | Description |
|---------|-------------|
| [examples/saas-mvp/](examples/saas-mvp/) | Full sprint from intention to deployed URL |

---

## Design Principles

- **One sprint = one contract** — no hidden scope
- **Every proof is binary** — done or not done, no narrative
- **Memory is structural** — each sprint inherits from the previous one via 𝕄ₙ
- **The global vision never changes** — 𝕋ᴳ constrains every μₙ and κₙ
- **Ambiguity is measured, not felt** — μA(C) < 0.25 before you execute

---

## License

MIT
