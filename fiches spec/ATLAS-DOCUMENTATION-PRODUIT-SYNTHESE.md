# ATLAS DE LA DOCUMENTATION PRODUIT
## Intégration fmaths + Protocole de Brainstorming

**Situation** : Tu veux cartographier TOUT l'univers de la documentation produit (MRD, BRD, PRD, SRD) en appliquant le protocole **fmaths** pour en extraire la structure formelle ET le protocole de brainstorming pour en extraire le workflow opérationnel.

**Ce document** : Un atlas qui fusionne les deux perspectives — la rigueur mathématique (fmaths) avec la praticité du brainstorming.

---

## PARTIE 1 : MAP MENTALE DE L'UNIVERS DOCUMENTAIRE

### Les quatre documents et leurs rôles (fmaths Passe 2)

```
┌─────────────────────────────────────────────────────────────────┐
│                        MRD (Marché)                             │
│                  Pourquoi + Pour qui ?                          │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ • Problème marché réel (research-based)                 │   │
│  │ • Customer segments & pain points                       │   │
│  │ • Market size & growth                                  │   │
│  │ • Success metrics: adoption, revenue                    │   │
│  └──────────────────────────────────────────────────────────┘   │
│  Audience: Marketing, Execs, Product Manager                    │
│  Timeline: Stable (1+ année)                                     │
│  Update frequency: Quarterly reviews                             │
└─────────────────────────────────────────────────────────────────┘
                              ↓
                      [RUPTURE 1]
        "Market → Strategy" (réduction intentionnelle)
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                        BRD (Business)                            │
│                  Quels objectifs business ?                      │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ • Business case (ROI, timeframe, ressources)            │   │
│  │ • Stakeholder requirements & constraints                │   │
│  │ • Strategic goals (rétention, revenu, etc.)             │   │
│  │ • Scope de phase 1 (réduction du marché complet)        │   │
│  └──────────────────────────────────────────────────────────┘   │
│  Audience: PM, Project Managers, Business Analysts               │
│  Timeline: Moyen (1-2 trimestres)                                │
│  Update frequency: Per sprint or per phase                       │
└─────────────────────────────────────────────────────────────────┘
                              ↓
                      [RUPTURE 2]
    "Strategy → Features" (choix créatifs multiples)
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                        PRD (Produit)                             │
│                  Quelles fonctionnalités ?                       │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ • User stories & personas                               │   │
│  │ • Functional requirements & flows                        │   │
│  │ • Acceptance criteria (testables)                        │   │
│  │ • UI/UX guidelines & interactions                        │   │
│  └──────────────────────────────────────────────────────────┘   │
│  Audience: Product Manager, UX Designer, Developers              │
│  Timeline: Court (1-2 sprints)                                   │
│  Update frequency: Multiple times per sprint                     │
└─────────────────────────────────────────────────────────────────┘
                              ↓
                      [RUPTURE 3]
  "Features → Architecture" (trade-offs techniques)
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                        SRD (Technique)                           │
│                  Comment construire ?                            │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ • System architecture & components                       │   │
│  │ • Technical constraints & non-functionals                │   │
│  │ • API specs, data models, workflows                      │   │
│  │ • Security, performance, scalability targets             │   │
│  └──────────────────────────────────────────────────────────┘   │
│  Audience: Developers, Architects, QA Engineers                  │
│  Timeline: Court (1 sprint or less)                              │
│  Update frequency: Live during coding                            │
└─────────────────────────────────────────────────────────────────┘
                              ↓
                      [RUPTURE 4]
      "Spec → Reality" (révélateur d'implicites)
                              ↓
                            CODE
```

### Les trois socles immuables (fmaths)

