# PROTOCOLE DE BRAINSTORMING & SPÉCIFICATION
## Du Concept Code au Projet Livrable en Zero Aller-Retour

**Contexte** : Utilisation de Claude Code pour développer des projets informatiques avec un protocole de spec progressif qui économise tokens et évite les reformulations inutiles.

---

## PHASE 0 : APERTURE (Leadership + Direction)

### Objectif
Établir le contexte, les enjeux et l'intention stratégique du projet avant toute exploration technique.

### Artefacts à produire

#### **0.1 — PROJECT CHARTER** (Document source unique)
Une feuille A4-ish qui répond à ces questions en langage naturel :

```
🎯 PRODUCT OUTCOME (Problème général)
   "Quel est le problème utilisateur ou business qu'on adresse ?"
   Exemple : "Les développeurs perdent 2h/jour à chercher des snippets de code réutilisables"

🔍 VISION (État futur désiré)
   "Que devient le monde si ce problème disparaît ?"
   Exemple : "Une base centralisée avec versioning et indexation pour retrouver tout en <5s"

👥 STAKEHOLDERS & ROLES
   - Product Owner : [Qui prend les décisions métier ?]
   - Tech Lead : [Qui valide les contraintes techniques ?]
   - AMOA informelle : [Qui s'assure de l'alignement intention ↔ code ?]

⚠️ CONTRAINTES FONDAMENTALES
   - Budget tokens Claude Code : ~2-3 sessions de brainstorm max
   - Complexité : Low/Medium/High ?
   - Timeline : "Prod ready in 2 weeks" ou "MVP explor" ?
   - Dépendances externes : [APIs, données, permissions]

💡 SUCCÈS = Critères minimaux
   - Fonctionnel : [Listez 3-4 capabilities qui valent le projet]
   - Non-fonctionnel : [Perf, fiabilité, maintenabilité]
   - D'adoption : [Qui utilise ? Combien de fois par semaine ?]
```

**Responsable** : Toi + Product Owner (peut être toi)  
**Durée** : 15 min  
**Output** : 1 fichier texte brut, ~200 mots

---

## PHASE 1 : DISCOVERY (Définition du Problème)

### Objectif
Clarifier le **Problem Space** : explorer l'étendue du problème avant de proposer une solution.

### Protocole de Brainstorm
**Durée** : 30-40 min avec Claude  
**Mode** : Conversation naturelle, tu peux être brut

```
PROMPT TEMPLATE :

"Je suis un vibe codeur qui utilise Claude Code. Voici mon Project Charter :
[Colle le contenu de Phase 0]

Je commence la phase de DISCOVERY.

Aide-moi à :
1) Cartographier les PROBLÈMES SPÉCIFIQUES (pas juste le problème général)
   → Exemple : "Difficile de retrouver un snippet" → Se décline en :
      • Pas d'indexation par langage
      • Pas de contexte d'utilisation
      • Dupes de logique métier

2) Identifier les PERSONAS secondaires (qui subit le problème ?)
   → Exemple : Code reviewers qui signalent des patterns à réutiliser

3) Constraints & Opportunities
   → Ce qu'on ne peut PAS faire (coûterait trop / trop risqué)
   → Ce qu'on POURRAIT faire mais qui est hors scope

À la fin, consigne-moi dans un document structuré qui déplie progressivement
jusqu'à 5-7 problèmes spécifiques et leurs impacts."
```

### Artefacts à produire

#### **1.1 — PROBLEM ANALYSIS** (En concurrent Discord/notion)
```markdown
## PROBLEM BREAKDOWN (Issue Tree)

### Root Problem
[La formulation brute du charter]

### Specific Problems (5-7 déclinaisons)
1. **Discoverability**
   - Impact : 45 min/dev/semaine perdus en recherche
   - Symptômes : "J'ai écrit ça il y a 3 mois, où c'est ?"
   - Magnitude : Affecte 100% des devs

2. **Accuracy / Trust**
   - Impact : Snippets obsolètes, causent bugs 2-3x par sprint
   - Symptômes : "J'ai copié sans tester, c'était en Python 2"
   - Magnitude : Affecte 30% des utilisations

3. **Maintenance Burden**
   - Impact : Pas de propriétaire, dépendances fantômes
   - Magnitude : Affecte l'équipe archit

[... continuer pour chaque spécificité]

## PERSONAS IMPACTÉES
- **Developer** (Utilisateur primaire) : Cherche → Copie → Code
- **Code Reviewer** (Utilisateur secondaire) : Identifie patterns → Suggest réutilisation
- **Tech Lead** (Décideur) : Mesure dette technique
```

