# ecosystem.html — SRD
*project-spec v1 · 2026-05-16 · source: PRD.md + ecosystem.html (feat/atlas-concepts)*

---

## O1 — Formalisation

```
ecosystem_SRD : Ω_comportements_utilisateur → Ω_implémentation
```

| | Contenu |
|---|---|
| **Domaine** | Comportements utilisateur validés (4 CU, features F1.1-F4.3) |
| **Codomaine** | Implémentation concrète : fichier unique, fonctions JS, structure HTML, données |
| **Propriété** | Terminus · SRD² = SRD (idempotent) — relire le SRD ne change pas l'implémentation |

---

## O2 — GAFAM best practices appliquées

| Pratique | Source | Application ecosystem |
|---|---|---|
| Single-file architecture | Progressive enhancement | 1 fichier HTML = zéro build, zéro dépendance serveur, déployable sur Pages |
| Data-first design (dbt pattern) | dbt community | ATLAS_DATA = source unique de vérité → tous les rendus dérivent de là |
| Incremental computation | dbt incremental models | computeRolePairs() calculé 1 fois au load — pas de recalcul sur filtre |
| CSS scoping (BEM-like) | CSS community | `#metiers-it .card`, `#atlas-mindmap .th` — isolation stricte par section |
| Feature flags via JS const | Google | Filtres actifs/inactifs = modification de filterAtlas() seulement |

---

## O3 — Négation talmudique

| Ce que SRD N'EST PAS | Document correct |
|---|---|
| Liste de features (WHAT) | PRD.md |
| Contraintes business (WHY) | BRD.md |
| Documentation de déploiement | Vercel dashboard + .github/workflows |
| Spec API ou endpoints | Pas d'API — standalone HTML |
| ADR sur chaque choix tech | ADR.md (fiche spec séparée) |

---

## O4 — Formulaire science (ordre cognitif)

1. **Quelle est l'architecture réelle du fichier ?** → Structure HTML + sections
2. **Où sont les données et comment circulent-elles ?** → Data model + transformations
3. **Quelles fonctions JS implémentent les CU ?** → Fonctions clés + linéage PRD
4. **Quelles sont les contraintes d'implémentation non-négociables ?** → CSS scoping + pièges connus
5. **Qu'est-ce qui est done vs pending dans le code ?** → DoR/DoD par feature

---

## Sommaire canonique

### Architecture fichier

```
ecosystem.html (~3700 lignes · feat/atlas-concepts)
├── <head>         — meta, styles inline (~500 lignes CSS)
├── <body>
│   ├── topbar     — 6 boutons tab + DAG label badges
│   ├── tab-ecosystem   — PWF tracker + cartes projets
│   ├── tab-legendes    — nav L1 (4) + nav L2 SOLID (4)
│   ├── tab-nature      — formulaire ontologique
│   ├── tab-metiers     — marts rôle-orientés (#metiers-it)
│   ├── tab-prefecture  — visualisation zones
│   └── tab-atlas       — 154 concepts, 9 col, 5 filtres (#atlas-mindmap scope)
└── <script>
    ├── ATLAS_DATA[]    — source de vérité (154 concepts)
    ├── FL, FB maps     — family code → label / badge CSS
    ├── computeRolePairs() → ROLE_PAIRS
    ├── switchTab()     — navigation principale
    ├── switchLegTab()  — navigation L1 Légendes
    ├── switchSolidSubTab() — navigation L2 SOLID
    ├── goToRole()      — cross-tab Atlas → Rôles
    ├── filterAtlas()   — 5 filtres (type/fam/dag/ddd/q)
    └── renderAtlas()   — rendu table Atlas
```

---

### Data Model

#### ATLAS_DATA — structure d'un concept (154 entrées)

```javascript
{
  id:    "C001",          // ID stable (cible Phase 8)
  name:  "Aggregate",     // nom canonique
  fr:    "Agrégat",       // traduction FR
  type:  "ENTITY",        // SOURCE | TRANSFORM | ENTITY | RULE | PATTERN | METRIC
  fam:   "N1",            // N1/N2/N3 ou F1-F6 ou S/O/L/I/D
  dag:   "WAREHOUSE",     // SOURCE | LAKE | WAREHOUSE | MART | SERVE | CONSUME
  ddd:   "domain",        // domain | application | infra | interface | "all"
  roles: ["R005","R016"], // rôles associés (IDs stables)
  th:    ["T007","T022"], // théorèmes associés (optionnel)
  def:   "...",           // définition courte
}
```

**Règle** : `ddd:"all"` = universel toutes couches → toujours inclus dans tout filtre DDD.

#### ROLE_PAIRS — computed (54 rôles × théorèmes)

