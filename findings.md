# Findings & Decisions — Claire repo

## 🎯 Requirements & Contraintes
- 0€ de dépense (Vercel Hobby + GitHub gratuit)
- Repo public, autonome, compréhensible sans l'auteur
- Style de référence : OthmanAdi/planning-with-files (20k stars)
- Sources locales : `vault/protocole/CPE/sources/clear-sky/` + `saas-traduction/`

## 🔍 Research Findings

### Structure PWF de référence (OthmanAdi)
- Dossiers : commands/, docs/, examples/, scripts/, skills/, templates/
- README très court → renvoie vers docs/
- Multi-IDE (17+ environnements supportés)
- Multi-langue (6 langues)
- Installable via `npx skills add`

### Contenu CPE disponible en local
| Fichier source | Contenu |
| :--- | :--- |
| `clear-sky/000_CANONICAL_PIPELINE_EQUATION.md` | Équation complète, objets, opérateurs, invariants |
| `saas-traduction/ITEM 1 — GOAL.md` | Format GOAL formalisé |
| `saas-traduction/ITEM 2 - SPRINT BACKLOG.md` | Backlog B1/B2/B3 |
| `saas-traduction/ITEM 3 - DEFINITION OF DONE.md` | DoD D1-D5 |
| `saas-traduction/ALGORITHME DE SCROING.md` | Scoring μA / μV |
| `saas-traduction/1 - task_plan.md (ACTION).md` | Template task_plan |
| `saas-traduction/2 - findings.md (APPRENTISSAGE).md` | Template findings |
| `saas-traduction/3 - progress.md (PREUVE).md` | Template progress |

### Objets CPE (liste complète)
| Symbole | Nom | Équivalent fichier |
| :--- | :--- | :--- |
| 𝕀₀ | Intention brute | — |
| 𝕮ₙ | Contrat sprint | task_plan.md |
| 𝕋ᴳ | Attracteur global | Vision du projet |
| 𝕋ₙ | Attracteur sprint | Vision du sprint |
| Δ₀ | Capteur dérives | Anti-pathologies |
| 𝕽 | Référentiel invariant | PWF (les 3 fichiers) |
| 𝕍 | Validateur contrat | Gate scoring |
| 𝕊ₙ | Sprint | Exécution |
| 𝕡ₙ | Produit | Artefact livrable |
| 𝔸ₙ | Archive | findings.md + progress.md |
| 𝕄ₙ | Sprint Memory | Mémoire distillée |

### Opérateurs CPE
| Symbole | Input | Output |
| :--- | :--- | :--- |
| φ₀ | 𝕀₀ | (𝕮₀, 𝕋ᴳ, Δ₀) |
| μₙ | (𝕮ₙ, 𝕄ₙ₋₁, 𝕡ₙ₋₁, 𝕋ᴳ, 𝕋ₙ, Δ₀ \| 𝕽) | 𝕊ₙ |
| εₙ | (𝕊ₙ \| 𝕽) | (𝕡ₙ, 𝔸ₙ) |
| τₙ | (𝔸ₙ, 𝕡ₙ, 𝕋ₙ) | 𝕄ₙ |
| κₙ | (𝕮ₙ, 𝔸ₙ, 𝕄ₙ, 𝕋ᴳ) | (𝕮ₙ₊₁, 𝕋ₙ₊₁) |

## 🛠 Décisions Techniques
| Décision | Rationnel |
| :--- | :--- |
| Mermaid pour les schémas | Natif GitHub, pas de dépendance externe |
| Anglais pour docs/ | Standard open source, cohérence avec PWF |
| Scoring μA/μV inclus | C'est le différenciateur fort vs Scrum classique |

## ⚠️ Issues & Blocages
| Problème | Résolution |
| :--- | :--- |
| gh CLI non installé | Utiliser git + remote add origin manuellement |

## 🖼 Observations
- Le schéma Mermaid validé par l'auteur (2026-05-04)
- La boucle κₙ → 𝕮ₙ₊₁ est le cœur différenciateur (continuité entre sprints)

---

