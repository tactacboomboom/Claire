---
description: Contexte complet ecosystem.html pour démarrer un sprint sans relire le fichier. Encode structure, CSS registry, JS, pièges et règles token-efficaces.
---

# Skill — ecosystem-sprint

Charge ce skill au début de chaque session sur `ecosystem.html`. Il remplace la lecture du fichier pour la prise de contexte initiale.

---

## Fichier cible

```
G:\Mon Drive\10 - Claude\projects\Claire\ecosystem.html
Branch : feat/atlas-concepts
Dernier commit : 29e87ea (Fix C6 — CSS scope)
Taille actuelle : ~3700 lignes
```

---

## Structure HTML — onglets actifs (6)

| Tab ID | Bouton topbar | Contenu |
|--------|--------------|---------|
| `tab-ecosystem` | 🗺️ Ecosystem | Cards projet, PWF tracker |
| `tab-legendes` | 📚 Légendes | Navigation L1 + L2 |
| `tab-nature` | 🧬 Nature | Formulaire ontologique |
| `tab-metiers` | 👔 Métiers | Marts rôle-orientés |
| `tab-prefecture` | 🏛️ Préfecture | Visualisation zones |
| `tab-atlas` | 🗂️ Atlas | 154 concepts, 9 colonnes, 5 filtres |

### Légendes — navigation L1 (4 leg-nav-btn)

| leg ID | Titre | Défaut |
|--------|-------|--------|
| `leg-sommaire` | 📋 Sommaire | actif |
| `leg-solid` | 📐 SOLID & Pipeline | — |
| `leg-theoremes` | 🔬 Théorèmes | — |
| `leg-rolesit` | 🧑‍💻 Rôles IT | — |

### SOLID & Pipeline — navigation L2 (4 solid-sub-btn)

| sub ID | Titre | Contenu | Défaut |
|--------|-------|---------|--------|
| `leg-solid-pipeline` | 🔄 Pipeline | Vocabulaire DAG + Zones orthogonales | actif |
| `leg-solid-code` | 🧬 Code | POO + SOLID + Volatilité + GoF 14 | — |
| `leg-solid-architecture` | 🏗️ Architecture | DDD + Paradigmes + Processus découpe | — |
| `leg-solid-projets` | 📦 Projets | 8 Natures + Division cognitive | — |

### Divs dépréciés (display:none!important — ne pas toucher)

- `tab-solid-orphan` — contenu sections 2-11 tab-solid
- `tab-theoremes-deprecated` + `atlas-mindmap-deprecated`
- `tab-rolesit-deprecated` + `metiers-it-deprecated`

---

## CSS Scoping Registry — CRITIQUE

> Avant toute modification CSS, vérifier dans ce registre. Toute classe ci-dessous ne répond QU'à son sélecteur ID parent.

| Sélecteur racine | Portée | Classes internes |
|-----------------|--------|-----------------|
| `#metiers-it` | Rôles IT | `.mt-header`, `.timeline`, `.era`, `.family`, `.card-grid`, `.card`, `.card-name`, `.card-fr`, `.card-zone`, `.card-narrative`, `.e0`→`.e6`, `.f1`→`.f6`, `.disc-header`, `.disc-body` |
| `#atlas-mindmap` | Théorèmes | `.mm-header`, `.canvas`, `.act`, `.disc-grid`, `.disc`, `.th`, `.th-name`, `.th-narrative`, `.l1`→`.l3`, `.d11`→`.d34` |
| Global (non scopé) | Partout | `.tab-btn`, `.tab-content`, `.leg-nav-btn`, `.leg-section`, `.solid-sub-btn`, `.solid-sub-section`, `.solid-title`, `.ref-table`, `.vocab-grid`, `.vocab-card`, `.dag-flow`, `.atl-ctrl`, `.atl-sel`, `.btype` |

**Règle absolue** : ne jamais renommer `id="metiers-it"` ou `id="atlas-mindmap"`. Si doublon nécessaire, renommer l'ancien en `*-deprecated`.

---

## JS — Fonctions clés

```javascript
// Navigation principale — utilise event.target (ne PAS appeler programmatiquement)
switchTab(name)

// Navigation L1 Légendes — passer this depuis onclick
switchLegTab(name, btn)        // ex: onclick="switchLegTab('solid', this)"

// Navigation L2 SOLID — passer this depuis onclick
switchSolidSubTab(name, btn)   // ex: onclick="switchSolidSubTab('code', this)"

// Navigation depuis pill Atlas → Légendes → Rôles IT (manipulation DOM directe)
goToRole(roleId)               // double setTimeout : 120ms (tab) + 80ms (sub-tab)

// Filtrage Atlas
filterAtlas()                  // lit : atl-type, atl-fam, atl-dag, atl-ddd, atl-role, atl-q

// Rendu Atlas
renderAtlas(rows)              // utilise FL[r.fam] pour labels familles dans cellules
```

### État mémorisé

```javascript
let _legTab = 'sommaire';       // position L1 mémorisée
let _solidSubTab = 'pipeline';  // position L2 mémorisée
```

