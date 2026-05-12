# Task Plan: Claire — Documentation Repo

## 🎯 Goal

Créer le repo de documentation Claire qui formalise la méthode CPE (Canonical Pipeline Equation) — chaque objet nommé, typé, documenté — de sorte qu'une nouvelle session puisse comprendre et appliquer la méthode sans contexte préalable.

**PROOF:** Repo GitHub `tactacboomboom/Claire` public avec README + docs/ + templates/ + examples/ complètement remplis.

## 📍 Current Phase

**Phase 8 — Sprints ecosystem.html (IDs + Atlas UX)**

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
- [x] Bouton retour "← Specs" depuis ecosystem.html
- [x] Onglet SOLID & Pipeline — vocabulaire DAG + audit claire-app
- [x] POO — ontologie minimale (vérifié fmaths)
- [x] Design Patterns — 14 essentiels sur 3 familles exhaustives (vérifié fmaths)
- **Status:** complete

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

## 🗂️ Ecosystem.html — Sprints produit

> Branche active : `feat/atlas-concepts`
> Dernier commit : `46f4666` — role pills + goToRole cross-tab navigation

### Sprint accomplis (historique)
- [x] C4 — Tabs Métiers, Préfecture, Théorèmes (53 théorèmes Atlas)
- [x] Atlas tab — 154 concepts, 9 colonnes, 5 filtres
- [x] Role-theorem pairing — computeRolePairs() algorithme sémantique score ≥ 2
- [x] Role pills + goToRole() — navigation croisée Atlas → Métiers

### Phase 7: Product Spec — ecosystem-prd.md
- [x] Définir purpose + public + global attractor d'ecosystem.html
- [x] Mapper les onglets actuels sur les couches raw/transform/mart/viz
- [x] Q3 — rôle de chaque onglet (résolu)
- [x] Q4 — Métiers vs Rôles IT (résolu : différent)
- [x] Q5 — ⊕ Universels → supprimer (résolu)
- [x] Q6 — Filtres Atlas → DDD manquant + labels familles (résolu)
- [x] Produire `ecosystem-prd.md`
- **Status:** complete

### Phase 8: Sprint "Terminologie IDs"
- [ ] Définir le système d'IDs stables (T001-T053, R001-R054, Z001-Z008, D001-D010…)
- [ ] Vérifier cohérence entre tous les onglets
- [ ] Ajouter IDs manquants (SOLID S001-S005, GoF G001-G014, etc.)
- **Status:** pending

### Phase 8b: Sprint C5 "Atlas UX"
- [x] Supprimer bouton ⊕ Universels
- [x] Ajouter filtre "Couche DDD" dans l'Atlas
- [x] Labels familles dans dropdown : "N1 — Matière", "N2 — Mouvement", "N3 — Jonction", "F1 — …"
- [x] Labels familles dans cellules table (FL map)
- [x] Barre filtres sticky
- **Status:** complete

### Phase 9: Sprint C6 "Légende & Ontologie"
- [x] Fusionner onglets SOLID&Pipeline + Théorèmes + Rôles IT en onglet unique "📚 Légendes"
- [x] SOLID & Pipeline découpé en 4 sous-onglets (Pipeline · Code · Architecture · Projets)
- [x] Sommaire par défaut avec description de chaque section
- [x] goToRole() recâblé vers Légendes → Rôles IT
- [x] État mémorisé (_legTab, _solidSubTab)
- **Status:** complete

### Phase 10: Sprint C7 "DAG Layer Labels"
- [x] Étiquette DAG (LAKE/WAREHOUSE/MART/SOURCE/CONSUME) sur chaque bouton topbar
- [x] CSS `.tab-dag` + règle de nommage pour futurs onglets
- [x] Arbitrage : Nature = SOURCE, LAKE/WAREHOUSE/MART = terminologie business
- **Status:** complete

### Phase 10b: Sprint C7b "Atlas Cleanup"
- [x] Retirer filtre `atl-role` de l'onglet Atlas (mart caché dans warehouse)
- [x] Supprimer les 3 lignes role dans filterAtlas()
- [x] Conserver computeRolePairs() pour usage futur en C8
- **Status:** complete

### Phase 11: Sprint C8 "Marts"
- [ ] Onglet dédié 🛒 MART
- [ ] mart_role_stack — fiche complète d'un rôle (théorèmes + outils + zones + nœuds DAG)
- [ ] mart_zone_coverage — pour chaque zone, quels théorèmes et rôles
- [ ] Migrer computeRolePairs() vers le nouvel onglet
- **Status:** pending

### Phase 12: Sprint "Préfecture → Entrepôt industriel"
- [ ] Définir la métaphore entrepôt Amazon (zones physiques ↔ zones IT)
- [ ] Mapper rôles entrepôt ↔ rôles IT ↔ familles F1-F6
- [ ] Rendu visuel — pas un tableau, une viz graphique
- **Status:** pending

### Phase 13: Sprint "Role-as-Skill mapping"
- [ ] Relier chaque rôle ATLAS_DATA à un skill Claude Code (existant ou à créer)
- [ ] Définir le format d'un "skill de domaine" (≠ skill de processus)
- [ ] Prototype : skill `data-engineer` invocable depuis Claude Code
- **Status:** pending

> PRD complet : `ecosystem-prd.md`
> Global Attractor : décodeur IT + orchestre d'agents (4 cas d'usage)
> Q3 (mapping onglets) en cours au moment du compact

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
