# Lean BML — Build-Measure-Learn
*doc-spec v1 · 2026-05-16 · protocole R1 (MRD → BRD)*

---

## O1 — Formalisation

```
BML : Ω_hypothèse → Ω_connaissance_validée
```

| | Contenu |
|---|---|
| **Domaine** | Hypothèse non-validée sur un segment ou une opportunité marché |
| **Codomaine** | Connaissance validée (ou invalidée) par l'expérience — input pour BRD |
| **Propriété** | Itérateur · chaque boucle réduit l'incertitude sur une hypothèse spécifique · converge vers la vérité marché |

---

## O2 — GAFAM best practices

| Pratique | Source | Apport |
|---|---|---|
| Build-Measure-Learn loop | Eric Ries / "The Lean Startup" (2011) | 3 phases cycliques — minimiser le temps de la boucle |
| MVP (Minimum Viable Product) | Eric Ries / Steve Blank | Expérience minimale qui valide l'hypothèse la plus risquée |
| Customer Development | Steve Blank (2003) | Interviews avant tout build — "get out of the building" |
| Pivot vs Persevere | Eric Ries | Décision explicite après chaque boucle — pas de dérive silencieuse |
| Lean Analytics | Croll & Yoskovitz (2013) | Métriques par stade de maturité startup — évite les vanity metrics |

---

## O3 — Négation talmudique

| Ce que BML N'EST PAS | Document correct |
|---|---|
| Sprint Agile (livraison de features) | Sprint Scrum (SRD / R3) |
| Test A/B sur une feature existante | Optimisation produit (PRD) |
| Roadmap produit | BRD Release Roadmap |
| Recherche utilisateur formelle | UX Research |
| Déploiement continu | CI/CD (Code / R4) |

---

## O4 — Format canonique

1. **Quelle hypothèse veut-on tester (la plus risquée en premier) ?** → Leap of Faith Assumption
2. **Quel est le minimum à construire pour tester cette hypothèse ?** → MVP définition
3. **Quelle métrique prouvera que l'hypothèse est validée/invalidée ?** → Success metric + seuil
4. **Pivot ou persévère ?** → Decision post-boucle

---

## Format canonique

| Phase | Question | Garde-fou |
|---|---|---|
| **Build** | Quel est le minimum construisable pour tester l'hypothèse ? | MVP trop gros = trop long pour apprendre |
| **Measure** | Quelle métrique mesure le comportement réel (pas les déclarations) ? | Vanity metric = boucle inutile |
| **Learn** | L'hypothèse est-elle validée ? Pivot ou persévère ? | Pas de décision explicite = dérive |

---

## Ker / Im

| | Contenu |
|---|---|
| **Ker** | Hypothèses testées · Résultats mesurés · Pivots documentés |
| **Im → BRD** | Hypothèses marché validées → facts qui fondent le Business Case et le Feature Scope |
