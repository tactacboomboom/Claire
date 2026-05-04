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
