# Sprint Contract — C7 "DAG Layer Labels"

> μA(C) = 0, μV(C) = 1 → PASS

## Sprint n°: C7
**Date:** 2026-05-12
**Project:** ecosystem.html — branche feat/atlas-concepts
**Global Attractor 𝕋ᴳ:** Décodeur IT + orchestre d'agents — chaque couche du pipeline est nommée et visible.

## Goal (G)
```
Chaque bouton topbar affiche son étiquette DAG au-dessus de son nom.
— PROOF: Grep 'class="tab-dag"' ecosystem.html → 6 hits
  AND Grep 'WAREHOUSE' ecosystem.html → ≥ 1 hit dans un tab-btn
```
**SCOPE:** `ecosystem.html` lignes 251-258 (CSS) + lignes 516-521 (6 boutons)
**TIMEBOX:** 1 sprint
**NON-GOALS:** Pas de changement navigation, pas de retrait atl-role, pas de nouvel onglet

## Sprint Backlog (B)
1. [CSS] Ajouter après ligne 258 :
   `.tab-dag { display:block; font-size:10px; color:#484f58; text-align:center; letter-spacing:.03em; margin-bottom:1px; }`
   `.tab-btn.active .tab-dag { color:rgba(88,166,255,.55); }`
2. [STRUCT] Modifier les 6 boutons lignes 516-521 — ajouter `<span class="tab-dag">LABEL</span>` avant le texte :
   - Ecosystem → `🧠 CONSUME`
   - Légendes  → `🪨 LAKE`
   - Nature    → `📱 SOURCE`
   - Métiers   → `🛒 MART`
   - Préfecture → `🛒 MART`
   - Atlas     → `🏢 WAREHOUSE`

## Definition of Done (D)
- [D1] `Grep 'class="tab-dag"' ecosystem.html` → 6 hits
- [D2] `Grep 'WAREHOUSE' ecosystem.html` → ≥ 1 hit
- [D3] `Grep 'SOURCE.*tab-dag\|tab-dag.*SOURCE' ecosystem.html` → 0 hit (SOURCE est dans un span séparé)

## Pre-execution Score
| Composant | μA | μV |
|-----------|----|----|
| Goal G    | 1 interprétation, PROOF Grep binaire → 0/1 | PROOF exact → 1/1 |
| Backlog B | 2 items, lignes ciblées, mapping complet → 0/1 | Exhaustif → 1/1 |
| DoD D     | 3 conditions Grep → 0/1 | Toutes vérifiables → 1/1 |
| **Contract C** | **μA = 0** | **μV = 1** |

**Décision :**
- [x] PASS

## Sprint Attractor 𝕋₇
Tout visiteur identifie en 3 secondes la couche DAG de chaque onglet. L'architecture LAKE → WAREHOUSE → MART est lisible sans documentation externe.

## Notes
- LAKE/WAREHOUSE/MART = terminologie business préférée aux nœuds canoniques (STORE RAW, STORE STRUCTURED). Décision 2026-05-12.
- Labels MART sur Métiers et Préfecture = architecture cible. Implémentation actuelle : HTML statique. À résorber en C8.
- Règle pour tout futur onglet : choisir dans { 📱 SOURCE · 🪨 LAKE · 🏢 WAREHOUSE · 🛒 MART · 🎯 SERVE · 🧠 CONSUME }.
- Corrections binômes intégrées : D4→D3 (Grep positif), font-size:10px, text-align:center, Nature=SOURCE.
