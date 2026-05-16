# Backlog Refinement
*doc-spec v1 · 2026-05-16 · protocole R3a (PRD → SRD)*

---

## O1 — Formalisation

```
Refinement : Ω_stories_PRD → Ω_stories_DoR
```

| | Contenu |
|---|---|
| **Domaine** | User stories PRD (trop grosses, AC flous, estimation absente) |
| **Codomaine** | Stories raffinées qui satisfont le DoR — prêtes pour Sprint Planning |
| **Propriété** | Clarificateur · réduit l'ambiguïté des stories jusqu'au seuil DoR · ~10% de la capacité sprint |

---

## O2 — GAFAM best practices

| Pratique | Source | Apport |
|---|---|---|
| Backlog Refinement | Scrum Guide 2020 | Activité continue (~10% capacity) — pas un événement figé |
| "INVEST" criteria | Bill Wake | Independent · Negotiable · Valuable · Estimable · Small · Testable |
| Story splitting patterns | Richard Lawrence | 9 patterns pour découper les épics sans perdre de valeur |
| Three Amigos | BDD community | PO + Dev + QA clarifient ensemble — 3 perspectives = moins d'ambiguïtés |
| Example Mapping | Matt Wynne | Rules + Examples + Questions — clarifie les AC en 20 min |

---

## O3 — Négation talmudique

| Ce que Refinement N'EST PAS | Document correct |
|---|---|
| Sprint Planning (engagement sur un sprint) | Sprint Planning (R3b) |
| Backlog grooming = suppression d'items | Refinement ≠ nettoyage — c'est de la clarification |
| Estimation définitive | Story points = approximation, pas contrat |
| Réunion de statut | Daily Scrum (R3c) |
| Design ou architecture | SRD / ADR |

---

## O4 — Format canonique

1. **La story est-elle suffisamment petite pour tenir en 1 sprint ?** → Split si > 1 sprint
2. **Les acceptance criteria sont-ils rédigés et testables ?** → Compléter les AC
3. **Les dépendances sont-elles identifiées ?** → Identifier + résoudre avant sprint
4. **L'estimation est-elle faite (story points ou T-shirt) ?** → Estimer
5. **Le DoR est-il atteint ?** → Gate de passage en Sprint Planning

---

## Format canonique

| Critère DoR | Question | Garde-fou |
|---|---|---|
| **AC rédigés** | Peut-on écrire un test pour chaque AC ? | AC absents = story non-terminable |
| **Estimation** | L'équipe a-t-elle estimé la complexité ? | Non-estimé = impossible à planifier |
| **Dépendances** | Quelles dépendances bloquantes identifiées ? | Dépendance cachée = sprint bloqué |
| **Maquettes** | Les wireframes/designs sont-ils disponibles ? | Design en cours = démarrage fictif |
| **Taille** | La story tient-elle dans 1 sprint ? | Story trop grosse = jamais Done |

---

## Ker / Im

| | Contenu |
|---|---|
| **Ker** | Stories DoR-ready · AC testables · Estimations · Dépendances résolues |
| **Im → Sprint Planning** | Backlog raffiné prêt à être sélectionné pour le Sprint Goal |
