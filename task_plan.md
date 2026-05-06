# Task Plan: Claire — Documentation Repo

## 🎯 Goal

Créer le repo de documentation Claire qui formalise la méthode CPE (Canonical Pipeline Equation) — chaque objet nommé, typé, documenté — de sorte qu'une nouvelle session puisse comprendre et appliquer la méthode sans contexte préalable.

**PROOF:** Repo GitHub `tactacboomboom/Claire` public avec README + docs/ + templates/ + examples/ complètement remplis.

## 📍 Current Phase

**Phase 1 — en cours**

## 🗓 Phases

### Phase 1: Fichiers CPE + structure
- [x] Créer dossiers (docs/, templates/, examples/, skills/)
- [x] Créer task_plan.md, findings.md, progress.md
- **Status:** complete

### Phase 2: Specs Viewer HTML (specs/index.html)
- [x] Créer specs/index.html — VSCode dark theme, marked.js, 36 fiches CPE
- [x] cs-000 analysé via fmaths Décodeur + nilpotence-cognitive (🟢 done)
- [x] Bouton "🗺️ Ecosystem" dans la topbar (même onglet, pas nouvelle page)
- **Status:** complete (rétro-ingénierie cs-001+ à poursuivre)

### Phase 3: Ecosystem Dashboard (ecosystem.html)
- [x] 3 cartes 3D : 📐 Claire, ⚙️ claire-app, 🗄️ vault
- [x] Copy-to-clipboard sur les chemins locaux
- [x] PWF Tracker — GitHub API commits (refreshPWF)
- [x] Ops & Coûts — Vercel Hobby bandwidth
- [ ] Bouton retour "← Specs" depuis ecosystem.html
- [ ] Onglet SOLID & Pipeline — vocabulaire DAG + audit claire-app
- **Status:** in_progress

### Phase 4: Rétro-ingénierie CPE (multi-sessions)
Sources : clear-sky (21 fiches) + saas-traduction (15 templates)
- [x] cs-000 — CANONICAL_PIPELINE_EQUATION
- [ ] cs-010 — 𝕽 Référentiel invariant
- [ ] cs-020 → cs-200 — objets + morphismes restants
- [ ] Résoudre contradictions C1, C3, C5
- **Status:** in_progress

### Phase 5: Refactor claire-app SOLID-compliant
- [ ] lib/llm.ts — interface LLMProvider (principe D)
- [ ] lib/generate.ts — appel LLM abstrait (principe S)
- [ ] lib/diagnostics.ts — checks ε₀ (principe O — extension)
- [ ] lib/refine.ts — boucle κ₀ (principe O)
- [ ] lib/personas/ — 5 personas PSPO (principes L + I)
- **Status:** pending (après Phase 4)

### Phase 6: README.md + docs/
- [ ] README — pipeline visuel, quick start
- [ ] docs/method.md, objects.md, operators.md
- **Status:** pending

---

## ❓ Key Questions
1. Le repo est-il suffisamment autonome pour qu'une nouvelle session comprenne CPE sans l'auteur ?

## 🛠 Decisions Made
| Décision | Rationnel |
| :--- | :--- |
| Dossier local : `G:\Mon Drive\10 - Claude\projects\Claire` | Séparé du vault (notes perso) |
| Langue : anglais pour docs/ | Cohérence avec PWF de référence |
| Langue : français pour task_plan/findings/progress | Langue de travail de l'auteur |

## 🚨 Errors Encountered
| Error | Attempt | Resolution |
| :--- | :--- | :--- |
| | | |

## 📝 Notes
- Sources : `G:\Mon Drive\10 - Claude\vault\protocole\CPE\sources\`
- Repo GitHub cible : `https://github.com/tactacboomboom/Claire`
- Référence de style : `OthmanAdi/planning-with-files`