```javascript
// Calculé par computeRolePairs() depuis ATLAS_DATA
// Score ≥ 2 = association retenue
// Structure : { roleId: [{ th, score, concepts[] }] }
```

---

### Fonctions JS — linéage PRD

| Fonction | CU linéagé | Lignes approx. | Notes |
|---|---|---|---|
| `switchTab(name)` | Tous | ~15 | Ne PAS appeler programmatiquement (P2) |
| `switchLegTab(name, btn)` | CU1/CU2 | ~20 | État mémorisé dans `_legTab` |
| `switchSolidSubTab(name, btn)` | CU2 | ~20 | État mémorisé dans `_solidSubTab` |
| `goToRole(roleId)` | CU1 | ~30 | Double setTimeout 120ms + 80ms — DOM direct |
| `computeRolePairs()` | CU1/CU4 | ~60 | Calculé 1× au load — score sémantique |
| `filterAtlas()` | CU2 | ~40 | Lit 5 selects + q input |
| `renderAtlas(rows)` | CU2 | ~80 | FL[r.fam] pour labels familles |

---

### CSS Scoping — règles absolues

| ID racine | Portée stricte | Classes internes |
|---|---|---|
| `#metiers-it` | Onglet Métiers uniquement | `.mt-header`, `.card`, `.card-name`, `.e0`→`.e6`, `.f1`→`.f6` |
| `#atlas-mindmap` | Théorèmes (Légendes) uniquement | `.mm-header`, `.canvas`, `.th`, `.d11`→`.d34` |

**Règle absolue** : ne jamais renommer ces deux IDs. Si doublon → renommer l'ancien en `*-deprecated`.

---

### Pièges connus (P-registry)

| # | Piège | Conséquence | Règle |
|---|---|---|---|
| P1 | `<option>CODE — Label</option>` sans `value` | filtre échoue silencieusement | Toujours `value="CODE"` |
| P2 | `switchTab()` appelé sans event | `event.target` undefined | DOM direct dans goToRole() |
| P3 | Renommer `#metiers-it` ou `#atlas-mindmap` | CSS scopé → rendu texte brut | IDs immuables |
| P4 | IDs dupliqués dans le DOM | CSS s'applique aux deux | Renommer le déprécié en `*-deprecated` |
| P5 | Insert HTML > 150 lignes en 1 Edit | Coût tokens + risque match partiel | Découper en blocs thématiques |
| P6 | Lire ecosystem.html en entier | ~1000 tokens inutiles | Grep ciblé + Read offset/limit |

---

### DoR / DoD par feature (features pending)

#### F3.2 — Préfecture refonte 3D (Phase 12)

**DoR :** Métaphore Entrepôt Amazon définie · 8 zones Z001-Z008 mappées · rôles/outils/théorèmes par zone spécifiés

**DoD :** Clic zone → panel rôles + théorèmes affiché · CSS scopé `#prefecture-3d` · goToRole() fonctionnel depuis panel · sprint < 200 lignes

#### F4.3 — mart_role_stack (Phase 11)

**DoR :** Onglet 🛒 MART créé · structure mart_role_stack définie (théorèmes + outils + zones + DAG) · computeRolePairs() migré

**DoD :** Sélectionner un rôle → fiche complète affichée · linéage `// [PRD:CU4] mart_role_stack` dans le code

#### F4.2 / F1.4 — Role-as-Skill (Phase 13)

**DoR :** 54 skills de domaine créés dans `~/.claude/skills/roles/` · format SKILL.md de domaine défini (≠ skill de processus)

**DoD :** Clic rôle → commande `/skill-[role]` copiée dans clipboard · workflow de domaine documenté dans chaque SKILL.md

---

### Dette technique connue

| # | Dette | Impact | Phase cible |
|---|---|---|---|
| DT1 | IDs concepts non stables (C001 manquants dans certains) | Links cassent si ordre change | Phase 8 |
| DT2 | `computeRolePairs()` non migré vers Mart | Couplage warehouse↔mart | Phase 11 |
| DT3 | Filtre `atl-role` supprimé C7b — ROLE_PAIRS inutilisé | Perte d'accès mart depuis warehouse | Phase 11 |
| DT4 | `tab-solid-orphan`, `*-deprecated` → dead code | +~300 lignes inutiles | Phase 11+ |
| DT5 | Onglet Nature sans spec dédiée | Risque scope creep | Sprint dédié post-Phase 13 |

---

## Ker / Im

| | Contenu |
|---|---|
| **Ker** | Architecture décrite · Data model spécifié · Fonctions linéagées · Pièges documentés · DoR/DoD par feature pending |
| **Im → Code via R4** | SRD = contrat d'implémentation — toute feature doit tracer vers CU[N] via `// [PRD:CU1]` |
| **Référence ligne** | ecosystem.html · branch `feat/atlas-concepts` · ~3700 lignes |
