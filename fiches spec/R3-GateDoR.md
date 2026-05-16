# Gate DoR — Definition of Ready
*doc-spec v1 · 2026-05-16 · gate R3a → R3b*

---

## O1 — Formalisation

```
DoR : Ω_story_brute → {0, 1}  (prête / non-prête)
```

| | Contenu |
|---|---|
| **Domaine** | Story candidate à entrer en Sprint Planning |
| **Codomaine** | Décision binaire : prête (1) ou non (0) |
| **Propriété** | Gate · décision binaire déterministe — la story passe ou elle retourne en Refinement · co-créé par la Scrum Team, révisé tous les 2-3 sprints |

---

## O2 — GAFAM best practices

| Pratique | Source | Apport |
|---|---|---|
| Definition of Ready | Scrum community (Alistair Cockburn +) | Checklist d'entrée en sprint — évite les engagements fictifs |
| "INVEST" gate | Bill Wake | Critères INVEST comme base du DoR |
| Team-defined DoR | Scrum Guide | Le DoR est co-créé, pas imposé — adapté au contexte de l'équipe |
| DoR évolutif | Scrum community | Révisé à chaque Rétro — s'adapte à la maturité de l'équipe |
| 3 Amigos pre-check | BDD community | PO + Dev + QA vérifient le DoR ensemble avant Sprint Planning |

---

## O3 — Négation talmudique

| Ce que DoR N'EST PAS | Document correct |
|---|---|
| Definition of Done (critères de sortie) | Gate DoD (R4) |
| Spécification complète | PRD / SRD |
| Contrat immuable | DoR évolue avec l'équipe — révisé en Rétro |
| Bureaucratie ralentissante | DoR trop strict = stories jamais prêtes = problème de Refinement |
| Standard universel | Chaque équipe définit son DoR |

---

## O4 — Format canonique

1. **Les AC sont-ils rédigés et testables ?** → Critère 1
2. **L'estimation est-elle faite ?** → Critère 2
3. **Les dépendances sont-elles identifiées et résolues ?** → Critère 3
4. **Les maquettes/designs sont-ils disponibles (si applicable) ?** → Critère 4
5. **La story tient-elle dans 1 sprint (taille ≤ 1 sprint) ?** → Critère 5

---

## Format canonique (checklist équipe)

| Critère | Vérification | Garde-fou |
|---|---|---|
| **AC rédigés** | Chaque AC est testable par un test automatisé ou manuel | "Fonctionne correctement" = pas un AC |
| **Estimation** | Story points ou T-shirt size définis | Non-estimé = impossible à planifier |
| **Dépendances** | Aucune dépendance bloquante non-résolue | Dépendance cachée = sprint bloqué à mi-chemin |
| **Design** | Wireframes ou maquettes disponibles (si UX impliqué) | Dev sans design = aller-retour coûteux |
| **Taille** | Implémentable dans 1 sprint par 1-2 devs | Story épique = jamais Done |

---

## Ker / Im

| | Contenu |
|---|---|
| **Ker** | Checklist d'entrée · Co-propriété de l'équipe · Révisable en Rétro |
| **Im → Sprint Planning** | Seules les stories DoR-ready entrent en Sprint Planning — intégrité du sprint garantie |
