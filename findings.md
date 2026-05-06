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

### Décision technique : Décodeur fmaths appliqué au projet

Le pipeline next.js = DAG invariant. Ce qui change d'un projet à l'autre = uniquement 📱 → ⚙️ → 🧠.
Le 🪨 🚚 🗄️ 🎯 = infrastructure invariante. On installe, on oublie.
𝕽 (PWF) correspond au cross-cutting ⊕ IAM+ORCHESTRATION — il conditionne μₙ et εₙ sans être dans le flux de données.