## Session 2026-05-06 — Formalisation DAG + SOLID

### Vocabulaire invariant DAG (emojis réutilisables)

| Emoji | Nœud DAG | Ce que ça désigne |
| :--- | :--- | :--- |
| 📱 | SOURCE | Ce qui entre dans le système (intention, clé API) |
| 🚚 | TRANSPORT | Ce qui déplace sans transformer |
| 🪨 | STORE RAW | Ce qui persiste en forme brute, intouchable |
| ⚙️ | TRANSFORM | Ce qui change la forme |
| 🗄️ | STORE STRUCTURÉ | Ce qui persiste en forme organisée |
| 🎯 | SERVE | Ce qui expose au consommateur final |
| 🧠 | CONSUME | Ce qui reçoit et utilise |
| 🔑 | IAM | Les secrets, les accès, les identités |
| 🎼 | ORCHESTRATION | Les rituels qui lancent la chaîne |
| 🏗️ | INFRA | Ce qui fait tourner tout ça (cross-cutting) |

### SOLID → DAG (traduction)

| Principe | Règle | Traduction DAG |
| :--- | :--- | :--- |
| S — Single Responsibility | Un fichier = un nœud, pas deux | scoring.ts = ⚙️ uniquement. Pas ⚙️ + 🎯 dans le même fichier |
| O — Open/Closed | Ajouter sans modifier | Ajouter ε₀ ne doit pas toucher φ₀ — deux ⚙️ séparés |
| L — Liskov | Les sous-types sont substituables | Les 5 personas PSPO sont tous des Validator (même contrat) |
| I — Interface Segregation | Petites interfaces ciblées | ScrumMasterValidator n'implémente pas les checks DevValidator |
| D — Dependency Inversion | Dépendre des abstractions | route.ts → LLMProvider (interface), pas directement Anthropic SDK |

### Audit claire-app (état au 2026-05-06)

| Fichier | Principe | Status | Détail |
| :--- | :--- | :--- | :--- |
| lib/scoring.ts | S | ✅ | Fait une seule chose |
| lib/types.ts | S | ✅ | Fait une seule chose |
| lib/prompts.ts | S | ✅ | Fait une seule chose |
| app/api/generate/route.ts | S + D | 🔴 | Trop de responsabilités + Anthropic SDK câblé en dur |

### Architecture cible Sprint 2

    📱  SOURCE          → route.ts (orchestration seule)
          ↓
    ⚙️  φ₀             → lib/generate.ts (appel LLM abstrait)
          ↓
    ⚙️  𝕍              → lib/scoring.ts (déjà propre ✅)
          ↓
    ⚙️  ε₀             → lib/diagnostics.ts (nouveau — extension O)
          ↓
    ⚙️  κ₀             → lib/refine.ts (nouveau — extension O)
          ↓
    🎯  SERVE           → route.ts (response uniquement)

    ⊕  🔑  lib/llm.ts       → interface LLMProvider  (D — abstraire le SDK)
    ⊕  🎼  lib/personas/    → un fichier par persona PSPO (L + I)

### Décision technique : Décodeur fmaths appliqué au projet (session 2026-05-06)

Le pipeline next.js = DAG invariant. Ce qui change d'un projet à l'autre = uniquement 📱 → ⚙️ → 🧠.
Le 🪨 🚚 🗄️ 🎯 = infrastructure invariante. On installe, on oublie.
𝕽 (PWF) correspond au cross-cutting ⊕ IAM+ORCHESTRATION — il conditionne μₙ et εₙ sans être dans le flux de données.

---

## Session 2026-05-07 — fmaths × POO × Design Patterns

### fmaths appliqué : POO — ensemble minimal fermé

**Résultat** : {Classe, Objet, Méthode, Interface} est FERMÉ et GÉNÉRATEUR.

| Primitif | Irréductible ? |
| :--- | :--- |
| Classe | ✅ — sans elle, aucun Objet ne naît |
| Objet | ✅ — sans lui, la Classe est vide |
| Méthode | ✅ — sans elle, les Objets sont inertes |
| Interface | ⚠️ — sous-cas de Classe, mais sémantique distincte |

