# USM — User Story Mapping
*doc-spec v1 · 2026-05-16 · protocole R2 (BRD → PRD)*

---

## O1 — Formalisation

```
USM : Ω_features → Ω_expérience_cohérente
```

| | Contenu |
|---|---|
| **Domaine** | Features candidates issues de l'Impact Map ou du BRD (liste plate, non-ordonnée) |
| **Codomaine** | Parcours utilisateur cohérent avec tranches de valeur (slices) livrables indépendamment |
| **Propriété** | Organisateur · 2 axes orthogonaux — horizontal = temps (parcours) · vertical = détail (valeur) |

---

## O2 — GAFAM best practices

| Pratique | Source | Apport |
|---|---|---|
| User Story Mapping | Jeff Patton (2005+, "User Story Mapping" 2014) | Grille 2D : activités → tâches → stories par slices |
| "Backbone" concept | Jeff Patton | Axe H = backbone (activités séquencées) — inchangé quelle que soit la version |
| Walking Skeleton | Alistair Cockburn | Slice v1 = expérience minimale mais cohérente end-to-end |
| Dual-track Agile | Marty Cagan / Teresa Torres | Discovery (USM vivant) vs Delivery (sprint backlog) |
| Miro / Mural templates | Standard remote | USM en atelier distribué — collaboratif en temps réel |

---

## O3 — Négation talmudique

| Ce que USM N'EST PAS | Document correct |
|---|---|
| Impact Mapping (causalité goal → feature) | Impact Mapping |
| Backlog Scrum (liste plate ordonnée) | Sprint Backlog (SRD) |
| User journey map (émotions + touchpoints) | UX Journey Map |
| Processus métier formalisé | BPMN / Event Storming |
| Document figé — évolue avec la discovery | USM est vivant |

---

## O4 — Format canonique

1. **Quel est le parcours utilisateur de bout en bout (axe horizontal) ?** → Activités (niveau 1)
2. **Quelles tâches composent chaque activité ?** → Tâches (niveau 2) = backbone
3. **Quelles stories implémentent chaque tâche ?** → User Stories (niveau 3+)
4. **Quelle tranche horizontale livre une expérience minimale cohérente ?** → Slice v1 (Walking Skeleton)
5. **Quelles tranches supplémentaires enrichissent l'expérience ?** → Slice v2, v3…

---

## Format canonique (grille 2D)

| Axe | Structure | Garde-fou |
|---|---|---|
| **Horizontal (temps)** | Activités → Tâches séquencées dans le temps | Activités non-séquentielles = backbone artificiel |
| **Vertical (valeur)** | Stories du plus essentiel (haut) au plus optionnel (bas) | Trop de stories en haut = pas de slice possible |
| **Slice** | Ligne horizontale = version livrée cohérente | Slice qui coupe une activité = expérience brisée |

---

## Ker / Im

| | Contenu |
|---|---|
| **Ker** | Backbone (activités stables) · Slices de valeur · Séquençage utilisateur |
| **Im → PRD** | User Workflows structurés · Product Vision par slice · Stories ordonnées pour le backlog |
