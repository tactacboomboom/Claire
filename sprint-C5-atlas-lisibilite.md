# Sprint Contract — C₅ "Atlas Lisibilité"

> Contrat actif. μA(C) = 0, μV(C) = 1 → PASS. (Revue rôles : QA R009 + Frontend R004 + Architect R054 + PM R037)

---

## Sprint n°: C₅

**Date:** 2026-05-11
**Project:** Claire / ecosystem.html
**Global Attractor 𝕋ᴳ:** ecosystem.html = un décodeur de l'IT auto-explicatif, sans contexte préalable.

---

## Goal (G)

```
Rendre l'Atlas lisible sans connaître les codes par cœur —
labels familles explicites, filtre DDD ajouté, bouton Universels supprimé.
— PROOF: git log --oneline -1 montre commit sur feat/atlas-concepts
  AND dropdown "Toutes familles" affiche "N1 — Matière" (pas "N1")
  AND un select "Couche DDD" est visible dans la barre Atlas
  AND Ctrl+F "⊕ Universels" dans ecosystem.html = 0 occurrences HTML
```

**SCOPE:** ecosystem.html — barre de filtres Atlas + filterAtlas() uniquement
**TIMEBOX:** 1 sprint
**NON-GOALS:**
- Autres onglets (Métiers, Rôles IT, SOLID & Pipeline)
- Refonte layout/colonnes de l'Atlas
- Phase 9 (fusion Légendes)

---

## Sprint Backlog (B)

1. [SUPPR] Supprimer bouton ⊕ Universels (ligne 1805) ET supprimer la fonction toggleAtlasUniv() du JS
2. [LABEL] Remplacer les options codes dans `atl-fam` en séparant value et display :
   Format obligatoire : <option value="CODE">CODE — Label</option>
   - <option value="N1">N1 — Matière</option>
   - <option value="N2">N2 — Mouvement</option>
   - <option value="N3">N3 — Jonction</option>
   - <option value="F1">F1 — Développeurs</option>
   - <option value="F2">F2 — Data / ML</option>
   - <option value="F3">F3 — Infra / Ops</option>
   - <option value="F4">F4 — Sécurité</option>
   - <option value="F5">F5 — Produit / Design</option>
   - <option value="F6">F6 — Leadership</option>
   - <option value="S">S — SRP</option>
   - <option value="O">O — OCP</option>
   - <option value="L">L — LSP</option>
   - <option value="I">I — ISP</option>
   - <option value="D">D — DIP</option>
   - Autres (Création, Structure, Comportement, Principal, Orthogonal, Impérative, Déclarative, Concurrente, Pilote, Ossature, Substance, POO, Zone) → inchangés
3. [FILTRE] Ajouter <select id="atl-ddd"> avec options labellisées (value=code, display=label) :
   - <option value="">Toutes couches DDD</option>
   - <option value="domain">Domain — Logique métier</option>
   - <option value="infrastructure">Infrastructure — Technique</option>
   - <option value="application">Application — Use cases</option>
   - <option value="interfaces">Interfaces — UI & API</option>
   - <option value="all">Tous contextes DDD</option>
   Logique filtre : r.ddd === 'all' || r.ddd.includes(selectedDDD)

---

## Definition of Done (D)

- [D1] Bouton et fonction absents — PROOF : Ctrl+F "⊕ Universels" dans ecosystem.html = 0 hit UI AND Ctrl+F "toggleAtlasUniv" = 0 hit
- [D2] Labels familles — PROOF : dropdown famille → "N1 — Matière" visible
- [D3] Filtre DDD fonctionnel — PROOF : sélectionner "domain" → seuls concepts avec ddd contenant "domain"
- [D4] Commit sur feat/atlas-concepts — PROOF : git log --oneline -1

---

## Pre-execution Score

| Composant | μA (ambiguité) | μV (validation) |
|-----------|---------------|-----------------|
| Goal G | A1=0 A2=0 A3=0 A4=0 → **0/1** | V1=1 V2=1 V3=1 → **1/1** |
| Backlog B | 3 items, labels tous définis → **0/1** | V1=1 V2=1 V3=1 → **1/1** |
| DoD D | D1-D4 toutes binaires, valeur exacte spécifiée → **0/1** | V1=1 V2=1 V3=1 → **1/1** |
| **Contract C** | **μA = 0** | **μV = 1** |

**Décision :**
- [x] PASS — μA(C) = 0 < 0.5 AND μV(C) = 1 ≥ 0.4 → sprint exécutable

---

## Sprint Attractor 𝕋ₙ

L'Atlas est auto-explicatif. Le dropdown famille affiche "N1 — Matière" au lieu de "N1". Un filtre "Couche DDD" permet de filtrer par domain / infrastructure / application / interfaces. Le bouton ⊕ Universels a disparu.

---

## Notes

- Ligne 1805 : bouton à supprimer
- Ligne 1710-1719 : dropdown atl-fam à relabelliser
- filterAtlas() : ajouter const ddd = document.getElementById('atl-ddd').value; + condition r.ddd.includes(ddd)
- Ambiguïtés résolues : A1 (labels SOLID) + A2 (format "N1 — Matière") en session 2026-05-11
