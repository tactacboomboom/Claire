# Sprint Planning
*doc-spec v1 · 2026-05-16 · protocole R3b (PRD → SRD)*

---

## O1 — Formalisation

```
SprintPlanning : Ω_backlog_raffiné → Ω_sprint_goal + sprint_backlog
```

| | Contenu |
|---|---|
| **Domaine** | Product Backlog raffiné (stories DoR-ready) + vélocité de l'équipe |
| **Codomaine** | Sprint Goal (engagement collectif) + Sprint Backlog (tasks décomposées) |
| **Propriété** | Planificateur · sélectionne et décompose les stories qui maximisent la valeur du Sprint Goal · Timebox : 8h (sprint 1 mois) |

---

## O2 — GAFAM best practices

| Pratique | Source | Apport |
|---|---|---|
| Sprint Planning (2 parties) | Scrum Guide 2020 | Partie 1 (PO+Dev) : Sprint Goal · Partie 2 (Dev) : décomposition en tasks |
| Sprint Goal obligatoire | Scrum Guide 2020 | Goal first — les stories sont en support du Goal, pas l'inverse |
| Vélocité + capacité | Scrum standard | Sélection basée sur la vélocité historique corrigée de la capacité réelle |
| "What" vs "How" | Scrum Guide | Partie 1 = WHAT (stories) · Partie 2 = HOW (tasks techniques) |
| Definition of Ready gate | Scrum community | Story non-DoR = refus en Sprint Planning |

---

## O3 — Négation talmudique

| Ce que Sprint Planning N'EST PAS | Document correct |
|---|---|
| Backlog Refinement (clarification des AC) | Backlog Refinement (R3a) |
| Assignation individuelle des tâches | L'équipe s'auto-organise — pas de micro-management |
| Contrat immuable | Sprint Goal peut évoluer si contexte change radicalement |
| Réunion de planification projet long terme | BRD Release Roadmap |
| Estimation de la vélocité future | Vélocité = passé, pas prédiction |

---

## O4 — Format canonique

1. **Quel Sprint Goal unique exprime la valeur de ce sprint ?** → Sprint Goal (1 phrase)
2. **Quelles stories du backlog servent ce Goal (dans la vélocité) ?** → Stories sélectionnées
3. **Comment décomposer chaque story en tâches ≤ 1 jour ?** → Tasks techniques
4. **L'équipe peut-elle s'engager sur ce Sprint Backlog ?** → Confirmation capacité

---

## Format canonique

| Phase | Participants | Timebox | Output |
|---|---|---|---|
| **Partie 1 — WHAT** | Scrum Team + PO | 4h | Sprint Goal + stories sélectionnées |
| **Partie 2 — HOW** | Developers (PO optionnel) | 4h | Sprint Backlog (tasks décomposées) |

| Critère | Règle | Garde-fou |
|---|---|---|
| **Sprint Goal** | 1 phrase — exprime la valeur, pas la liste de features | Sprint Goal = liste de stories = pas un Goal |
| **Vélocité** | Capacité réelle = vélocité historique × (jours dispo / jours normaux) | Sur-engagement = sprint fail systématique |
| **DoR** | Story non-DoR refusée — pas en Sprint Backlog | Accepter non-DoR = engagement fictif |

---

## Ker / Im

| | Contenu |
|---|---|
| **Ker** | Sprint Goal · Sprint Backlog · Engagement collectif |
| **Im → Daily Scrum** | Référence commune pour évaluer la progression quotidienne |
| **Im → SRD** | Tasks techniques décomposées = artefacts SRD exécutables |
