# ecosystem.html — PRD
*project-spec v1 · 2026-05-16 · source: BRD.md + ecosystem-prd.md*

---

## O1 — Formalisation

```
ecosystem_PRD : Ω_objectifs_produit → Ω_comportements_utilisateur
```

| | Contenu |
|---|---|
| **Domaine** | Objectifs mesurables du BRD (O1-O4) + scope IN délimité |
| **Codomaine** | Comportements utilisateur observables : 4 CU, features, workflows, out-of-scope |
| **Propriété** | Liant · le PRD connecte l'intention (BRD) à l'implémentation (SRD) via des cas d'usage testables |

---

## O2 — GAFAM best practices appliquées

| Pratique | Source | Application ecosystem |
|---|---|---|
| Job-To-Be-Done | Clayton Christensen | CU1-CU4 = JTBD concrets ("quand je veux X, je fais Y, pour obtenir Z") |
| User Story Mapping | Jeff Patton | Backbone = 4 CU ; stories = features par CU |
| Acceptance Criteria (Gherkin) | BDD community | DoD par feature = "Given/When/Then" implicite dans le workflow |
| "Fake door" + discovery signal | Teresa Torres | Onglet Nature = produit autonome latent — ne pas intégrer sans sprint dédié |
| Out-of-scope explicite | PM standard | Réduire ambiguïté de scope avant le SRD |

---

## O3 — Négation talmudique

| Ce que PRD N'EST PAS | Document correct |
|---|---|
| Architecture technique (fichiers, fonctions) | SRD.md |
| Objectifs business (OKRs) | BRD.md |
| Maquette ou prototype | Rendu = ecosystem.html lui-même |
| Contrat d'acceptation figé | Évolue avec la roadmap — chaque sprint peut ajouter CU5+ |
| Liste exhaustive des bugs | Task_plan.md (Errors section) |

---

## O4 — Formulaire science (ordre cognitif)

1. **Qui utilise le produit et dans quel contexte ?** → Audience + mode d'entrée
2. **Que veut-il accomplir en 1 session ?** → Job-To-Be-Done par CU
3. **Quel workflow suit-il pour y arriver ?** → User workflow par CU
4. **Quelles features rendent ce workflow possible ?** → Features par CU
5. **Qu'est-ce qui reste hors scope ?** → Out of scope explicite

---

## Sommaire canonique

### Audience

| Public | Mode d'entrée | CU principal |
|---|---|---|
| **Soi-même** | Direct (local HTML) | Tous — mémorisation + ontologie |
| **Jeunes en orientation IT** | Métaphore industrielle (Entrepôt Amazon) | CU1 Career Compass |
| **Professionnels IT** | Taxonomie formelle (rôles + concepts) | CU2, CU3, CU4 |
| **Recruteurs / LinkedIn** | Showcase public (GitHub Pages) | CU1, CU2 — preuve de maîtrise |

---

### CU1 — Career Compass

**JTBD :** "Quand je ne sais pas quel rôle IT correspond à qui je suis, j'utilise ecosystem.html pour m'orienter en < 2 min."

| Feature | Workflow | Status |
|---|---|---|
| F1.1 — Onglet Métiers avec cards rôles | Parcourir F1-F6 familles → trouver sa famille | ✅ livré |
| F1.2 — Card rôle avec narrative + zone | Lire la narrative "en 1 phrase" du rôle | ✅ livré |
| F1.3 — Pill rôle → goToRole() | Cliquer rôle → Atlas filtré sur ce rôle → voir théorèmes associés | ✅ livré |
| F1.4 — Role-as-Skill (Phase 13) | Cliquer rôle → invoquer skill Claude Code spécialisé | pending |

---

### CU2 — Job Decoder

**JTBD :** "Quand je lis une fiche de poste opaque, j'utilise ecosystem.html pour décomposer le jargon en taxonomie formelle."

| Feature | Workflow | Status |
|---|---|---|
| F2.1 — Atlas : 154 concepts browsable | Chercher un terme de la fiche → trouver sa définition formelle | ✅ livré |
| F2.2 — Filtre Atlas par type/famille/DAG/DDD | Filtrer par layer DDD → voir quels concepts sont concernés | ✅ livré |
| F2.3 — Colonne "rôles" dans Atlas | Voir quels rôles utilisent ce concept | ✅ livré |
| F2.4 — ROLE_PAIRS score ≥ 2 | Voir therorèmes associés au rôle mentionné dans la fiche | ✅ livré |

---

### CU3 — Org Mapper

**JTBD :** "Quand je rejoins une équipe inconnue, j'utilise ecosystem.html pour cartographier l'organisation avant d'arriver."

| Feature | Workflow | Status |
|---|---|---|
| F3.1 — Zones IT (Préfecture / Z001-Z008) | Visualiser les zones fonctionnelles d'une organisation | ✅ livré (viz statique) |
| F3.2 — Préfecture refonte 3D (Phase 12) | Cliquer zone → rôles + outils + théorèmes associés | pending |
| F3.3 — Filtre Atlas par rôle (supprimé C7b) | Filtré dans mart — mart_role_stack (Phase 11) | pending |

---

### CU4 — Agent Orchestration

**JTBD :** "Quand j'ai un problème technique, j'utilise ecosystem.html pour identifier quel rôle/skill invoquer."

| Feature | Workflow | Status |
|---|---|---|
| F4.1 — ROLE_PAIRS (computeRolePairs()) | Pour un concept → rôles matchés automatiquement | ✅ livré |
| F4.2 — Role-as-Skill mapping (Phase 13) | Rôle → skill Claude Code → workflow de domaine | pending |
| F4.3 — mart_role_stack (Phase 11) | Fiche complète rôle : théorèmes + outils + zones + DAG | pending |

---

### Out of Scope (PRD level)

| Exclusion | CU concerné | Décision |
|---|---|---|
| Onglet Nature (questionnaire projets) | aucun CU actuel | Produit autonome latent — sprint séparé |
| Comparaison multi-rôles côte-à-côte | CU1 extension | Phase 13+ |
| Export fiche de poste annotée | CU2 extension | Non planifié |
| Historique navigations / bookmarks | CU1-CU3 | LocalStorage acceptable, pas prévu v1 |
| Mobile responsive | Tous | Desktop-first v1 |

---

## Ker / Im

| | Contenu |
|---|---|
| **Ker** | 4 CU définis · Features statusées (livré / pending) · Workflows utilisateur décrits |
| **Im → SRD via R3** | Comportements utilisateur → implémentation : ATLAS_DATA · computeRolePairs() · renderAtlas() · structure HTML |
