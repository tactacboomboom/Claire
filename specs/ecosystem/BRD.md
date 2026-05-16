# ecosystem.html — BRD
*project-spec v1 · 2026-05-16 · source: MRD.md + ecosystem-prd.md*

---

## O1 — Formalisation

```
ecosystem_BRD : Ω_opportunité_décodeur → Ω_objectifs_produit
```

| | Contenu |
|---|---|
| **Domaine** | Opportunité délimitée par le MRD : décodeur IT navigable pour 54 rôles, 154 concepts, 53 théorèmes |
| **Codomaine** | Objectifs produit mesurables : cas d'usage validés, scope IN/OUT, roadmap phasée |
| **Propriété** | Transformateur · BRD² ≠ 0 (itérable) · convertit l'opportunité en contraintes actionnables |

---

## O2 — GAFAM best practices appliquées

| Pratique | Source | Application ecosystem |
|---|---|---|
| OKRs (Objectives & Key Results) | Google | NSM = trouver le bon rôle en < 2 min ; KR = concepts liés cliqués/session |
| Shape Up "appetit fixe" | Basecamp | Chaque sprint = timebox fixe (1-3h) sur une phase précise |
| "Now/Next/Later" roadmap | Product community | Phase 7-13 = structure Now/Next/Later visible dans task_plan.md |
| "Smallest Useful Thing" | Jeff Patton | v1 = standalone HTML — zéro dépendance serveur, zéro friction |
| Stakeholder map (RACI-like) | PM standard | 1 maker (Yanis) · 0 stakeholders externes · audience = showcase + soi |

---

## O3 — Négation talmudique

| Ce que BRD N'EST PAS | Document correct |
|---|---|
| Liste de features → PRD | PRD.md |
| Architecture technique → SRD | SRD.md |
| Vision sans contraintes → MRD | MRD.md |
| Contrat figé | Il évolue avec la roadmap phasée |
| Document pour stakeholders externes | Projet solo — audience = soi-même + showcase |

---

## O4 — Formulaire science (ordre cognitif)

1. **Quels objectifs mesurables ce projet doit-il atteindre ?** → Business Objectives
2. **Quel scope est IN pour la version actuelle ?** → Scope IN
3. **Qu'est-ce qui est explicitement OUT ?** → Scope OUT
4. **Quelles contraintes s'imposent ?** → Constraints
5. **Quelle roadmap structure les phases ?** → Release Roadmap

---

## Sommaire canonique

### Business Objectives

| Objectif | Métrique | Cible |
|---|---|---|
| **O1 — Orientation** | Temps pour trouver le rôle correspondant à un profil (NSM) | < 2 min |
| **O2 — Décodage** | Fiche de poste → concepts Atlas identifiés / session | ≥ 3 concepts par session |
| **O3 — Showcase** | Outil présentable sur LinkedIn sans explication préalable | Auto-explicatif à 80% |
| **O4 — Orchestration** | Chaque rôle = 1 skill Claude Code invocable | 54 rôles couverts en Phase 13 |

---

### Scope IN (version actuelle)

| Feature | Justification |
|---|---|
| 6 onglets actifs (Ecosystem · Légendes · Nature · Métiers · Préfecture · Atlas) | Déjà livrés — base stable |
| ATLAS_DATA : 154 concepts × 9 colonnes | Source de vérité — ne jamais dupliquer |
| 54 rôles IT (ROLE_PAIRS via computeRolePairs()) | Matching théorèmes × rôles actif |
| 53 théorèmes (Atlas mindmap) | Formalisés en N1/N2/N3 |
| Navigation croisée Atlas → Rôles (goToRole()) | Linéage CU1 → CU2 |
| Filtres Atlas : type · famille · DAG · DDD | Accès warehouse direct |
| DAG Layer Labels sur chaque onglet | Lisibilité architecture interne |

---

### Scope OUT (explicitement exclus)

| Exclusion | Raison |
|---|---|
| Backend serveur / API | Standalone HTML — contrainte I1 nœud DAG |
| Auth / multi-utilisateurs | Produit personnel — pas SaaS |
| Persistence données utilisateur | LocalStorage acceptable, base de données non |
| CMS ou édition inline | Édition = directement dans ATLAS_DATA (JS) |
| Export PDF / print | Non prévu dans les 4 CU |
| Internationalisation (EN) | Français only pour v1 |

---

### Constraints

| Contrainte | Impact |
|---|---|
| **Fichier unique** ecosystem.html | Tout tient en < 5000 lignes — pas de bundler, pas de framework |
| **Zéro réseau obligatoire** | marked.js + toutes libs = inlinées ou CDN avec fallback |
| **Tokens Claude Code** | Chaque sprint < 150 lignes new_string — P5 : découper les inserts |
| **CSS scoping strict** | `#metiers-it` et `#atlas-mindmap` = IDs immuables |
| **Git** branch `feat/atlas-concepts` → PR → main avant deploy | Vercel = main only |

---

### Release Roadmap

| Phase | Sprint | Durée estimée | Status |
|---|---|---|---|
| Phase 7 | Product Spec (ecosystem-prd.md) | 1h | ✅ complete |
| Phase 8 | IDs stables T001-T053, R001-R054 | 30 min | pending |
| Phase 9 | Légendes & Ontologie (fusion 3 onglets) | 2h | ✅ complete |
| Phase 10 | Atlas UX (filtres + labels) | 1h | ✅ complete |
| Phase 11 | Marts onglet dédié (mart_role_stack) | 2h | pending |
| Phase 12 | Préfecture → Entrepôt industriel | 3h | pending |
| Phase 13 | Role-as-Skill mapping (54 rôles) | > 1 jour | pending |

---

## Ker / Im

| | Contenu |
|---|---|
| **Ker** | Objectifs O1-O4 délimités · Scope IN/OUT explicite · Contrainte standalone respectée |
| **Im → PRD via R2** | Objectifs mesurables → cas d'usage numérotés (CU1-CU4) + features par use case |
