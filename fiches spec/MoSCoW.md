# MoSCoW — Prioritization Framework
*doc-spec v1 · 2026-05-16 · pipeline: fmaths + GAFAM + négation talmudique + formulaire science*

---

## O1 — Formalisation

```
MoSCoW : Ω_backlog → Ω_priorités
```

| | Contenu |
|---|---|
| **Domaine Ω_backlog** | Ensemble non-priorisé de features, requirements, user stories |
| **Codomaine Ω_priorités** | 4 buckets ordonnés : Must / Should / Could / Won't |
| **Propriété** | Classificateur · partitionne le backlog en 4 classes disjointes · doit être révisé à chaque release |

---

## O2 — GAFAM best practices

| Pratique | Source | Apport |
|---|---|---|
| MoSCoW (DSDM) | Dai Clegg / Oracle (1994) | Must · Should · Could · Won't — cadre de discussion, pas d'oracle |
| Now / Next / Later | GitHub / Spotify | Alternative moderne — horizon temporel vs importance absolue |
| RICE Scoring | Intercom | Reach × Impact × Confidence / Effort — quantifie avant de classer |
| Kano Model | Noriaki Kano | Basic vs Performance vs Excitement — complémentaire à MoSCoW |
| "Ruthless Prioritization" | Amazon | Toute feature doit lier à un customer problem — sinon = Won't |

---

## O3 — Négation talmudique

| Ce que MoSCoW N'EST PAS | Document correct |
|---|---|
| Estimation de complexité ou story points | Planning Poker / Scrum |
| Scoring multicritères objectif | RICE, ICE, Kano |
| Roadmap produit | BRD Release Roadmap |
| Backlog refinement | Process R3 (SRD) |
| Décision finale irréversible | MoSCoW est un outil de conversation — révisable à chaque release |

---

## O4 — Formulaire science (ordre cognitif)

> De l'essentiel vers l'exclu. Chaque bucket définit la frontière du précédent.

1. **Sans quoi la release n'a aucune valeur ?** → Must Have
2. **Qu'est-ce qui est important mais non-bloquant ?** → Should Have
3. **Qu'est-ce qui serait bien d'avoir si la capacité le permet ?** → Could Have
4. **Qu'est-ce qu'on exclut explicitement de CETTE release ?** → Won't Have (this time)

---

## Sommaire canonique

| Bucket | Question structurante | Garde-fou |
|---|---|---|
| **Must Have** | Sans ça, la release est un échec ou illégale | > 60% du backlog en Must = scope illimité |
| **Should Have** | Important, mais la release a de la valeur sans ça | Should mal défini glisse en Must |
| **Could Have** | Bonus si temps et budget disponibles | Could illimité = scope creep déguisé |
| **Won't Have (this time)** | Exclu de CETTE release — pas définitivement | "Won't" sans "this time" = suppression définitive (faux signal) |

---

## Ker / Im

| | Contenu |
|---|---|
| **Ker** (reste dans MoSCoW) | Critères de classification · Règle Must ≤ 60% · Révision par release |
| **Im → BRD / PRD** | Feature Scope In/Out (BRD) · Stories priorisées pour le sprint (PRD) |
| **Position dans la chaîne** | Protocole de R2 (BRD → PRD) — utilisé lors de l'arbitrage features avant la spec PRD |
