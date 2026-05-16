# PRD — Product Requirements Document
*doc-spec v1 · 2026-05-16 · pipeline: fmaths + GAFAM + négation talmudique + formulaire science*

---

## O1 — Formalisation

```
PRD : Ω_objectifs → Ω_comportements
```

| | Contenu |
|---|---|
| **Domaine Ω_objectifs** | Objectifs business et scope features issus du BRD |
| **Codomaine Ω_comportements** | Interactions utilisateur précises : user stories, wireframes, acceptance criteria |
| **Propriété** | Spécificateur · traduit les objectifs business en comportements utilisateur testables |

---

## O2 — GAFAM best practices

| Pratique | Source | Apport |
|---|---|---|
| User Story Map | Jeff Patton | Structure les stories en parcours utilisateur cohérents par tranches de valeur |
| Personas + JTBD | Intercom / Christensen | Définit qui sont les utilisateurs et quels jobs ils font |
| North Star input metrics | Amplitude | Chaque feature candidate est testée : fait-elle bouger la North Star ? |
| Shape Up (pitches) | Basecamp | Pitch = appétit + solution + scope maigre · évite les specs sur-détaillées |
| Continuous Discovery | Teresa Torres | Discovery continu — le PRD est vivant, pas un document figé en début de projet |

---

## O3 — Négation talmudique

| Ce que PRD N'EST PAS | Document correct |
|---|---|
| Analyse marché ou sizing | MRD |
| Objectifs business et ROI | BRD |
| Architecture ou choix techniques | SRD |
| Prototype final ou maquette haute-fidélité | Design (Figma) |
| Document figé — les features changent avec la discovery | PRD est vivant |

---

## O4 — Formulaire science (ordre cognitif)

> Du concret vers l'abstrait. Chaque question s'appuie sémantiquement sur la précédente.

1. **Pour qui, quel problème, en 1 phrase ?** → Product Vision
2. **Qui sont les utilisateurs, quels jobs font-ils ?** → Personas + JTBD
3. **Que doit faire le produit exactement ?** → Features + User Stories
4. **Quel est le parcours complet (edge cases inclus) ?** → User Workflows
5. **Quelles contraintes perf/sécu/accès chiffrées ?** → Non-Functional Requirements
6. **Qu'est-ce qui est explicitement exclu de cette version ?** → Out of Scope

---

## Sommaire canonique

| Section | Question structurante | Garde-fou |
|---|---|---|
| **Product Vision** | Pour qui, quel problème, différenciateur clé — en 1 phrase ? | > 2 phrases = pas une vision |
| **Personas** | Qui sont les utilisateurs cibles ? Quels jobs-to-be-done ? | Personas sans comportements = décoratif |
| **Features & User Stories** | "En tant que [X], je veux [Y] pour [Z]" — avec acceptance criteria ? | Feature sans AC = non-testable |
| **User Workflows** | Parcours complet utilisateur avant/après, edge cases inclus ? | Workflow sans edge cases = incomplet |
| **Non-Functional Requirements** | Performance, sécurité, accessibilité, scalabilité chiffrés ? | NFR absents = découverts trop tard |
| **Out of Scope** | Qu'est-ce qui est explicitement exclu de cette version ? | Pas d'Out of Scope = scope illimité |

---

## Ker / Im

| | Contenu |
|---|---|
| **Ker** (reste dans PRD) | Personas · Wireframes/flows · Data models · API specs haut niveau · Performance requirements · Décisions UX |
| **Héritage R2 → PRD** | Impact Mapping · USM · JTBD · North Star |
| **Im → SRD via R3** | User Stories + Acceptance Criteria → Backlog Refinement |