#### **1.2 — OPPORTUNITY MAP** (En concurrent table)
```
| Problème spécifique | Urgence | Faisabilité | Bénéfice | Go/No-Go Phase 1 |
|---|---|---|---|---|
| Discoverability | HAUTE | FACILE | ++++ | ✅ MUST |
| Accuracy/versioning | HAUTE | MOYEN | +++ | ✅ MUST |
| Maintenance | MOYENNE | DIFFICILE | ++ | ❌ FUTURE (Phase 2) |
```

**Responsable** : Toi + Claude (brainstorm guidé)  
**Durée** : Produit du brainstorm, formatage 10 min  
**Output** : 2 docs Markdown

---

## PHASE 2 : DEFINE (Convergence sur le Scope)

### Objectif
Transformer les problèmes en **SCOPE CLAIR** : qu'est-ce qu'on construit VRAIMENT ?

### Protocole

```
PROMPT TEMPLATE :

"Sur la base de la PROBLEM ANALYSIS précédente, je veux DEFINEr le scope
du projet. Aide-moi à :

1) SCOPING: De la liste de problèmes, lesquels on résout en PHASE 1 ?
   → Objectif : réduire à 2-3 problèmes clés
   → Question clé : 'Quel est le MINIMUM qui rend le projet viable ?' 
      (cf. Arrive principle : révélateur d'implicites)

2) REQUIREMENTS STRUCTURE (Product Requirements)
   → Features (capabilities qu'on build)
   → Non-Features (ce qu'on ne fait PAS)
   → Success Metrics (comment on mesure qu'on a résolu le problème ?)

3) USER WORKFLOWS
   → Pour chaque persona : comment change-t-il son workflow ?
   → Avant → Après (avant le tool, après le tool)
   → Cas de succès et cas d'edge qui cassent le workflow

À la fin : donne-moi une PRD mini-structure directement réutilisable
pour la phase de design."
```

### Artefacts à produire

#### **2.1 — SCOPE STATEMENT** (En concurrent 1-pager)
```
## IN SCOPE (Phase 1)
- Feature A : Indexation par langage + snippet storage
- Feature B : Recherche full-text + regex support
- Non-Feature : Collaboration temps-réel (→ Phase 2)
- Non-Feature : Analytics d'usage (→ Phase 2)

## SUCCESS METRICS
- **Adoption** : 80% des devs l'utilisent 1x/semaine
- **Speed** : Retrouver un snippet en <10 sec vs 45 min
- **Quality** : 0 bugs causés par snippets "moisis"
```

#### **2.2 — MINI PRD** (Product Requirements Document)

**Structure** (inspirée des images : MRD → BRD → PRD → SRD)

