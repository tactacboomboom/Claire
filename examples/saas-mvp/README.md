# Example: SaaS MVP — Lead Capture Landing Page

A complete CPE sprint from raw intention to deployed URL.

---

## Raw Intention (𝕀₀)

```
I want a landing page where visitors can leave their email so I can validate interest in my SaaS idea before building the full product.
```

---

## φ₀ — Clarification Output

### Global Attractor 𝕋ᴳ

```
A public web application where any visitor can submit their email,
the submission is stored in a database, and the founder can export
the list at any time to measure validated demand.
```

### Sprint Contract 𝕮₀

**GOAL:**
```
Deploy a landing page with an email signup form — PROOF: https://[app].vercel.app loads and POST /api/leads returns 201.
SCOPE: 1 page + 1 endpoint + 1 database table
TIMEBOX: 1 sprint
NON-GOALS: email confirmation, analytics dashboard, payments
```

**SPRINT BACKLOG:**
```
1. [BUILD]     Create Next.js project with landing page and CTA button
2. [BUILD]     Create POST /api/leads endpoint storing email in sqlite
3. [INTEGRATE] Connect form submission to /api/leads endpoint
4. [VERIFY]    Deploy to Vercel and confirm public URL works end-to-end
```

**DEFINITION OF DONE:**
```
- [D1] Public URL loads landing page — PROOF: https://[app].vercel.app
- [D2] Form submission creates a DB row — PROOF: curl POST /api/leads returns 201
- [D4] Code pushed to main — PROOF: commit hash on GitHub
```

### Drift Sensor Δ₀
- Is each sprint moving toward 𝕋ᴳ (validated demand list)?
- Is there a shippable artifact at the end?
- Is the archive written before closing?

---

## 𝕍 — Scoring

| Component | μA | μV |
|-----------|----|----|
| Goal G | 0.0 | 1.0 |
| Backlog B | 0.0 | 1.0 |
| DoD D | 0.0 | 1.0 |
| **Contract C** | **0.0** | **1.0** |

**Decision: PASS** — μA(C) = 0.0 < 0.5, μV(C) = 1.0 ≥ 0.4

---

## μ₀ — Sprint Instantiation (task_plan.md)

```markdown
# Task Plan: Lead Capture Landing Page

## Goal
Deploy a landing page with email signup — PROOF: https://[app].vercel.app + curl 201

## Current Phase
Phase 1

## Phases

### Phase 1: Create Next.js project with landing page
- [ ] npx create-next-app@latest lead-capture
- [ ] Build landing page with CTA button
- Status: in_progress

### Phase 2: Create /api/leads endpoint
- [ ] Create pages/api/leads.ts
- [ ] Set up sqlite with better-sqlite3
- Status: pending

### Phase 3: Connect form to endpoint
- [ ] Wire form onSubmit to POST /api/leads
- [ ] Handle success/error states
- Status: pending

### Phase 4: Deploy and verify
- [ ] Push to GitHub, connect Vercel
- [ ] Test public URL and curl endpoint
- Status: pending
```

---

## ε₀ — Production

Sprint executed over 3 hours.

**Product 𝕡₀:** https://lead-capture-demo.vercel.app

**Archive 𝔸₀ highlights (from findings.md):**
- Used `better-sqlite3` instead of Prisma — simpler for a single table
- Vercel serverless functions don't support persistent sqlite — switched to Vercel KV (free tier)
- Form validation done client-side only — sufficient for MVP

---

## τ₀ — Sprint Memory 𝕄₀

```
SPRINT 0 MEMORY

Built: Landing page + email capture endpoint + Vercel KV storage
Deployed: https://lead-capture-demo.vercel.app
Validated: 201 on POST /api/leads, 4 test emails stored

Key decision: sqlite → Vercel KV (serverless constraint)
Deferred: email confirmation, analytics

Distance to 𝕋ᴳ: 60% — storage works, export feature missing
```

---

## κ₀ — Evolution → 𝕮₁

**Next Sprint Goal:**
```
Expose GET /api/leads/export that returns all emails as CSV — 
PROOF: curl downloads a valid CSV with all submitted emails.
SCOPE: 1 endpoint
TIMEBOX: 1 sprint
NON-GOALS: auth, pagination, filtering
```

The chain continues. 𝕄₀ feeds μ₁. 𝕋ᴳ hasn't changed.
