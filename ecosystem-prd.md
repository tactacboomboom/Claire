# ecosystem.html — Product Requirements Document

**Date:** 2026-05-11
**Branch active:** `feat/atlas-concepts`
**Dernier commit:** `46f4666`

---

## 🎯 Global Attractor

> **ecosystem.html = un décodeur de l'IT et un orchestre d'agents** — qui permet de comprendre l'essence de chaque rôle, de cartographier une organisation depuis une fiche de poste, d'orienter n'importe qui vers son métier naturel, et d'invoquer la bonne expertise au bon moment via des sub-agents spécialisés. Accessible via la métaphore industrielle, formalisé via la taxonomie IT.

---

## 📋 Cas d'usage (4)

| # | Cas d'usage | Description |
|---|-------------|-------------|
| CU1 | **Career compass** | "Quel rôle correspond à qui je suis ?" — test d'orientation vers un métier IT |
| CU2 | **Job decoder** | "Cette fiche de poste dit quoi en vrai ?" — décomposer le jargon recrutement en taxonomie formelle |
| CU3 | **Org mapper** | "Comment est structurée cette équipe ?" — cartographier une organisation avant d'y avoir mis les pieds |
| CU4 | **Agent orchestration** | "Pour ce problème, quel rôle/skill invoquer ?" — chaque rôle = un sub-agent Claude spécialisé |

---

## 👥 Audience

| Public | Mode d'entrée | Usage |
|--------|--------------|-------|
| **Soi-même** | Direct | Mémorisation, construction de l'ontologie, exploration |
| **Recruteurs / LinkedIn** | Showcase | Preuve de maîtrise conceptuelle |
| **Jeunes en orientation IT** | Métaphore industrielle | CU1 — orientation métier |
| **Professionnels IT** | Taxonomie formelle | CU2, CU3, CU4 |

**Note :** Pas vocation à être présenté à des non-IT — la métaphore industrielle (Entrepôt Amazon) est la porte d'entrée pour eux.

---

## 🗂️ Architecture couches (DAG → dbt → ecosystem.html)

| Couche DAG | Équivalent dbt | Dans ecosystem.html |
|------------|---------------|---------------------|
| STORE RAW | `sources` | `ATLAS_DATA` — 154 concepts, source de vérité |
| TRANSFORM | modèles `stg_/int_` | `computeRolePairs()`, fonctions dérivées |
| STORE STRUCTURED | `marts` | `ROLE_PAIRS` (actuel) + marts à créer |
| SERVE | exposures/API | `renderAtlas()`, `renderRoleBadges()` |
| CONSUME | dashboards/viz | Onglets HTML — ce que l'utilisateur voit |

---

## 🗺️ Mapping onglets actuels → couches (Q3 résolu)

| Onglet | Rôle (un mot) | Couche DAG | Décision / Notes |
|--------|--------------|-----------|-----------------|
| 🗺️ Ecosystem | Navigation | Meta | **À refondre** — lié à claire-app (séparé) ; à reconstruire pour ecosystem seul |
| 📐 SOLID & Pipeline | Légende | Raw reference | = "Paramètres" — ontologie, taxonomie, concepts, légende globale |
| 🧬 Nature | Advisor | Hors couches | **Produit autonome** — questionnaire → template projet (TDD, fichiers, dossiers, layers free tier) ; à brainstormer séparément |
| 👔 Métiers | Marts | Mart layer | Marts rôle-orientés : sous-onglets mart_xxx dérivés du STORE RAW — spec data à définir |
| 🏛️ Préfecture | Visualisation | Serve/Viz | **Refonte 3D/gaming** — clic sur nœud = rôles + outils + théorèmes associés |
| 🔬 Théorèmes | Légende | Raw reference | → À fusionner dans un onglet "Légendes générales" (sous-onglet) |
| 🧑‍💻 Rôles IT | Légende | Raw reference | → À fusionner dans "Légendes générales" (+ historiographie des métiers IT) |
| 🗂️ Atlas | Warehouse | STORE RAW | Source de vérité = ATLAS_DATA ; accès direct rare — tout dérive de là |

**Q4 résolu :** 👔 Métiers ≠ 🧑‍💻 Rôles IT — Rôles IT = légende/raw taxonomy ; Métiers = marts dérivés (questions orientées rôle)

**Note 🧬 Nature :** Concept "sous-côté" mais à fort potentiel — système de templates de projets basé questionnaire. Hors scope PRD actuel, à traiter en sprint séparé.

---

## 🚀 Sprints planifiés

| Phase | Sprint | Status |
|-------|--------|--------|
| Phase 7 | Product Spec — ce document | in_progress |
| Phase 8 | Terminologie IDs — système d'IDs stables cross-onglets | pending |
| Phase 9 | Légende & Ontologie — fusionner SOLID+Pipeline + Théorèmes + Rôles IT | pending |
| Phase 10 | Store Raw explicite — nommer ATLAS_DATA comme source de vérité | pending |
| Phase 11 | Marts — onglet dédié, mart_role_stack en premier | pending |
| Phase 12 | Préfecture → Entrepôt Amazon — refonte visuelle complète | pending |
| Phase 13 | Role-as-Skill mapping — relier chaque rôle à un skill Claude Code | pending |

---

## 🔍 Décisions issues des questions ouvertes

### Q5 — ⊕ Universels (résolu)
**Décision : supprimer le bouton.**
Raison : l'utilisateur ne comprend pas sa valeur. Un concept `univ: true` = présent dans toutes les familles — cette notion n'est pas intuitive sans légende. À terme, si "Universel" redevient utile, le traiter comme une valeur du filtre Type, pas un bouton isolé.

### Q6 — Filtres Atlas insuffisants (résolu)
**Problèmes identifiés :**
1. **Couche DDD absente** — pas de filtre par couche DDD (Domain, Application, Infrastructure…)
2. **Familles sans label** — le dropdown famille affiche "N1", "F4" sans explication ; l'utilisateur ne connaît pas les codes par cœur
3. **Code couleur bon mais insuffisant** — les couleurs sont conservées, mais il manque une légende lisible

**Décisions :**
- Ajouter filtre "Couche DDD" dans l'Atlas
- Dans le dropdown famille : afficher "N1 — Matière", "N2 — Mouvement", "N3 — Jonction", "F1 — …", etc.
- Ces améliorations = scope Sprint "Atlas UX" (à insérer avant ou pendant Phase 8)

---

## 🔗 Vision long terme : Role-as-Agent

La taxonomie ecosystem.html devient une **matrice de compétences invocables** :

```
Tâche identifiée
→ Atlas: nœuds DAG + zones + acte N1/N2/N3
→ Rôles matchés via ROLE_PAIRS
→ Invocation du skill Claude Code correspondant
→ Workflow de domaine enforced (TDD, debugging, review...)
```

Les 14 skills Claude Code existants = **workflows de processus** (comment faire)
Les skills à construire = **workflows de domaine** (ce que sait chaque rôle)
Les deux ensemble = remplacement de 5 ETP par orchestration d'agents spécialisés.

---

## ❓ Questions ouvertes

| Q | Question | Status |
|---|----------|--------|
| Q3 | Rôle de chaque onglet en un mot | **résolu** |
| Q4 | 👔 Métiers vs 🧑‍💻 Rôles IT — même chose ou différent ? | **résolu** |
| Q5 | ⊕ Universels — supprimer ou repositionner ? | **résolu** |
| Q6 | Filtres Atlas — suffisants ou à revoir ? | **résolu** |