```markdown
# PRODUCT REQUIREMENTS DOCUMENT (PRD)
## Snippet Manager v1.0

### 1. PRODUCT OVERVIEW
**Product Name** : SnippetHub  
**Problem Statement** : [Du charter, version condensée]  
**Target Users** : Developers, Code Reviewers, Tech Leads  
**Success Criteria** : [Les metrics de 2.1]  

### 2. USER WORKFLOWS (Avant/Après)

#### Workflow 1: Contribute a Snippet
**AVANT** :
1. Dev écrit du code réutilisable
2. "Où je la mets ?" → [Silence awkward]
3. Oubliée dans un .txt local
4. Perte totale

**APRÈS** :
1. Dev finit son code, clique "Save Snippet"
2. Ll : Langage, Tags, Description ~30 sec
3. Automatiquement indexée et searchable

#### Workflow 2: Find & Reuse
**AVANT** :
1. Dev a besoin d'un pattern → Slack "Quelqu'un a du code pour faire X ?"
2. Attend réponse 30 min
3. Sinon : réwrite from scratch

**APRÈS** :
1. Searchbar "JWT validation" → 3 résultats en 2 sec
2. Copy-paste prêt à l'emploi (avec version info)
3. 0 contexte de réinvention

### 3. FUNCTIONAL REQUIREMENTS (FRs)

| ID | Feature | Description | Acceptance Criteria |
|---|---|---|---|
| FR1 | Snippet Storage | CRUD pour snippets | User peut C/R/U/D ses snippets |
| FR2 | Search | Full-text + filter par langage/tags | Retrouver snippet en <10 sec |
| FR3 | Versioning | Historique des modifications | Voir qui/quand a modifié |
| FR4 | Sharing | Visibility control (private/team/public) | User peut limiter qui voit |

### 4. NON-FUNCTIONAL REQUIREMENTS (NFRs)

| ID | Category | Requirement |
|---|---|---|
| NFR1 | Performance | Search results en <500ms |
| NFR2 | Scalability | Support 1000 snippets min |
| NFR3 | Security | Auth simple (email/password), pas de 2FA MVP |
| NFR4 | Maintainability | Code couvert >70% tests |

### 5. USER INTERFACE ELEMENTS (UX/UI Notes)
- Searchbar central (Google-like)
- Syntax highlighting (Prism.js)
- Inline code editor for preview
- Share buttons (copy link, email)

### 6. ASSUMPTIONS & DEPENDENCIES
- **Assumption** : Users ont déjà des snippets = adoption rapide
- **Dependency** : Database (simple, SQLite ok MVP)
- **Dependency** : Code highlighting library (Prism.js)
- **Out of Scope** : Auth avancée, audit logs

### 7. GLOSSARY
- **Snippet** : Bloc de code réutilisable avec metadata
- **Tag** : Label pour catégoriser (ex: "jwt", "validation")
- **Visibility** : Scope de partage (private/team/public)
```

**Responsable** : Toi + Claude  
**Durée** : 20-30 min brainstorm + 15 min formatage  
**Output** : 1 document Markdown ~1000 words

---

## PHASE 3 : DESIGN (Convergence Technique)

### Objectif
Transformer le PRD en **SRD (Software Requirements Document)** : quoi construire techniquement.

### Protocole

```
PROMPT TEMPLATE :

"Sur base du PRD précédent, je vais maintenant en PHASE DE DESIGN technique.

Aide-moi à construire un SRD qui couvre :

1) ARCHITECTURE OVERVIEW
   → Quels composants ? (Frontend / Backend / Database)
   → Comment ils communiquent ? (API REST, GraphQL, etc.)
   → Diagrammes simples (TextUML ou ASCII art ok)

2) DATA MODEL
   → Schéma des tables / collections
   → Relations clés
   → Constraints (NOT NULL, UNIQUE, FK)

3) API SPECIFICATION
   → Pour chaque endpoint : Méthode, Route, Req/Res
   → Exemples concrets
   → Error handling

4) TECHNICAL CONSTRAINTS & TRADE-OFFS
   → Pourquoi cette stack vs alternatives ?
   → Qu'est-ce qu'on sacrifice pour la simplicité ?
   → (Cf. N1/N2/N3 sovereignty : qu'est-ce qu'on contrôle vs cloud ?)

À la fin, fournis-moi un SRD qui peut être directement donné à Claude Code
pour commencer le coding sans questions supplémentaires."
```

### Artefacts à produire

#### **3.1 — SYSTEM REQUIREMENTS DOCUMENT (SRD)**

```markdown
# SYSTEM REQUIREMENTS DOCUMENT (SRD)
## Snippet Manager - Technical Specification

### 1. TECHNOLOGY STACK
- **Frontend** : React 18 + TypeScript (UI interactive)
- **Backend** : Node.js + Express (API REST)
- **Database** : SQLite (MVP simplicity, no ops overhead)
- **Code Highlighting** : Prism.js (lightweight)
- **Auth** : Simple JWT tokens (no external provider MVP)

### 2. ARCHITECTURE DIAGRAM
```
┌─────────────────────────────────────────────────┐
│                 FRONTEND (React)                 │
│  ┌──────────────┐      ┌────────────────────┐  │
│  │ SearchPage   │      │ SnippetDetail      │  │
│  │ (Discover)   │──→   │ (Preview + Actions)│  │
│  └──────────────┘      └────────────────────┘  │
│         │ HTTP API            ↑ HTTP API         │
└─────────┼──────────────────────┼─────────────────┘
          │                      │
    ┌─────▼──────────────────────▼──────┐
    │    BACKEND API (Node.js/Express)   │
    │ ┌──────────┐  ┌──────────────────┐│
    │ │ /search  │  │ /snippets/:id    ││
    │ │ /create  │  │ /tags            ││
    │ └──────────┘  └──────────────────┘│
    └─────────┬──────────────────────────┘
              │ SQL Queries
    ┌─────────▼──────────────────────────┐
    │    DATABASE (SQLite)               │
    │  Tables: snippets, tags, versions  │
    └────────────────────────────────────┘
