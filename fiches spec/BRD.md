# BRD — Business Requirements Document
*doc-spec v1 · 2026-05-16 · pipeline: fmaths + GAFAM + négation talmudique + formulaire science*

---

## O1 — Formalisation

```
BRD : Ω_opportunité → Ω_objectifs
```

| | Contenu |
|---|---|
| **Domaine Ω_opportunité** | Opportunité délimitée issue du MRD (problem space, sizing, timing) |
| **Codomaine Ω_objectifs** | Objectifs business mesurables + scope features priorisé sur 9–12 mois |
| **Propriété** | Réducteur · \|Im(BRD)\| < \|Dom(BRD)\| — filtrage intentionnel du scope MRD |

---

## O2 — GAFAM best practices

| Pratique | Source | Apport |
|---|---|---|
| OKRs Key Results | Google / Doerr | Objectifs mesurables à 9–12 mois avec critères de succès |
| Impact Mapping | Gojko Adzic / SAFe | WHY → WHO → HOW → WHAT : lie chaque feature à un impact business |
| Epic Planning | Atlassian / Spotify | Structures les features en Epics traçables jusqu'au sprint |
| Working Backwards | Amazon | La question "quel ROI ?" avant toute décision de scope |
| Business Case / ROI | Standard VC | Coût de ne pas faire + projection sur la période |

---

## O3 — Négation talmudique

| Ce que BRD N'EST PAS | Document correct |
|---|---|
| Analyse marché, tendances, sizing | MRD |
| Spec produit (user stories, wireframes) | PRD |
| User stories détaillées | PRD / SRD |
| Document technique ou architecture | SRD |
| Plan financier P&L complet | Document finance |

---

## O4 — Formulaire science (ordre cognitif)

> Du concret vers l'abstrait. Chaque question s'appuie sémantiquement sur la précédente.

1. **Quel problème MRD adresse-t-on ?** → Executive Summary
2. **Quels objectifs mesurables à 9–12 mois ?** → Business Objectives
3. **Pourquoi ça vaut le coût / coût de ne pas faire ?** → Business Case / ROI
4. **Qui approuve, quelles contraintes légales/métier ?** → Stakeholder Requirements
5. **Qu'est-ce qu'on construit ? Qu'est-ce qu'on exclut ?** → Feature Scope In/Out
6. **Dans quel ordre sur 9–12 mois ?** → Release Roadmap

---

## Sommaire canonique

| Section | Question structurante | Garde-fou |
|---|---|---|
| **Executive Summary** | Quel problème MRD ? Quelle réduction stratégique ? Quel ROI attendu ? | > 5 phrases = pas un résumé |
| **Business Objectives** | Quels objectifs mesurables à 9–12 mois ? | Objectifs sans métrique = invalide |
| **Business Case / ROI** | Pourquoi maintenant ? Coût de ne pas faire ? | ROI sans hypothèses explicites = invalide |
| **Stakeholder Requirements** | Qui approuve quoi ? Quelles contraintes métier/légales ? | Stakeholders sans contraintes = inutile |
| **Feature Scope (In/Out)** | Quelles features sont IN pour v1 ? Qu'est-ce qui est OUT ? | Pas d'Out of Scope = scope illimité |
| **Release Roadmap** | Séquence des phases à 9–12 mois ? | Roadmap sans critères de passage = invalide |

---

## Ker / Im

| | Contenu |
|---|---|
| **Ker** (reste dans BRD) | Epic/Theme structure · Stakeholder mapping · Contraintes légales/tech · Release roadmap · Business Case/ROI |
| **Héritage R1 → BRD** | OKRs · PR-FAQ · JTBD · Lean BML |
| **Im → PRD via R2** | Impact Mapping · USM · JTBD · North Star |
