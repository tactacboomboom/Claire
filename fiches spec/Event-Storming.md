# Event Storming — Domain Discovery Workshop
*doc-spec v1 · 2026-05-16 · pipeline: fmaths + GAFAM + négation talmudique + formulaire science*

---

## O1 — Formalisation

```
EventStorming : Ω_domaine → Ω_langage_ubiquitaire
```

| | Contenu |
|---|---|
| **Domaine Ω_domaine** | Processus métier complexes, règles implicites, expertise distribuée dans les têtes des participants |
| **Codomaine Ω_langage_ubiquitaire** | Bounded contexts + aggregates + domain events + langage partagé entre dev et métier |
| **Propriété** | Découvreur · révèle les connaissances tacites du domaine par socialisation collaborative — output non-reproductible sans les participants |

---

## O2 — GAFAM best practices

| Pratique | Source | Apport |
|---|---|---|
| Event Storming (Big Picture) | Alberto Brandolini (2012+) | Exploration libre du domaine entier — orange stickies = domain events |
| Event Storming (Process Level) | Brandolini | Zoom sur un sous-domaine — découvre les process flows et politiques |
| Context Mapping | Eric Evans / DDD | Délimite les bounded contexts depuis l'event storm |
| Domain Storytelling | Hofer / Schwentner | Alternative narrative — acteurs + activités + objets de travail |
| Example Mapping | Matt Wynne / Cucumber | BDD depuis les domain events — rules + examples + questions |

---

## O3 — Négation talmudique

| Ce que Event Storming N'EST PAS | Document correct |
|---|---|
| User Story Mapping (orienté tâches utilisateur) | USM (Jeff Patton) |
| Processus métier formalisé et exhaustif | BPMN |
| Diagramme technique ou architecture | SRD / C4 Model |
| Spec produit avec acceptance criteria | PRD |
| Document écrit — c'est un atelier, l'output est un mur de stickies + bounded contexts | Wiki / Notion post-atelier |

---

## O4 — Formulaire science (ordre cognitif)

> Du chaos vers la structure. Chaque phase réduit l'ambiguïté du domaine.

1. **Quels événements domaine se produisent dans le système (formule : passé simple) ?** → Domain Events (orange)
2. **Quelles commandes déclenchent ces événements (formule : impératif) ?** → Commands (bleu)
3. **Qui ou quoi émet ces commandes ?** → Actors (jaune clair) + External Systems (rose)
4. **Quelles règles / politiques s'appliquent entre command et event ?** → Policies (lilas)
5. **Quels agrégats coordonnent events + commands ?** → Aggregates (jaune)
6. **Où les bounded contexts se délimitent-ils (lignes de friction) ?** → Bounded Contexts

---

## Sommaire canonique (format atelier)

| Phase | Question structurante | Garde-fou |
|---|---|---|
| **Domain Events** | Qu'est-ce qui se passe dans le domaine ? (passé simple) | Events formulés au présent = trop vague |
| **Commands** | Qu'est-ce qui déclenche chaque event ? | Command sans actor = orphelin |
| **Actors & Systems** | Qui ou quoi émet cette command ? | Actor non-nommé = ambiguïté métier |
| **Policies** | Quelle règle métier relie command et event ? | Politique implicite = dette de connaissance |
| **Aggregates** | Quel nœud de cohérence groupe ces events ? | Aggregate trop gros = God Object |
| **Bounded Contexts** | Où le langage change-t-il de sens ? | Pas de frontières = Big Ball of Mud |

---

## Ker / Im

| | Contenu |
|---|---|
| **Ker** (reste dans Event Storming) | Domain events nommés · Politiques métier · Hotspots (zones d'ambiguïté) · Langage ubiquitaire |
| **Im → BRD / PRD** | Bounded contexts délimités · Aggregates candidats · Sous-domaines core vs support vs generic |
| **Position dans la chaîne** | Protocole de R2 (BRD → PRD) — précède la définition des features PRD dans les domaines complexes |
