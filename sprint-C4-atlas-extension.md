# Sprint Contract — C₄

> Contrat actif. μA(C) = 0, μV(C) = 1 → PASS.

---

## Sprint n°: C₄

**Date:** 2026-05-09
**Project:** Claire / ecosystem.html
**Global Attractor 𝕋ᴳ:** Un explorer interactif unique qui rend l'architecture logicielle et data navigable pour n'importe quel niveau — du rôle métier au théorème formel, de l'outil à la couche DDD — sans prérequis technique.

---

## Goal (G)

```
Add tabs Métiers + Préfecture + Théorèmes to ecosystem.html
so that the page maps job roles to architectural layers
and embeds the 53 theorems atlas
— PROOF: git log --oneline -1 shows commit on main
  AND ecosystem.html opens with 5 tabs visible.
```

**SCOPE:** ecosystem.html (1 file) + embed de mindmap-atlas-50-theoremes.html
**TIMEBOX:** 1 sprint
**NON-GOALS:**
- Tools atlas tab (sprint séparé)
- Hyperliens croisés théorèmes ↔ nœuds DAG (post-sprint)

---

## Sprint Backlog (B)

1. [BUILD] Construire tab 👔 Métiers — table DAG nodes + couches DDD + zones → rôle métier (Backend / DevOps / Data Engineer / SRE / AMOA / Frontend)
2. [BUILD] Construire tab 🏛️ Préfecture — table commutative Préfecture↔IT sur 10 zones avec colonne bijection
3. [INTEGRATE] Intégrer mindmap-atlas-50-theoremes.html comme tab 🔬 Théorèmes via iframe embed

---

## Definition of Done (D)

- [D4] Commit sur main — PROOF: `git log --oneline -1` affiche un hash sur main
- [D3] ecosystem.html rend 5 tabs — PROOF: fichier ouvre dans le navigateur avec 5 tabs visibles : 📊 SOLID · 🧬 Nature · 👔 Métiers · 🏛️ Préfecture · 🔬 Théorèmes
- [D3] Tab 🔬 Théorèmes affiche les 3 actes — PROOF: N1 Matière + N2 Mouvement + N3 Jonction visibles avec leurs cards

---

## Pre-execution Score

| Component | μA (ambiguité) | μV (validation) |
|-----------|----------------|-----------------|
| Goal G | A₁=0 A₂=0 A₃=0 A₄=0 → **0/1** | V₁=1 V₂=1 V₃=1 → **1/1** |
| Backlog B | 3 items, chacun = 1 phase exacte → **0/1** | V₁=1 V₂=1 V₃=1 → **1/1** |
| DoD D | D4+D3+D3, toutes binaires → **0/1** | V₁=1 V₂=1 V₃=1 → **1/1** |
| **Contract C** | **μA = 0** | **μV = 1** |

**Decision:**
- [x] PASS — μA(C) = 0 < 0.5 AND μV(C) = 1 ≥ 0.4 → sprint exécutable

---

## Sprint Attractor 𝕋ₙ

Ecosystem.html affiche 5 onglets. 👔 Métiers montre quel ingénieur opère chaque zone du DAG. 🏛️ Préfecture transpose la préfecture française en architecture IT sur 10 zones. 🔬 Théorèmes affiche les 53 théorèmes de l'Atlas data engineering.

---

## Notes

- Source Préfecture : tableau 10 zones fourni par l'utilisateur + atlas-dag-absolu-N4.md
- Source Métiers : dérivé du DAG absolu + DDD + zones orthogonales (mappings dans findings.md)
- Source Théorèmes : G:\Mon Drive\10 - Claude\projects\Claire\mindmap-atlas-50-theoremes.html
