# Code — Terminus de la Chaîne
*doc-spec v1 · 2026-05-16 · pipeline: fmaths + GAFAM + négation talmudique + formulaire science*

---

## O1 — Formalisation

```
Code : Ω_implémentation → Ω_réel
```

| | Contenu |
|---|---|
| **Domaine Ω_implémentation** | Tâches DoR-ready issues du SRD |
| **Codomaine Ω_réel** | Incrément livrable + révélation des implicites non-spécifiés |
| **Propriété** | Terminus nilpotent · Code² = Code (idempotent sur le réel) · révélateur des implicites |

> Le Code est le seul artefact qui force la résolution de toutes les ambiguïtés. Ce qui était flou dans le PRD ("chargement rapide") devient une contrainte précise ("< 200ms sur 4G") dès que le test de performance tourne.

---

## O2 — GAFAM best practices

| Pratique | Source | Apport |
|---|---|---|
| TDD (Test-Driven Development) | Kent Beck / Google | Le test précède l'implémentation — le DoD devient exécutable |
| CI/CD (DORA metrics) | Google DORA | Déploiement fréquent + mesure Lead Time / MTTR / Change Failure Rate |
| Code Review | Microsoft / Google | Détecte les ambiguïtés SRD non résolues avant qu'elles atteignent la prod |
| Observability | Netflix / Honeycomb | Les NFR du PRD sont mesurés en production (logs, traces, métriques) |
| Infrastructure as Code | AWS / Terraform | L'infra vit dans le repo — même cycle de review que le code applicatif |

---

## O3 — Négation talmudique

| Ce que Code N'EST PAS | Document correct |
|---|---|
| Spécification de ce qu'il faut construire | SRD |
| Vérité sur le produit voulu par l'utilisateur | PRD |
| Stratégie business ou ROI | BRD / MRD |
| Documentation (sauf si self-documenting) | Docs séparées |
| Source de vérité sur les décisions d'architecture | ADR dans le SRD |

---

## O4 — Formulaire science (ordre cognitif)

> Du concret vers l'abstrait. Chaque question s'appuie sémantiquement sur la précédente.

1. **Chaque feature SRD est-elle couverte ?** → Implementation
2. **Les DoD sont-ils vérifiables par les tests ?** → Tests
3. **Quels bugs révèlent des ambiguïtés SRD/PRD ?** → Révélateurs d'implicites
4. **Les NFR du PRD sont-ils mesurés en production ?** → Métriques runtime

---

## Sommaire canonique

| Section | Question structurante | Garde-fou |
|---|---|---|
| **Implementation** | Chaque feature SRD est-elle couverte ? | Feature orpheline = spec SRD manquante |
| **Tests** | Les DoD sont-ils vérifiables par les tests ? | Tests sans DoD = coverage sans sens |
| **Révélateurs d'implicites** | Quels bugs/edge cases révèlent des ambiguïtés SRD/PRD ? | Bug non-remonté = dette documentaire |
| **Métriques runtime** | Les NFR du PRD sont-ils mesurés en production ? | NFR non-mesurées = contrat PRD non-vérifié |

---

## Ker / Im

| | Contenu |
|---|---|
| **Ker** (reste dans Code) | Syntaxe · Patterns · Tests · Révélateurs d'implicites · Métriques runtime |
| **Héritage R4 → Code** | Incrément DoR-ready · Sprint Goal · DoD vérifiable |
| **Im → feedback upstream** | Bugs → SRD (DoD préciser) → PRD (AC corriger) → BRD (scope réviser) — itération nilpotente inverse |