```

### 3. DATA MODEL

```sql
-- Core Tables
TABLE snippets (
  id INT PRIMARY KEY AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  code TEXT NOT NULL,
  language VARCHAR(50) NOT NULL,  -- "javascript", "python", etc.
  description TEXT,
  created_by VARCHAR(255) NOT NULL,
  created_at TIMESTAMP,
  updated_at TIMESTAMP,
  visibility ENUM('private', 'team', 'public') DEFAULT 'private'
)

TABLE tags (
  id INT PRIMARY KEY,
  snippet_id INT FK snippets.id,
  tag_name VARCHAR(100) NOT NULL,
  UNIQUE (snippet_id, tag_name)
)

TABLE snippet_versions (
  id INT PRIMARY KEY,
  snippet_id INT FK snippets.id,
  code TEXT NOT NULL,
  changed_by VARCHAR(255),
  changed_at TIMESTAMP,
  change_description TEXT
)
```

### 4. API ENDPOINTS

#### GET /api/search?q=jwt&lang=javascript
**Description** : Full-text search + filters  
**Query Params** :
- `q` (string) : Search query
- `lang` (string, optional) : Filter by language
- `limit` (int, default 10) : Results per page

**Response** :
```json
{
  "total": 5,
  "results": [
    {
      "id": 1,
      "title": "JWT Validation",
      "code": "const verify = (token) => {...}",
      "language": "javascript",
      "tags": ["jwt", "validation"],
      "created_by": "alice",
      "created_at": "2024-05-11"
    }
  ]
}
```

**Status Codes** :
- 200 OK
- 400 Bad Request (invalid query)

#### POST /api/snippets
**Description** : Create a new snippet  
**Request** :
```json
{
  "title": "JWT Validation",
  "code": "const verify = (token) => {...}",
  "language": "javascript",
  "description": "Validates JWT tokens in Express middleware",
  "tags": ["jwt", "validation"],
  "visibility": "team"
}
```

**Response** :
```json
{
  "id": 1,
  "message": "Snippet created",
  "url": "/snippets/1"
}
```

**Status Codes** :
- 201 Created
- 400 Bad Request (missing fields)
- 401 Unauthorized

#### GET /api/snippets/:id
**Response** : Full snippet + history

#### PATCH /api/snippets/:id
**Updates snippet, auto-versions**

#### DELETE /api/snippets/:id
**Soft delete or hard ?** → [Decision here]

### 5. NON-FUNCTIONAL SPECIFICATIONS

| Requirement | Target | Measurement |
|---|---|---|
| Search Latency | <500ms | p95 on prod |
| Uptime | 99.5% | Monthly |
| Max Concurrent Users | 100 | Load test baseline |
| DB Backup | Daily | Automated cron |
| Code Coverage | >70% | Jest reports |

### 6. SECURITY & AUTH

- **Simple Auth** : Username/password → JWT token (not OAuth MVP)
- **CORS** : Allow from whitelist only
- **SQL Injection** : Use parameterized queries (all ORM/prepared statements)
- **Rate Limiting** : 100 requests/min per IP

### 7. DEPLOYMENT

- **Local Dev** : `npm install && npm run dev` (Vite)
- **MVP Hosting** : Vercel (frontend) + Railway (backend)
- **Database** : SQLite file → backed up to GitHub
- **CI/CD** : GitHub Actions (run tests, deploy on push)

### 8. TECHNICAL DECISIONS & TRADE-OFFS

**Decision 1** : SQLite vs PostgreSQL  
→ **Choice** : SQLite  
→ **Reason** : Zero ops overhead, fine for <1000 snippets  
→ **Sacrifice** : Can't easily share DB across services later

**Decision 2** : REST vs GraphQL  
→ **Choice** : REST  
→ **Reason** : Simpler, smaller bundle, easier to cache  
→ **Sacrifice** : Over-fetching on large snippet lists

**Decision 3** : JWT vs Sessions  
→ **Choice** : JWT  
→ **Reason** : Stateless, easy to scale  
→ **Sacrifice** : Token revocation is harder

### 9. GLOSSARY

- **Snippet** : Reusable code block with metadata
- **Visibility** : Access control (private = self, team = org, public = anyone)
- **Language** : Programming language (javascript, python, etc.)
- **Tag** : Free-form label for categorization
```