```
    ┌─────────────────────────────────────────┐
    │   SOCLE 1: COHÉRENCE D'INTENTION        │
    │  (Même idée à chaque niveau              │
    │   juste plus détaillée)                  │
    │                                          │
    │  MRD: "Fragmentation du marché"          │
    │  BRD: "Plateforme unifiée"               │
    │  PRD: "Features intégrées"               │
    │  SRD: "Services interconnectés"          │
    │  Code: "APIs que se parlent"             │
    │                                          │
    │  ✓ Cohérent (même intention)             │
    └─────────────────────────────────────────┘

    ┌─────────────────────────────────────────┐
    │   SOCLE 2: TRAÇABILITÉ BIDIRECTIONNELLE │
    │  (Chaque requirement trace au précédent  │
    │   ET chaque problème a une solution)     │
    │                                          │
    │  PRD Feature X → BRD Goal Y → MRD Problem Z
    │  Et vice versa :                         │
    │  MRD Problem Z → BRD Goal Y → PRD Feature X
    │                                          │
    │  ✗ Requirement orphelin = construcción inutile
    │  ✗ Problème non-couvert = spec incomplète
    └─────────────────────────────────────────┘

    ┌─────────────────────────────────────────┐
    │   SOCLE 3: NON-REDONDANCE                │
    │  (Chaque document a un rôle unique,      │
    │   ne refait pas le boulot du suivant)    │
    │                                          │
    │  MRD ≠ BRD (marché ≠ stratégie)          │
    │  BRD ≠ PRD (objectifs ≠ features)        │
    │  PRD ≠ SRD (features ≠ architecture)     │
    │                                          │
    │  ✗ Redondance = bruit, confusion         │
    └─────────────────────────────────────────┘
```

---

## PARTIE 2 : WORKFLOW DE BRAINSTORMING APPLIQUÉ À CHAQUE DOCUMENT

### Phase par phase: où chaque document est produit

#### PHASE 0 → MRD : APERTURE (Leadership + Direction)

**Durée** : 15 min  
**Brainstorm** : Toi + Product Owner / Executive

**Questions clés** :
1. Quel est le **problème réel** qu'on adresse ? (data-based, pas intuition)
2. **Qui** le souffre le plus ? (segmentation)
3. À **quelle fréquence** ? (magnitude)
4. **Quel coût** si on ne résout pas ? (urgency)
5. **Market size** ? (est-ce que ça vaut la peine ?)

**Artefact produit** :

```markdown
# MRD — [Product Name]

## Problem Statement (Market Level)
- **The Problem**: [Ce que les gens souffrent]
- **Segments Affected**: [Qui exactement]
- **Frequency/Magnitude**: [Combien souvent, impact économique]
- **Current Workarounds**: [Comment ils gèrent aujourd'hui]

## Market Opportunity
- **Market Size**: [TAM/SAM/SOM]
- **Growth Rate**: [% YoY]
- **Competitive Landscape**: [Who else is solving this]

## Success Metrics
- **Primary**: [Le métrique qui prouve qu'on a résolu le problème]
- **Secondary**: [Other indicators]

## Timeline & Constraints
- **Must Solve By**: [Date]
- **Budget**: [If any]
- **External Dependencies**: [Market factors, tech availability]
```

