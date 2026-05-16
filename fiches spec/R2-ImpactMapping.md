# Impact Mapping
*doc-spec v1 · 2026-05-16 · protocole R2 (BRD → PRD)*

---

## O1 — Formalisation

```
ImpactMap : Ω_goal → Ω_features_justifiées
```

| | Contenu |
|---|---|
| **Domaine** | Goal business (BRD Objective) |
| **Codomaine** | Features PRD dont chacune est justifiée par un impact sur un acteur qui sert le goal |
| **Propriété** | Filtre causal · élimine les features sans lien causal avec le goal — 4 niveaux : WHY → WHO → HOW → WHAT |

---

## O2 — GAFAM best practices

| Pratique | Source | Apport |
|---|---|---|
| Impact Mapping | Gojko Adzic (2012) | WHY (goal) → WHO (acteurs) → HOW (impacts comportementaux) → WHAT (features) |
| "Impact Mapping" livre | Gojko Adzic | Format mindmap — une page, goal au centre |
| SAFe PI Planning | Scaled Agile | Impact Map comme outil de PI Objectives |
| OKR + Impact Map | Combinaison fréquente | OKR = goal, Impact Map = route vers le goal |
| BDD + Impact Map | ThoughtWorks | Les impacts → scenarios BDD → acceptance criteria |

---

## O3 — Négation talmudique

| Ce que Impact Mapping N'EST PAS | Document correct |
|---|---|
| User Story Map (séquence horizontale d'activités) | USM (Jeff Patton) |
| Liste de features priorisées | MoSCoW / Backlog |
| Spécification de comportement | User Stories PRD |
| Diagramme de flux ou processus | BPMN / Event Storming |
| Garantie que les features livreront l'impact | C'est une hypothèse à tester (BML) |

---

## O4 — Format canonique

1. **WHY : Quel goal business précis (mesurable) ?** → Root node
2. **WHO : Quels acteurs peuvent influencer ce goal ?** → Level 2
3. **HOW : Quel changement de comportement de chaque acteur sert le goal ?** → Level 3 (impacts)
4. **WHAT : Quelles features permettent ce changement de comportement ?** → Level 4 (deliverables)

---

## Format canonique (mindmap)

| Niveau | Question | Garde-fou |
|---|---|---|
| **WHY** | Quel goal mesurable (OKR Key Result) ? | Goal flou = tout semble justifié |
| **WHO** | Qui peut aider ou nuire à l'atteinte du goal ? | Acteur sans comportement = inutile |
| **HOW** | Quel comportement de cet acteur sert le goal ? | Comportement non-observable = non-testable |
| **WHAT** | Quelle feature minimale déclenche ce comportement ? | Feature sans acteur associé = orpheline |

---

## Ker / Im

| | Contenu |
|---|---|
| **Ker** | Lien causal goal → acteur → impact → feature · Features orphelines exclues |
| **Im → PRD** | Features justifiées par un impact · Personas validés · Acceptance criteria candidats |