Tout le reste est dérivé : Attribut = Méthode triviale, Héritage = morphisme entre Classes, Polymorphisme = Méthode sur Interface, etc.

DTO / VO / Entity / DAO = **couche secondaire** (spécialisations de Objet selon axe identité + axe rôle) — pas de nouveaux primitifs.

### fmaths appliqué : Design Patterns — 3 familles exhaustives

| Famille | Question couverte | Nb GoF | Nb essentiels |
| :--- | :--- | :--- | :--- |
| Création | Comment naissent les objets ? | 5 | 3 |
| Structure | Comment sont-ils assemblés ? | 7 | 5 |
| Comportement | Comment interagissent-ils ? | 11 | 6 |

**14 essentiels** : Factory Method, Builder, Singleton / Adapter, Decorator, Facade, Proxy, Composite / Observer, Strategy, Template Method, Command, State, Iterator

Pas de 4ème famille possible — Concurrence = runtime, Persistance = infrastructure, Méta-programmation = mécanisme du langage.

### Vault — Artifacts créés

| Fichier | Type |
| :--- | :--- |
| `vault/1 - CONVERSATIONS/poo-design-patterns-fmaths/raw.md` | Analyse fmaths complète (Passe 1 + Passe 2) |
| `vault/2 - CONCEPTS/ontologie-poo-minimale.md` | Concept — preuve de fermeture de l'ontologie POO |
| `vault/2 - CONCEPTS/design-patterns-essentiels.md` | Concept — 14 patterns essentiels + fermeture |
| `vault/REF/tags.md` | Ajout : `ontologie_poo_minimale` + `design_patterns_essentiels` dans #STRUCT |

---

## Session 2026-05-16 — Sprint S2 Kahn-0 + Taxonomie nommage

### Sprint S2 — État (A0.1 + A0.2 validés)

| Action | Résultat |
| :--- | :--- |
| `git push origin feat/atlas-concepts` | GitHub à jour — commit `1be02f2` ✅ |
| `git clone → C:\projects\claire` | Claire hors Drive, sur `feat/atlas-concepts` ✅ |
| `.gitignore` créé | `app/`, `app-temp/`, `*.local` exclus du repo Claire ✅ |
| `math_atlas_narrative.html` × 4 → 1 | Canonique : `vault/5 - OUTILS/` ✅ |
| `mindmap-atlas-50-theoremes.html` × 2 → 1 | Canonique : `vault/5 - OUTILS/` ✅ |

### Taxonomie nommage — à valider par Yanis

**Types d'artefacts**

| Type | Convention | Exemples |
| :--- | :--- | :--- |
| Skill | `verb-noun` kebab | `geo`, `cpe-sprint` |
| Concept | `noun-noun` kebab | `nilpotence-cognitive`, `kahn-dag` |
| Config | UPPER_CASE | `CLAUDE.md`, `settings.json` |
| Memory | `type_slug.md` | `project_atlas.md`, `user_profile.md` |
| Template | `noun.md` | `task_plan.md`, `sprint-contract.md` |
| Dashboard | `noun.html` | `ecosystem.html` |

**Couches DDD → nœuds DAG**

| DDD Layer | Nœud DAG | Chemin |
| :--- | :--- | :--- |
| Domain | vault/2-CONCEPTS | Théorèmes, méthodes, concepts purs |
| Application | ~/.claude/skills/ | Skills invocables par Claude Code |
| Infrastructure | my-claude-config (GitHub) | CLAUDE.md, settings.json, hooks |
| Presentation | ecosystem.html, claire-app | UX, dashboards, API |

**SOLID appliqué aux skills**

| Principe | Règle |
| :--- | :--- |
| S | 1 SKILL.md = 1 responsabilité (geo = garde-fou SEULEMENT) |
| O | Nouveau besoin → nouveau SKILL.md, jamais modifier l'existant |
| L | Interface obligatoire : `name / description / type / input / output / allowed-tools` |
| I | `allowed-tools:` limité au strict nécessaire — jamais `*` |
| D | Skills dépendent de l'API Claude abstraite, pas d'un outil concret |