**Validation MRD** (avant d'aller plus loin):
- ✓ Le problème est réel (research, data, ou expérience client)
- ✓ C'est notre compétence de le résoudre
- ✓ Les success metrics sont mesurables

---

#### PHASE 1 → BRD : DISCOVERY + DEFINE (Problèmes + Scope)

**Durée** : 40-50 min brainstorm  
**Participant** : Toi + PM + Execs (stakeholder alignment)

**Pont avec le MRD** :
```
MRD dit : "Les devs perdent 2h/day à chercher du code"
        ↓
BRD doit dire : "Nous, on cible LEQUEL de ces devs ?
                 Python/JS only? France only? Startups only?"
        ↓
INSIGHT: BRD reduit volontairement le marché du MRD
         (C'est normal, c'est une stratégie)
```

**Questions clés** :
1. De tous les segments du MRD, lequel on vise ? (Scope reduction)
2. Quel est notre **business case** ? (Revenue model, timeline, ROI)
3. Quels objectifs business mesurables ? (Rétention, ARPU, market share)
4. **Stakeholder alignment** : qui faut convaincre ? Quels sont leurs objectifs ?

**Artefact produit** :

```markdown
# BRD — [Product Name]

## Executive Summary
[1 paragraph: Pourquoi on fait ça, c'est quoi l'impact]

## Business Objectives
- **Primary Goal**: [Le métrique de succès business]
- **Secondary Goals**: [Autres objectifs alignés]
- **Target Segments**: [Lequel du MRD on vise réellement]

## Business Case
- **Revenue Model**: [Comment on fait du cash ?]
- **Timeline to Profitability**: [Quand ?]
- **Investment Required**: [Combien ça coûte à construire/lancer]
- **ROI Projection**: [Quels returns]

## Stakeholder Requirements
| Role | Primary Need | Success Metric |
|------|-------------|---|
| Sales | Easy-to-sell value prop | [Metric] |
| Customer Success | Easy to onboard | [Metric] |
| Finance | Profitable by Q[X] | [Metric] |

## Constraints & Dependencies
- **Timeline**: "Launch by [date]"
- **Team**: "We have N people for [duration]"
- **Tech**: "We own our data, no reliance on 3rd party APIs"

## Phase 1 Scope Definition
- **In**: [Features/problems we're solving in phase 1]
- **Out**: [Features/problems for phase 2+]
```

**Validation BRD** (avant d'aller au PRD) :
- ✓ Chaque objectif business trace au MRD (covariance)
- ✓ Scope est clairement défini ("phase 1 = ..." vs "future = ...")
- ✓ Stakeholders sont alignés (ce doc a été validé par Finance, Sales, etc.)

---

#### PHASE 2 → PRD : DEFINE + DESIGN (Features + Workflows)

**Durée** : 50-60 min brainstorm  
**Participant** : Toi + PM + UX Designer (creative choices)

**Pont avec le BRD** :
```
BRD dit : "Objectif: Augmenter rétention de 20%"
       ↓
PRD doit dire : "Comment ? Via notifications ?
                 Via recommandations ? Via communauté ?
                 Nous choisissons : [Feature X, Y, Z]"
       ↓
INSIGHT: PRD fait un CHOIX CRÉATIF que BRD ne détermine pas
         (C'est l'art du PM de trancher)
```

**Questions clés** :
1. Pour chaque objectif BRD, quelles features le réalisent ? (Features list)
2. Qui sont les **personas utilisateur** ? (Workflows different par persona)
3. Pour chaque feature, quel est le **user workflow** ? (Happy path + edge cases)
4. Quels **acceptance criteria** ? (Testable, precise)

**Artefact produit** :

```markdown
# PRD — [Product Name]

## Product Vision
[1-2 paragraphs: Quoi on construit, pour qui, pourquoi]

## Personas
| Persona | Primary Goal | Pain Point | Success Metric |
|---------|-------------|------------|---|
| Developer | Find code faster | "Lost 2h searching" | Find in <10 sec |
| Reviewer | Spot reusable patterns | "Can't suggest improvements" | ... |

## Features (Phase 1)

### Feature 1: Snippet Storage
**User Story**: "As a Developer, I want to save code snippets so that I can reuse them later"
**Acceptance Criteria**:
- User can create snippet with: code, title, language, tags
- User can edit snippet metadata
- User can delete own snippets
- Snippets are stored with version history

### Feature 2: Search & Discovery
**User Story**: "As a Developer, I want to search by language/tags so that I find relevant code fast"
**Acceptance Criteria**:
- Search results return in <10 seconds
- Filter by language dropdown
- Filter by tags (multi-select)
- Pagination for >10 results
- Syntax highlighting on results

[Continue for each feature]

## User Workflows (Detailed)

### Workflow: Create & Share Snippet
```
1. User writes code, clicks "Save Snippet"
2. Form appears: Title, Language (dropdown), Tags, Visibility (private/team/public)
3. User fills ~30 sec
4. Click "Save"
5. Snippet indexed, searchable immediately
```

### Workflow: Find & Reuse
```
1. User needs JWT validation code
2. Types in searchbar "jwt validation"
3. Results appear (3-5 snippets) in <10 sec
4. User clicks one, syntax highlighting appears
5. User copies, pastes into IDE
```

## Non-Functional Requirements
- **Performance**: Search results in <10 sec
- **Scalability**: Support 10,000 snippets min
- **Reliability**: 99% uptime
- **Security**: User auth (email/password), private snippets encrypted at rest

## Out of Scope (Phase 2+)
- Collaborative editing
- AI-powered recommendations
- Community features
- Advanced analytics
```

**Validation PRD** (avant d'aller au SRD) :
- ✓ Chaque feature maps à un objectif BRD
- ✓ User workflows sont testables (pas vague)
- ✓ Acceptance criteria sont précis et vérifiables
- ✓ "Out of Scope" est clair (tu n'as pas promis trop)

---

#### PHASE 3 → SRD : DESIGN + REVIEW (Architecture + Implementation)

**Durée** : 50-60 min brainstorm  
**Participant** : Toi + Tech Lead + Architect (technical choices)

**Pont avec le PRD** :
```
PRD dit : "Feature: Search snippets by language"
       ↓
SRD doit dire : "Techniquement, comment ?
                 Database: SQLite or PostgreSQL?
                 Index strategy: B-tree on language?
                 Query latency target: 500ms?
                 Pagination: 10 results per page?"
       ↓
INSIGHT: SRD fait des TRADE-OFFS TECHNIQUES
         (Simplicité vs scalabilité, Coût vs perf)
```

**Questions clés** :
1. Quels **composants** ? (Frontend, Backend, Database, External services)
2. Quel **data model** ? (Tables, relationships, constraints)
3. Quel **API design** ? (Endpoints, request/response format, error handling)
4. Quels **non-functional targets** ? (Performance, scalability, security)
5. Quels **trade-offs conscients** ? ("We're choosing X over Y because...")

**Artefact produit** :

```markdown
# SRD — [Product Name]

## System Architecture

### Components
```
┌─────────────────────────────────────────┐
│         FRONTEND (React)                 │
│  ┌──────────────┐    ┌──────────────┐  │
│  │ SearchPage   │    │ SnippetDetail│  │
│  │              │───▶│              │  │
│  └──────────────┘    └──────────────┘  │
│         │                  │             │
└─────────┼──────────────────┼─────────────┘
          │ HTTP/REST        │
    ┌─────▼──────────────────▼──────┐
    │   BACKEND API (Node/Express)   │
    │  ┌──────────┐  ┌──────────┐   │
    │  │ /search  │  │ /snippets│   │
    │  └──────────┘  └──────────┘   │
    └─────────┬──────────────────────┘
              │ SQL Queries
    ┌─────────▼──────────────────────┐
    │  DATABASE (SQLite MVP)          │
    │  Tables: snippets, tags         │
    └────────────────────────────────┘
```

### Technology Choices & Trade-offs

| Decision | Choice | Reason | Sacrifice |
|----------|--------|--------|-----------|
| Framework | React | Component-based, ecosystem | Bundle size |
| Backend | Node/Express | JS fullstack, fast dev | Scaling complexity |
| Database | SQLite MVP, PostgreSQL prod | Zero ops, then scalability | Migration at scale |
| Search | Full-text on DB | Fast to implement | Limited for large datasets |

## Data Model

```sql
TABLE snippets (
  id INT PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  code TEXT NOT NULL,
  language VARCHAR(50) NOT NULL,  -- javascript, python, etc.
  description TEXT,
  created_by VARCHAR(255) NOT NULL,
  created_at TIMESTAMP,
  visibility ENUM('private', 'team', 'public'),
  INDEX (language, created_at)
)

TABLE tags (
  id INT PRIMARY KEY,
  snippet_id INT FK snippets.id,
  tag_name VARCHAR(100),
  UNIQUE (snippet_id, tag_name)
)

TABLE snippet_versions (
  id INT PRIMARY KEY,
  snippet_id INT FK snippets.id,
  code TEXT NOT NULL,
  changed_by VARCHAR(255),
  changed_at TIMESTAMP
)
```

## API Specification

### GET /api/search?q=jwt&lang=javascript
**Purpose**: Search snippets by query + filters  
**Response**:
```json
{
  "total": 5,
  "results": [
    {
      "id": 1,
      "title": "JWT Validation",
      "code": "const verify = (token) => {...}",
      "language": "javascript",
      "tags": ["jwt", "security"],
      "created_at": "2024-05-11"
    }
  ]
}
```
**Performance Target**: <500ms  
**Pagination**: Limit 10 results, offset-based

### POST /api/snippets
**Purpose**: Create new snippet  
**Request**:
```json
{
  "title": "...",
  "code": "...",
  "language": "javascript",
  "tags": ["jwt"],
  "visibility": "private"
}
```
**Response**: 201 Created + snippet ID  
**Validation**: Title required, code required, language from enum

[Continue for each endpoint]

## Security & Performance

- **Auth**: Simple JWT tokens (not OAuth MVP)
- **CORS**: Whitelist origins
- **SQL Injection**: All queries parameterized
- **Rate Limiting**: 100 req/min per IP
- **Caching**: No Redis MVP (add later if needed)
- **Scalability**: SQLite fine for <100k snippets

## Deployment Plan
- **Development**: `npm install && npm run dev`
- **Production**: Railway backend + Vercel frontend
- **Database**: SQLite locally, PostgreSQL on Railway

## Known Limitations & Future Improvements
- Search on large datasets will degrade (→ migrate to Elasticsearch phase 2)
- Single-server deployment (→ add load balancing phase 2)
- No collaborative features (→ phase 2)
```

**Validation SRD** (avant coding) :
- ✓ Chaque feature PRD peut être implémentée via cette architecture
- ✓ Trade-offs sont explicites ("We chose SQLite for MVP, but...")
- ✓ API contracts sont clairs (endpoints, requests, responses)
- ✓ Performance targets sont mesurables (<500ms latency)
- ✓ Security baseline est couverte (no obvious holes)

---

## PARTIE 3 : CARTOGRAPHIE DES TENSIONS & RUPTURES

### Les 4 ruptures critiques et comment les valider

```
    MRD
     ↓
  [RUPTURE 1]
  VALIDATION:
    ✓ BRD adresse tous les problèmes du MRD ?
    ✓ BRD réduit intentionnellement le scope ? (et c'est OK)
    ✓ Stakeholders alignés sur la réduction ?
     ↓
    BRD
     ↓
  [RUPTURE 2]
  VALIDATION:
    ✓ Chaque feature PRD trace à un objectif BRD ?
    ✓ Pas de feature "orpheline" (cool mais unjustified) ?
    ✓ User workflows sont testables ?
     ↓
    PRD
     ↓
  [RUPTURE 3]
  VALIDATION:
    ✓ Chaque technical requirement trace à une feature PRD ?
    ✓ Trade-offs sont explicites et acceptés ?
    ✓ Timeline et ressources sont réalistes ?
     ↓
    SRD
     ↓
  [RUPTURE 4]
  VALIDATION:
    ✓ Code implémente toutes les features SRD ?
    ✓ Aucun "shortcut" techniquement grave ?
    ✓ Si découverte d'implicites → feeding back pour améliorer le process
     ↓
    CODE
```

### Les 5 axes de variation (où chaque document se situe)

```
ABSTRACTION
│
│  MRD (très abstrait: "fragmentation du marché")
│   │
│   │
│  BRD (abstrait-moyen: "offrir une plateforme unifiée")
│   │
│   │
│  PRD (moyen-concret: "features: chat, files, calendar")
│   │
│   │
│  SRD (concret: "3 microservices avec API REST")
│   │
│   ├─────────────────────────────────────────────────── BUSINESS
│   │
└───────────────────────────────────────────────────── TECHNICAL

      WIDE SCOPE          │         NARROW SCOPE
  (Marché entier)        │      (Une feature)
         │               │           │
      MRD/BRD            │          PRD/SRD
         │               │           │
     Large market        │      Specific feature
                         │
```

---

## PARTIE 4 : CHECKLIST DE COHÉRENCE INTÉGRALE

Avant de démarrer le coding, vérifie ces points :

### ✓ Cohérence MRD ↔ BRD
- [ ] Chaque problème MRD est adressé dans le BRD (même s'il est réduit en scope)
- [ ] BRD justifie pourquoi on réduit le scope du MRD (stratégie consciente)
- [ ] Objectifs business du BRD tracent directement au problème du MRD

### ✓ Cohérence BRD ↔ PRD
- [ ] Chaque objectif business a au moins une feature PRD qui l'adresse
- [ ] Aucune feature "orpheline" (cool mais non-justifiée)
- [ ] User workflows du PRD réalisent les objectifs du BRD

### ✓ Cohérence PRD ↔ SRD
- [ ] Chaque feature PRD peut être implémentée via l'architecture SRD
- [ ] Acceptance criteria du PRD sont techniquement testables
- [ ] Performance/scalability targets du SRD sont cohérentes avec l'usage attendu

### ✓ Cohérence SRD ↔ Code
- [ ] Tous les endpoints API du SRD ont un implémentation plan
- [ ] Database schema du SRD est réalisable
- [ ] Non-functional requirements sont mesurables (<500ms, 99% uptime, etc.)

### ✓ Absence de Redondance
- [ ] MRD ne parle pas de business case (c'est le BRD)
- [ ] BRD ne spécifie pas des features (c'est le PRD)
- [ ] PRD ne parle pas d'architecture (c'est le SRD)
- [ ] SRD ne parle pas de code en détail (c'est pendant le coding)

### ✓ Absence de Contradiction
- [ ] Aucune affirmation dans un document ne contredit une autre
  - Exemple: BRD dit "multilingue" mais PRD dit "English only MVP" → contradiction douce, à résoudre
  - Exemple: PRD demande "real-time" mais SRD dit "polling every 30sec" → contradiction dure, critique
- [ ] Si contradiction trouvée → marquée comme "DECISION POINT" et résolue explicitement

### ✓ Traçabilité Bidirectionnelle
- [ ] **Vers le bas** : Chaque requirement du SRD trace à un feature du PRD
- [ ] **Vers le haut** : Chaque feature du PRD trace à un objectif du BRD
- [ ] **Vers le haut** : Chaque objectif du BRD trace à un problème du MRD
- [ ] **Réciproquement** : Chaque problème du MRD est couvert par une feature du PRD

---

## PARTIE 5 : TEMPLATES PRÊTS À L'EMPLOI

(Voir les sections Phase 0-3 ci-dessus pour les templates détaillés)

Pour un projet **snippet manager** ou similaire, utilise directement :
1. `/outputs/FMATHS-DOCUMENTATION-PRODUIT-PASSE1.md` — structure formelle
2. `/outputs/FMATHS-DOCUMENTATION-PRODUIT-PASSE2.md` — narration high-level
3. `/outputs/PROTOCOL-BRAINSTORM-SPECS.md` — workflow opérationnel

---

## CODA : COMMENT UTILISER CET ATLAS

### Pour commencer un nouveau projet

1. **Remplis le MRD** (15 min) → Valide avec execs
2. **Brainstorm BRD** (30-40 min) → Valide avec stakeholders
3. **Brainstorm PRD** (50 min) → Valide avec PM + UX
4. **Brainstorm SRD** (50 min) → Valide avec architecture
5. **Checklist de cohérence** (10 min) → Identifie gaps
6. **Coding session** (120+ min) → Implémente le SRD sans questions

### Pour débugger un projet en difficulté

Utilise les **4 ruptures** comme diagnostic :

- **"Le code ne matche pas le PRD"** → Rupture 3 cassée (SRD flou)
- **"Le PRD ne matche pas les objectifs business"** → Rupture 2 cassée (PRD mal defini)
- **"On a des features orphelines"** → Rupture 2 cassée (PRD non-tracé au BRD)
- **"Personne ne sait pourquoi on fait ça"** → Rupture 1 cassée (BRD pas aligné au MRD)

Pour chaque rupture cassée, reviens à la phase précédente et refais la clarification.

---

## RÉFÉRENCES

- **fmaths Passe 1** : Analyse formelle via Ensembles, Logique, Invariants, Axes, Ruptures, Catégories, Topologie, Probabilités
- **fmaths Passe 2** : Décodeur narrative (les 9 actes qui te l'expliquent en français)
- **Protocol Brainstorm** : Phases 0-6, templates, checklist, optimisations tokens
- **Cet Atlas** : Point de fusion entre formalisme et praticité

**Deeplink** : Pour aller plus loin sur un concept (ex: "Dette d'intention"), see Passe 2, Acte 4, Section "Rupture 4".