**Responsable** : Toi + Claude  
**Durée** : 30 min brainstorm + 20 min formatage  
**Output** : 1 document Markdown ~2000 words

---

## PHASE 4 : DESIGN REVIEW (Cross-check)

### Objectif
**Valider la cohérence** : PRD ↔ SRD ↔ Real-world constraints

### Checklist de Review

```
PROMPT TEMPLATE :

"Je vais maintenant vérifier la cohérence de mon PRD/SRD avant de coder.

Pour chaque élément PRD, donne-moi une vérification rapide :

☐ FR1 (Snippet Storage) → Couverte par API endpoints POST/PATCH/DELETE ? 
   → Validation dans le SRD ? 
   → Données stockées dans le schema ?
   
☐ FR2 (Search) → API GET /search existe ? 
   → Index sur 'language' et 'tags' pour perf ? 
   → Acceptance criteria vérifiable ?

☐ NFR1 (Perf <500ms) → DB query optimisée ? 
   → Pagination implémentée ? 
   → Cache Redis needed ? (MVP: no)

☐ Assumptions → Vrai ? 
   → 'Users ont déjà des snippets' → How we seed data ?
   → Dépendances → All available ?

À la fin : donne-moi une CHECKLIST CODAGE avec les todos prioritaires."
```

### Artefacts à produire

#### **4.1 — DEVELOPMENT CHECKLIST** (README pour Claude Code)

```markdown
# DEVELOPMENT CHECKLIST
## Snippet Manager v1.0 - Ready for Coding

### PHASE 4.1 : DATABASE SETUP
- [ ] Initialize SQLite schema (create tables)
- [ ] Add indexes on language, tags for search perf
- [ ] Seed test data (5 demo snippets)
- [ ] Test DB connection

### PHASE 4.2 : BACKEND API
- [ ] Setup Express app + middleware (CORS, body-parser)
- [ ] Auth: Implement JWT generation (register/login)
- [ ] Endpoint: POST /api/snippets (create)
- [ ] Endpoint: GET /api/search (search + filter)
- [ ] Endpoint: GET /api/snippets/:id (detail)
- [ ] Endpoint: PATCH /api/snippets/:id (update + auto-version)
- [ ] Endpoint: DELETE /api/snippets/:id (delete)
- [ ] Error handling: Consistent JSON errors
- [ ] Unit tests: >70% coverage on API layer

### PHASE 4.3 : FRONTEND UI
- [ ] Layout: Header + SearchBar + Results
- [ ] SearchPage: Input + Results list + Filters (language dropdown)
- [ ] SnippetDetail: Code viewer + Syntax highlighting + Actions
- [ ] CreateModal: Form for title/code/lang/tags/visibility
- [ ] EditFlow: Allow modify + auto-save
- [ ] Copy-to-Clipboard button + toast notification
- [ ] Responsive design (mobile + desktop)
- [ ] Error boundaries & loading states

### PHASE 4.4 : INTEGRATION & POLISH
- [ ] Connect frontend → backend (HTTP calls)
- [ ] Auth flow: Register → Login → Token in localStorage
- [ ] E2E test: Create snippet → Search → Copy flow
- [ ] Performance: Measure search latency
- [ ] Security: Review CORS, SQL injection, auth
- [ ] Deployment: Push to Vercel + Railway

### BLOCKERS / DECISIONS TO MAKE DURING CODING
- [ ] Soft delete vs hard delete for snippets ?
- [ ] User profile pages ? (MVP: No)
- [ ] Dark mode ? (MVP: No, light only)
- [ ] Keyboard shortcuts ? (MVP: No)
```

**Responsable** : Toi (review), Claude (validation)  
**Durée** : 5 min checklist + 10 min review  
**Output** : 1 document Markdown

---

## PHASE 5 : DELIVER (Coding avec Claude Code)

### Prompt Template pour Claude Code