### OOP appliqué à la structure de fichiers

| Concept OOP | Traduction fichier |
| :--- | :--- |
| Classe | SKILL.md (contrat + interface) |
| Objet | Instance d'un skill invoqué dans une session |
| Méthode | Section du SKILL.md (protocole d'exécution) |
| Interface | Frontmatter obligatoire (name/description/type/input/output) |
| Héritage | skill B @extends skill A (import partiel) |
| Encapsulation | `allowed-tools:` = surface exposée seulement |

---

## Session 2026-05-16 — Sprint S5 : Audit repos gouvernance

### /fmath appliqué — 3 repos

#### 1. obra/superpowers — Analyse fmaths

**Ensemble minimal irréductible :**
| Primitif | Rôle | Irréductible ? |
| :--- | :--- | :--- |
| SKILL.md | Contrat d'un comportement | ✅ |
| Workflow | Séquence spec→plan→exécute | ✅ |
| Subagent | Isolant d'exécution autonome | ✅ |
| TDD cycle | Feedback loop RED→GREEN→REFACTOR | ✅ |

**Fermeture** : {skill + workflow + subagent + TDD} génère la totalité du dev cycle. Rien ne manque, rien n'est superflu.

**Tensions identifiées :**
- Spec-first ↔ autonomie subagent → résolu par brainstorming itératif (approbation humaine avant worktree)
- Flexibilité ↔ conformité → résolu par "check skills before task" (Δ₀ automatique)

**Topologie :** cascade linéaire stricte — brain → plan → worktree → subagent → test → review. Pas de boucle implicite.

**Invariant clé :** "The agent checks for relevant skills before any task" = Δ₀ appliqué automatiquement. Absent dans mes sessions actuelles → violation I3 répétée.

---

#### 2. thedotmack/claude-mem — Analyse fmaths

**Ensemble minimal irréductible :**
| Primitif | Rôle | Irréductible ? |
| :--- | :--- | :--- |
| Observation | Capture brute d'une action | ✅ |
| Summary | Compression sémantique | ✅ |
| Retrieval | Injection contextuelle ciblée | ✅ |
| Hook lifecycle | Déclenchement automatique | ✅ |

**Fermeture** : {observation + summary + retrieval + hooks} = couverture complète de la continuité mémoire inter-sessions.

**Tensions identifiées :**
- Complétude mémoire ↔ coût token → résolu par progressive disclosure 3 couches (index 50-100t → timeline → details 500-1000t/filtre)
- Automatisme ↔ privacy → résolu par `<private>` tags

**Topologie :** DAG : SessionStart → UserPromptSubmit → PostToolUse → Stop → compression → SQLite + Chroma → retrieval MCP → injection. Plus puissant que le hook actuel (~/.claude/settings.json qui lit seulement MEMORY.md).

**Invariant clé :** T009 Shannon appliqué à la mémoire — compression maximale sans perte sémantique. 10x token savings mesuré.

---

#### 3. safishamsi/graphify — Analyse fmaths

**Ensemble minimal irréductible :**
| Primitif | Rôle | Irréductible ? |
| :--- | :--- | :--- |
| Node | Concept extrait | ✅ |
| Edge (EXTRACTED/INFERRED/AMBIGUOUS) | Relation typée | ✅ |
| Cluster (Leiden) | Cohérence thématique | ✅ |
| God-node | Concept haute-densité (hub) | ⚠️ dérivé mais analytiquement distinct |

**Fermeture** : {node + edge + cluster} couvre toute structure de connaissance. God-node = propriété émergente, pas primitif.

**Tensions identifiées :**
- Freshness du graphe ↔ coût recalcul → résolu par cache SHA256 + --update incrémental
- Navigation libre ↔ structure imposée → résolu par modes query/path/explain + wiki

**Topologie :** fichiers disparates → extraction multimodale (AST + vision + NLP) → graphe NetworkX → Leiden clustering → sorties (html/json/obsidian/wiki). Post-commit git hook pour sync automatique.

**Invariant clé :** 71.5x réduction tokens = T009 Shannon. vault/2-CONCEPTS (49 fichiers) → graphe → navigation directe par concept sans lire 49 fichiers.

---

### Matrice gouvernance — repos × problèmes Yanis

| Problème Yanis | BN/Invariant | superpowers | claude-mem | graphify |
| :--- | :--- | :--- | :--- | :--- |
| CLAUDE.md 275L → mauvais nœud | BN1 / I1 | ✅ SKILL.md = 1 responsabilité | — | — |
| Skills orphelins sans arc | BN2 / I1 | ✅ install marketplace = arc auto | ✅ npx install = arc auto | ✅ pip install = arc auto |
| WIP > 3 simultanément | I2 | ✅ worktree = isolation WIP | ✅ sessions séparées tracées | — |
| Spec manquante avant code | I3 | ✅✅ brainstorm→writing-plans | — | — |
| Drive/memory jamais chargée | BN4 / I1 | — | ✅✅ injection auto SessionStart | ✅ vault indexé = retrieval rapide |
| Contamination inter-cerveaux | I4 | ✅ worktree = isolation physique | ✅ sessions séparément trackées | ✅ clusters = cerveaux séparables |
| Vault 49 fichiers non navigable | — | — | — | ✅✅ 71.5x réduction |
| "Check skills before task" manquant | I3/Δ₀ | ✅✅ mécanisme natif | — | — |
| Pas de vérification avant déclaration "done" | I3 | ✅ verification-before-completion | — | — |

### Actions recommandées

| Action | Repo source | Priorité | Effort |
| :--- | :--- | :--- | :--- |
| Adopter claude-mem (remplace hook MEMORY.md) | claude-mem | P0 | 30 min |
| Ajouter "check skills before task" dans /geo | superpowers | P1 | 15 min |
| Ajouter "verification-before-completion" dans /geo | superpowers | P1 | 10 min |
| Lancer graphify sur vault/2-CONCEPTS | graphify | P2 | 20 min |
| Enrichir /router : skills recommandés contextuels | superpowers | P2 | 20 min |
| Créer /drift-control (Δ₀ explicite) | superpowers + geo | P3 | 45 min |

---

## Vision système — capturée 2026-05-16

### Trois axes

**Axe 1 — Portabilité inter-machines**
GitHub privé contient tout : CLAUDE.md + settings.json + skills/. Quand une nouvelle machine ouvre Claude Code → hook SessionStart détecte les dépendances manquantes → propose `git clone + install`. Modèle : claude-mem (npx install) + superpowers (marketplace). Nœud : `my-claude-config` (infrastructure privée).

**Axe 2 — Agent de linéage**
Tout artefact créé a un lien de traçabilité vers sa source. Format : `source → transformation → artefact → usage`. Permet de retrouver d'une machine à l'autre : qui a créé quoi, pourquoi, à partir de quoi. Modèle : graphify edges (EXTRACTED / INFERRED / AMBIGUOUS) + god-nodes. Possible skill : /lineage.

**Axe 3 — Gestion de projet par projet (PM Dashboard)**
Chaque projet dans ecosystem.html a son propre panneau : MRD + BRD + PRD + SRD (18 documents) + contrats PWF + métriques μA/μV. Switch entre projets = switch de contexte avec spec complète visible. SOLID strict : 1 projet = 1 panneau = 1 contrat. 

### Pattern cross-projets (à extraire)
Les éléments qui se répètent dans tous les projets de Yanis deviennent des primitifs de rang N4 (irréductibles). Exemples détectés : spec-first (I3), session isolation (I4), PWF 3 fichiers, /geo invariants. Ces primitifs vont dans `~/.claude/` (rang global), les spécificités projet restent dans le CLAUDE.md projet.

### Ordre logique de construction
1. Portabilité (my-claude-config complet + SessionStart hook)
2. Linéage (skill /lineage tracant artefacts → sources)
3. PM Dashboard (ecosystem.html enrichi par projet)
4. Patterns cross-projets (extraire primitifs depuis usage réel)
