# MRD — Market Requirements Document
*doc-spec v1 · 2026-05-16 · pipeline: fmaths + GAFAM + négation talmudique + formulaire science*

---

## O1 — Formalisation

```
MRD : Ω_marché → Ω_opportunité
```

| | Contenu |
|---|---|
| **Domaine Ω_marché** | Signaux bruts : tendances macro, pain points, segments non-servis |
| **Codomaine Ω_opportunité** | Opportunité délimitée : problem space, sizing, timing |
| **Propriété** | Nilpotent : MRD² = 0 — appliquer MRD à une opportunité déjà délimitée n'ajoute rien |

---

## O2 — GAFAM best practices

| Pratique | Source | Apport |
|---|---|---|
| PR-FAQ (Working Backwards) | Amazon | Force à nommer le customer problem avant toute solution |
| JTBD | Christensen / Intercom | "What job is the customer hiring this product for ?" |
| North Star Metric | Sean Ellis / Amplitude | Une seule métrique de valeur → filtre R1 vers BRD |
| TAM / SAM / SOM | Standard VC/Product | Crédibilise l'opportunité sans sur-précision |
| OKRs stratégiques | Google / Doerr | Transforme l'opportunité en objectifs mesurables — pont R1 |

---

## O3 — Négation talmudique

| Ce que MRD N'EST PAS | Document correct |
|---|---|
| Liste de features | BRD / PRD |
| Roadmap technique ou architecture | SRD |
| Business plan financier (P&L, coûts) | Document finance |
| Spec produit (comment ça marche) | PRD |
| Document pour l'équipe dev | PRD / SRD |
| Document figé | MRD est vivant 6–18 mois |

---

## O4 — Formulaire science (ordre cognitif)

> Du concret vers l'abstrait. Chaque question s'appuie sémantiquement sur la précédente.

1. **Quel est le problème ?** → Problem Statement
2. **Qui souffre de ce problème ?** → Market Segments + JTBD
3. **Pourquoi maintenant ?** → Timing + Tendances macro
4. **Combien sont-ils ?** → TAM / SAM / SOM
5. **Qui d'autre y répond déjà ?** → Competitive Positioning
6. **Comment saurons-nous si on réussit ?** → Success Metrics / North Star
7. **Sur quel horizon ?** → Timeline + jalons de révision

---

## Sommaire canonique

| Section | Question structurante | Garde-fou |
|---|---|---|
| **Problem Statement** | Quel problème précis, pour qui, dans quel contexte ? | > 3 phrases = périmètre trop large |
| **Market Segments** | Quels segments cibles ? Quels JTBD par segment ? | Segment sans JTBD = décoratif |
| **Market Opportunity** | TAM/SAM/SOM + fenêtre d'opportunité (pourquoi maintenant) ? | Sizing sans hypothèses explicites = inventé |
| **Competitive Positioning** | Qui d'autre répond à ce problème ? Différenciateur unique ? | Différenciateur non-testable = invalide |
| **Success Metrics** | North Star Metric + 2–3 input metrics mesurables ? | Métrique sans baseline = non-suivable |
| **Timeline** | Horizon + jalons de révision déclenchés par quoi ? | Timeline sans trigger de révision = document mort |
| **R1 Handoff** | Quels artefacts transmis à BRD via R1 ? | Handoff sans protocole nommé = rupture silencieuse |

---

## Ker / Im

| | Contenu |
|---|---|
| **Ker** (reste dans MRD) | Analyse macro-tendances · Jobs non-satisfaits · Segments cibles · Sizing TAM/SAM/SOM |
| **Im → BRD via R1** | OKRs · North Star · PR-FAQ · JTBD · Lean BML |
