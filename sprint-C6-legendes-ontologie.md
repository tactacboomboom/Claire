# Sprint Contract — C₆ "Légendes & Ontologie"

> Contrat actif. μA(C) = 0, μV(C) = 1 → PASS. (Revue rôles : QA R009 + Frontend R004 + Architect R054 + Tech Lead R046 + PM R037 + UX R041 + Designer R039 + Security R029 + Backend R005 + Staff R047 + Principal R048)

---

## Sprint n°: C₆

**Date:** 2026-05-11
**Project:** Claire / ecosystem.html
**Global Attractor 𝕋ᴳ:** ecosystem.html = un décodeur de l'IT auto-explicatif, sans contexte préalable.

---

## Goal (G)

```
Fusionner les 3 onglets SOLID & Pipeline + Théorèmes + Rôles IT
en un seul onglet "📚 Légendes" avec navigation à 2 niveaux —
SOLID & Pipeline découpé en 4 sous-onglets thématiques,
goToRole() recâblé pour naviguer vers le bon sous-onglet.
— PROOF: git log --oneline -1 montre commit sur feat/atlas-concepts
  AND topbar a 5 boutons (Ecosystem + Légendes + Nature + Métiers + Préfecture + Atlas)
  AND clic "Légendes" → nav L1 visible avec 4 boutons
  AND clic "SOLID & Pipeline" → nav L2 visible avec 4 sous-onglets
  AND pill rôle dans Atlas → navigue vers Légendes/Rôles IT + surlignage
```

**SCOPE:** ecosystem.html — topbar + 3 anciens onglets + goToRole() + CSS nav secondaire
**TIMEBOX:** 1 sprint
**NON-GOALS:**
- Contenu des onglets (pas de réécriture des théorèmes, rôles IT, sections SOLID)
- Onglets Métiers, Préfecture, Atlas, Nature
- Phase 9+ (Marts, Préfecture 3D, Role-as-Skill)

---

## Sprint Backlog (B)

1. [NAV] Remplacer les 3 boutons topbar (solid, theoremes, rolesit) par 1 bouton `<button class="tab-btn" onclick="switchTab('legendes')">📚 Légendes</button>`
2. [STRUCT] Créer `div#tab-legendes` avec nav L1 : 4 boutons `.leg-nav-btn` (Sommaire | SOLID & Pipeline | Théorèmes | Rôles IT)
3. [STRUCT-SOLID] Dans `#leg-solid` : nav L2 avec 4 `.solid-sub-btn` (Pipeline | Code | Architecture | Projets)
   Découpe tab-solid (11 sections) en 4 sous-sections :
   - Pipeline : sections 1 (Vocabulaire DAG) + 6 (Zones orthogonales)
   - Code : sections 4 (POO) + 5 (SOLID→DAG) + 7 (Volatilité) + 8 (Design Patterns)
   - Architecture : sections 2 (DDD) + 3 (Paradigmes) + 9 (Processus découpe)
   - Projets : sections 10 (8 Natures) + 11 (Division cognitive)
4. [CSS] Définir `.leg-nav-btn` (niveau secondaire) et `.solid-sub-btn` (niveau tertiaire), distincts de `.tab-btn`
5. [MIGRATE] Déplacer le HTML de tab-solid (→ 4 sous-sections), tab-theoremes et tab-rolesit dans div#tab-legendes
6. [SOMMAIRE] Page sommaire par défaut : titre + 1 phrase par sous-onglet (3 lignes, très court)
7. [RECABLE] `goToRole()` : `switchTab('legendes')` → `setTimeout(120ms)` → activer `#leg-rolesit` → `setTimeout(80ms)` → scroll + fix sélecteur `#leg-rolesit .card-name`
8. [STATE] Variables `_legTab = 'sommaire'` et `_solidSubTab = 'pipeline'` pour mémoriser la position
9. [CLEAN] Supprimer `div#tab-solid`, `div#tab-theoremes`, `div#tab-rolesit`

---

## Definition of Done (D)

- [D1] Un seul bouton Légendes dans la topbar — PROOF : `querySelectorAll('.tab-btn')` → 6 boutons (Ecosystem + Légendes + Nature + Métiers + Préfecture + Atlas)
- [D2] Nav L1 visible dans Légendes — PROOF : `querySelectorAll('#tab-legendes .leg-nav-btn').length === 4`
- [D3] Sous-onglet Pipeline actif par défaut dans SOLID & Pipeline — PROOF : `#leg-solid-pipeline` a class `active` au premier clic SOLID
- [D4] goToRole() navigue correctement — PROOF : clic pill → Légendes actif + Rôles IT visible + carte surlignée
- [D5] Anciens onglets supprimés — PROOF : Ctrl+F `id="tab-solid"` = 0 hit AND `id="tab-theoremes"` = 0 hit AND `id="tab-rolesit"` = 0 hit

---

## Pre-execution Score

| Composant | μA (ambiguité) | μV (validation) |
|-----------|---------------|-----------------|
| Goal G | A1=0 A2=0 A3=0 A4=0 → **0/1** | V1=1 V2=1 V3=1 → **1/1** |
| Backlog B | 9 items, toutes actions binaires → **0/1** | V1=1 V2=1 V3=1 → **1/1** |
| DoD D | D1-D5 toutes binaires, valeur exacte → **0/1** | V1=1 V2=1 V3=1 → **1/1** |
| **Contract C** | **μA = 0** | **μV = 1** |

**Décision :**
- [x] PASS — μA(C) = 0 < 0.5 AND μV(C) = 1 ≥ 0.4 → sprint exécutable

---

## Sprint Attractor 𝕋ₙ

La topbar passe de 8 à 6 boutons. Les 3 onglets de référence sont regroupés sous "📚 Légendes". L'onglet SOLID & Pipeline est découpé en 4 sous-onglets thématiques (Pipeline / Code / Architecture / Projets). Les pills rôles dans l'Atlas naviguent vers Légendes → Rôles IT.

---

## Notes

- Ambiguïtés résolues : A1 (mémorisation position = oui, _legTab + _solidSubTab), A2 (nommage icônes boutons), A3 (iframe théorèmes = déjà HTML pur), A4 (style nav secondaire = classe distincte)
- goToRole() doit éviter event.target (pas d'événement lors d'appel programmatique) — manipulation DOM directe
- La découpe "Pipeline (1+6)" regroupe les couches DAG + zones orthogonales (cohérence thématique infra)
- La découpe "Code (4+5+7+8)" regroupe POO + SOLID + Volatilité + GoF (cohérence codage)
- La découpe "Architecture (2+3+9)" regroupe DDD + Paradigmes + Processus découpe (cohérence design)
- La découpe "Projets (10+11)" regroupe 8 Natures + Division cognitive (cohérence niveau projet)