### Maps de données

```javascript
// FL — family code → label lisible (dropdown + cellules table)
FL = {N1:'N1 — Matière', N2:'N2 — Mouvement', N3:'N3 — Jonction',
      F1:'F1 — Développeurs', F2:'F2 — Data / ML', F3:'F3 — Infra / Ops',
      F4:'F4 — Sécurité', F5:'F5 — Produit / Design', F6:'F6 — Leadership',
      S:'S — SRP', O:'O — OCP', L:'L — LSP', I:'I — ISP', D:'D — DIP'}

// FB — family code → classe CSS badge
FB = { N1:'bn1', N2:'bn2', ... }

// ROLE_PAIRS — calculé par computeRolePairs() depuis ATLAS_DATA
```

---

## Atlas — Filtres actifs (5)

| Select ID | Options | Logique |
|-----------|---------|---------|
| `atl-type` | Tous types / SOURCE / TRANSFORM… | `r.type === type` |
| `atl-fam` | Toutes familles / N1 — Matière… | `r.fam === fam` |
| `atl-dag` | Tous nœuds / 📱 SOURCE… | `r.dag === dag` |
| `atl-ddd` | Toutes couches DDD / domain… | `r.ddd === 'all' \|\| r.ddd.includes(ddd)` |
| `atl-role` | Tous rôles / R001… | `r.roles && r.roles.includes(role)` |

**ddd spécial** : `r.ddd === 'all'` = universel toutes couches → toujours inclus dans tout filtre DDD.

---

## Pièges connus

| # | Piège | Conséquence | Règle |
|---|-------|-------------|-------|
| P1 | `<option>CODE — Label</option>` sans `value` | `r.fam === "N1 — Matière"` échoue | Toujours `<option value="CODE">CODE — Label</option>` |
| P2 | `switchTab()` appelé sans event | `event.target` undefined = erreur silencieuse | Manipulation DOM directe dans goToRole() |
| P3 | Renommer `#metiers-it` ou `#atlas-mindmap` | CSS scopé → rendu texte brut | Ces IDs sont immuables |
| P4 | IDs dupliqués dans le DOM | CSS s'applique aux deux, HTML invalide | Renommer le déprécié en `*-deprecated` |
| P5 | Insert HTML > 150 lignes en 1 Edit | Énorme coût tokens + risque de match partiel | Découper les inserts en blocs thématiques |
| P6 | Lire ecosystem.html en entier | ~1000 tokens pour "vérifier une ligne" | Grep ciblé + Read offset/limit uniquement |

---

## Workflow token-efficient pour un sprint

```
1. /ecosystem-sprint          → charge ce contexte (0 lecture fichier)
2. Grep ciblé                  → localiser la zone exacte (10-30 tokens)
3. Read offset+limit           → lire uniquement les lignes nécessaires
4. Edit ciblé                  → modifier la zone exacte (< 150 lignes new_string)
5. Grep de vérification DoD    → valider sans relire le fichier
6. git add + commit + push     → clore le sprint
7. /compact                    → avant le prochain sprint
```

**Ne jamais** : lire le fichier en entier pour "se remettre en contexte".  
**Toujours** : utiliser ce skill + grep pour naviguer.

---

## Sprints historiques

| Sprint | Commit | Description |
|--------|--------|-------------|
| C4 | 46f4666 | Role pills + goToRole() cross-tab |
| C5 | 3a3373c + 0160d17 | Atlas UX : labels FL, filtre DDD, sticky bar |
| C6 | b9a7098 + 29e87ea | Légendes : fusion 3 onglets + nav L1/L2 |
| C7 | cdbfe8c | DAG Layer Labels — étiquettes pipeline dans topbar |
| C7b | (en cours) | Atlas Cleanup — retrait filtre atl-role (mart hors warehouse) |

---

## Architecture DAG — décisions 2026-05-12

| Onglet | DAG Layer | Type |
|--------|-----------|------|
| Ecosystem | 🧠 CONSUME | Dashboard |
| Légendes | 🪨 LAKE | Data Lake narratif |
| Nature | 📱 SOURCE | Formulaire saisie |
| Métiers | 🛒 MART | Mart rôle-orienté (cible) |
| Préfecture | 🛒 MART | Mart zone-orienté (cible) |
| Atlas | 🏢 WAREHOUSE | Raw browser SST |

**Règle** : LAKE/WAREHOUSE/MART = terminologie business. Tout futur onglet choisit dans { 📱 SOURCE · 🪨 LAKE · 🏢 WAREHOUSE · 🛒 MART · 🎯 SERVE · 🧠 CONSUME }.

---

## Prochain sprint planifié : C8 — Onglet Marts (Phase 11)

- Créer onglet dédié 🛒 MART
- mart_role_stack — fiche complète d'un rôle (théorèmes + outils + zones + nœuds DAG)
- Migrer computeRolePairs() vers cet onglet
- Portée estimée : moyenne (100-200 lignes)