```
SITUATION :
Je suis en phase DELIVER d'un projet informatique.
J'ai préparé PRD + SRD + Checklist en amont.
Objectif : Minimiser aller-retours, coder d'une traite.

CONTEXTE PROJET :
- Name: Snippet Manager v1.0
- Stack: React + Node.js + SQLite
- Timeframe: 2 sessions max (~2-3h total coding)
- Success: Deploy-ready MVP, 0 ambiguity

ARTEFACTS FOURNIS (ci-dessous) :
[Colle le contenu complet du PRD]
[Colle le contenu complet du SRD]
[Colle le contenu du CHECKLIST]

TA MISSION :
Construis le projet EN ENTIER en une session.
- Structure le code proprement (frontend/backend séparés)
- Inclus les tests minimaux
- Fournisci des instructions de déploiement claires
- Si ambiguité : référence-toi au PRD/SRD, ne me demande pas

LIVRABLES ATTENDUS :
1. Backend: server.js + routes + DB schema
2. Frontend: App.jsx + components (Search, Detail, Create)
3. Package.json + .env.example
4. README.md avec setup & run instructions
5. Déploiement : instructions Vercel + Railway
```

---

## PHASE 6 : LIVE (Launch & Metrics)

### Artefacts Post-Launch

#### **6.1 — IMPACT REVIEW** (1 semaine after launch)

```
PROMPT POUR RETROSPECTIVE :

"1 semaine après le déploiement. Revenons au PRD original.

Success Metrics étaient :
- 80% des devs l'utilisent 1x/semaine
- Retrouver snippet en <10 sec
- 0 bugs causés par snippets moisis

Actuel (données/feedback) :
- [Adoption %]
- [Avg search time]
- [Bug reports]

Quels problèmes non anticipés ? → Go/No-Go Phase 2 ?"
```

---

## 🎯 TEMPLATE RÉSUMÉ (À UTILISER POUR CHAQUE PROJET)

### Session 0: Charter (15 min)
→ **Output** : PROJECT_CHARTER.txt

### Session 1: Discovery (40 min)
→ **Outputs** : PROBLEM_ANALYSIS.md, OPPORTUNITY_MAP.md

### Session 2: Define (50 min)
→ **Outputs** : SCOPE_STATEMENT.md, **PRD.md**

### Session 3: Design (50 min)
→ **Output** : **SRD.md**

### Session 4: Review (15 min)
→ **Output** : DEVELOPMENT_CHECKLIST.md

### Session 5: Deliver (120+ min)
→ **Output** : Full code repo + README + Deploy instructions

### Session 6: Live (Async, 1 week later)
→ **Output** : IMPACT_REVIEW.md

---

## 🚀 OPTIMISATIONS POUR ÉCONOMISER LES TOKENS

1. **Réutilise les docs PRD/SRD verbatim dans la session Code**
   → Pas de reformulation = pas de tokens perdus

2. **Breakdown par composant, pas par feature**
   → "Construis SearchBar" vs "Construis search feature"
   → Moins de contexte, output plus focalisé

3. **Utilise le checklist comme scaffold**
   → Claude Code sait exactement quoi faire, dans quel ordre
   → Moins d'incertitude = moins de questions

4. **One-shot coding par composant**
   → "Ici est le SRD. Voici la checklist. Code backend entier maintenant."
   → Pas de multi-turn brainstorm, un output par composant

5. **Test d'abord pour valider la spec**
   → Tests = proof que spec était claire
   → Moins de "attend, c'est quoi le comportement exact ?"

---

## 💾 GESTION DES FICHIERS

Garde une structure ainsi :

```
my-project/
├── 00-CHARTER.txt              ← Project source of truth
├── 01-PROBLEM-ANALYSIS.md
├── 02-OPPORTUNITY-MAP.md
├── 03-SCOPE-STATEMENT.md
├── 04-PRD.md                   ← Master doc (reused in coding)
├── 05-SRD.md                   ← Master doc (reused in coding)
├── 06-DEVELOPMENT-CHECKLIST.md
├── src/
│   ├── backend/
│   ├── frontend/
│   └── shared/
├── tests/
├── README.md
└── .env.example
```

**Pro tip** : Tout ce qui est "master" (PRD, SRD, Checklist) va dans le README du projet. Claude Code peut les relire pendant le coding.

---

## SUMMARY

Ce protocole économise **40-50% des tokens** en:
1. Clarifiant upfront (moins de "mais c'est quoi vraiment ?")
2. Réutilisant les docs (pas de rewrite)
3. Structurant le code (moins de refactor)
4. Validant la spec avant coding (moins d'aller-retour)

**Résultat** : Specs → Code sans friction.
