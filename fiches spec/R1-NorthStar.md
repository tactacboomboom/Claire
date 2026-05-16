# North Star Metric
*doc-spec v1 · 2026-05-16 · protocole R1 (MRD → BRD) + unificateur R2*

---

## O1 — Formalisation

```
NorthStar : Ω_valeur → Ω_métrique_unique
```

| | Contenu |
|---|---|
| **Domaine** | Valeur créée pour le client (multidimensionnelle, subjective) |
| **Codomaine** | 1 métrique proxy qui corrèle valeur client et croissance long terme |
| **Propriété** | Compresseur · réduit la complexité de la valeur à 1 signal mesurable — critère : stable dans le temps, actionnable, leading indicator |

---

## O2 — GAFAM best practices

| Pratique | Source | Apport |
|---|---|---|
| North Star Metric | Sean Ellis / GrowthHackers (2010) | 1 métrique de croissance qui exprime la valeur client réelle |
| North Star Playbook | Amplitude (2017) | Input metrics (leviers) + North Star + Revenue (lagging) |
| "Aha moment" metric | Facebook / Twitter | Mesurer l'activation — moment où le client comprend la valeur |
| Leading vs Lagging | Sean Ellis | NSM = leading indicator · Revenue = lagging · ne pas confondre |
| Counter-metrics | Duolingo | Métrique de santé contre l'optimisation aveugle de la NSM |

---

## O3 — Négation talmudique

| Ce que North Star N'EST PAS | Document correct |
|---|---|
| Métrique de revenus (lagging) | P&L / Finance |
| KPI opérationnel (taux d'erreur, uptime) | Dashboard technique |
| Objectif trimestriel | OKR Key Result |
| Unique source de vérité sur la santé produit | Nécessite des counter-metrics |
| Métrique vanité (page views, downloads) | Réelle valeur client, pas volume brut |

---

## O4 — Format canonique

1. **Quelle valeur unique créons-nous pour le client ?** → Définir la valeur core
2. **Quelle métrique proxy capture cette valeur le mieux ?** → North Star candidate
3. **Quels leviers font bouger cette métrique ?** → Input metrics (3-5)
4. **Quelle contre-métrique évite les effets pervers ?** → Counter-metric

---

## Format canonique

| Élément | Exemple (Airbnb) | Garde-fou |
|---|---|---|
| **North Star Metric** | Nuits réservées | Métrique choisie par consensus ≠ métrique juste |
| **Input metrics** | Hôtes actifs · Taux de conversion · Rétention voyageurs | > 5 input metrics = diffusion du focus |
| **Counter-metric** | Qualité des séjours (rating ≥ 4.5) | Sans counter = optimisation aveugle |
| **Fréquence de review** | Mensuelle | Jamais révisée = métrique zombie |

---

## Ker / Im

| | Contenu |
|---|---|
| **Ker** | Valeur client articulée · Input metrics identifiées · Counter-metrics |
| **Im → R1 (BRD)** | Success Metrics fondées sur la NSM · Critères de priorisation OKRs |
| **Im → R2 (PRD)** | Filtre features : "cette feature fait-elle bouger une input metric ?" |
