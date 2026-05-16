# SRD — Software Requirements Document
*doc-spec v1 · 2026-05-16 · pipeline: fmaths + GAFAM + négation talmudique + formulaire science*

---

## O1 — Formalisation

```
SRD : Ω_comportements → Ω_implémentation
```

| | Contenu |
|---|---|
| **Domaine Ω_comportements** | User stories + acceptance criteria issus du PRD |
| **Codomaine Ω_implémentation** | Tâches techniques décomposées, DoR/DoD, contraintes d'architecture |
| **Propriété** | Décomposeur · traduit les comportements utilisateur en tâches techniques exécutables |

---

## O2 — GAFAM best practices

| Pratique | Source | Apport |
|---|---|---|
| ADR (Architecture Decision Records) | ThoughtWorks / GitHub | Documente chaque décision technique + alternatives rejetées + raison |
| DoR / DoD | Scrum Guide 2020 | Gate d'entrée (prêt à coder) et de sortie (terminé à livrer) — évite les stories fantômes |
| Backlog Refinement | Atlassian / Scrum Guide | Activité continue : clarifier les AC, estimer, vérifier DoR avant sprint planning |
| Technical Spec Doc | Google / Netflix | Architecture + data model + API spec + trade-offs explicités avant le code |
| Infrastructure as Code | AWS / HashiCorp | La spec d'infra vit dans le repo git — même versionnement que le code |

---

## O3 — Négation talmudique

| Ce que SRD N'EST PAS | Document correct |
|---|---|
| Spec produit ou user stories | PRD |
| Document pour l'utilisateur final | PRD |
| Le code lui-même | Code |
| Document de déploiement ou runbook | DevOps / SRE |
| Décision de scope ou de features | BRD / PRD |

---

## O4 — Formulaire science (ordre cognitif)

> Du concret vers l'abstrait. Chaque question s'appuie sémantiquement sur la précédente.

1. **Quels composants, interfaces, dépendances ?** → Architecture
2. **Quels choix tech et pourquoi (vs alternatives) ?** → Technology Stack
3. **Quelles entités, relations, contraintes d'intégrité ?** → Data Model
4. **Quels endpoints, formats, codes d'erreur ?** → API Specification
5. **Qu'est-ce qui est "prêt" à coder / "terminé" à livrer ?** → DoR / DoD
6. **Quelles limitations connues, quels compromis documentés ?** → Technical Debt

---

## Sommaire canonique

| Section | Question structurante | Garde-fou |
|---|---|---|
| **Architecture** | Quels composants, interfaces, dépendances ? | Architecture sans justification trade-offs = gold plating |
| **Technology Stack** | Quels choix tech et pourquoi vs alternatives ? | Stack listé sans trade-offs = copié-collé |
| **Data Model** | Quelles entités, relations, contraintes d'intégrité ? | Schéma sans contraintes = données incohérentes |
| **API Specification** | Quels endpoints, formats, codes d'erreur ? | API sans gestion d'erreurs = intégration impossible |
| **DoR / DoD** | Definition of Ready + Done pour ce sprint ? | DoR/DoD absents = stories non-terminables |
| **Technical Debt** | Quelles limitations connues, quels compromis documentés ? | Dette non-documentée = surprise en production |

---

## Ker / Im

| | Contenu |
|---|---|
| **Ker** (reste dans SRD) | Tasks décomposées · DoR/DoD · Sprint planning · Architecture decisions (ADR) · Technical debt |
| **Héritage R3 → SRD** | User Stories + AC via Backlog Refinement |
| **Im → Code via R4** | Tasks DoR-ready · DoD vérifiable · Incrément livrable |
