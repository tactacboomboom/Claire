# Planning With Files (𝕽)

Planning-With-Files is the **reference invariant** 𝕽 in CPE. It is always active. Every sprint runs under its filter.

The core idea: the context window is RAM (volatile, limited). The filesystem is disk (persistent, unlimited). Anything important must be written to disk.

---

## The Three Files

| File | Symbol | Role | When to update |
|------|--------|------|----------------|
| `task_plan.md` | 𝕮ₙ equivalent | Phases, goal, decisions, errors | After each phase |
| `findings.md` | Part of 𝔸ₙ | Research, discoveries, technical decisions | After any discovery |
| `progress.md` | Part of 𝔸ₙ | Session log, test results, error log | Throughout session |

These three files together form 𝔸ₙ (the archive) when frozen at sprint close.

---

## The 2-Action Rule

After every 2 view/search/browser operations → **immediately write key findings to findings.md**.

This prevents information from being lost when the context window fills.

---

## When to Update Which File

```
task_plan.md
├── Starting task (create it first)
├── Completing a phase (change status to complete)
├── Making a major decision (add to Decisions table)
└── Encountering an error (add to Errors table)

findings.md
├── Discovering something new (research, exploration)
├── After 2 view/browser/search operations (mandatory)
├── Making a technical decision (with rationale)
└── Finding useful resources

progress.md
├── Starting a new phase (log start time)
├── Completing a phase (log actions + files modified)
├── Running tests (add to Test Results table)
└── Encountering errors (add to Error Log with timestamp)
```

---

## The 5-Question Reboot Test

Use this to restore full context after any interruption:

| Question | Answer Source |
|----------|---------------|
| Where am I? | Current phase in task_plan.md |
| Where am I going? | Remaining phases |
| What's the goal? | Goal statement in task_plan.md |
| What have I learned? | findings.md |
| What have I done? | progress.md |

---

## Error Protocol (3 strikes)

```
Attempt 1: Diagnose & Fix
  → Read error carefully
  → Identify root cause
  → Apply targeted fix

Attempt 2: Alternative Approach
  → Same error? Try different method
  → Never repeat the exact same failing action

Attempt 3: Broader Rethink
  → Question assumptions
  → Search for solutions

After 3 failures: Escalate
  → Explain what you tried
  → Share the specific error
  → Ask for guidance
```

Log every error in task_plan.md — even resolved ones. This builds knowledge and prevents repetition.

---

## Read vs Write Decision Matrix

| Situation | Action | Reason |
|-----------|--------|--------|
| Just wrote a file | Don't read | Content still in context |
| Viewed image/PDF | Write findings NOW | Multimodal → text before lost |
| Browser returned data | Write to file | Screenshots don't persist |
| Starting new phase | Read plan/findings | Re-orient if context stale |
| Error occurred | Read relevant file | Need current state to fix |
| Resuming after gap | Read all planning files | Recover state |

---

## Relationship to CPE

𝕽 appears as a **condition** on μₙ and εₙ in the CPE equation:

```
μₙ : (𝕮ₙ, 𝕄ₙ₋₁, 𝕡ₙ₋₁, 𝕋ᴳ, 𝕋ₙ, Δ₀ | 𝕽) → 𝕊ₙ
εₙ : (𝕊ₙ | 𝕽) → (𝕡ₙ, 𝔸ₙ)
```

The `| 𝕽` notation means: these operators only produce valid outputs when 𝕽 is active.

A sprint executed without the three files is not a CPE sprint — it is untracked work.
