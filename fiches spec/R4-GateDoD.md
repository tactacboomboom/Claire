# Gate DoD — Definition of Done
*doc-spec v1 · 2026-05-16 · gate R4 (Code → Incrément livrable)*

---

## O1 — Formalisation

```
DoD : Ω_incrément_candidat → {0, 1}  (Done / non-Done)
```

| | Contenu |
|---|---|
| **Domaine** | Incrément candidat à la présentation en Sprint Review |
| **Codomaine** | Décision binaire : Done (1) ou non (0) |
| **Propriété** | Gate de sortie · décision binaire déterministe · standard org-level (pas seulement équipe) · peut être renforcé en Rétrospective, jamais assoupli |

---

## O2 — GAFAM best practices

| Pratique | Source | Apport |
|---|---|---|
| Definition of Done | Scrum Guide 2020 | Standard organisationnel minimal — l'équipe peut ajouter, jamais réduire |
| "Potentially Shippable" | Scrum Guide | Chaque Incrément Done = potentiellement livrable en prod |
| DoD + CI/CD gates | Google / Netflix | Tests verts + review passée + déployé en staging = DoD automatisable |
| "Done means Done" | Scrum community | Aucune exception — si non-Done, pas dans la Review |
| DoD renforcé par Retro | Scrum Guide 2020 | La Rétro peut élever le DoD — jamais l'abaisser |

---

## O3 — Négation talmudique

| Ce que DoD N'EST PAS | Document correct |
|---|---|
| Definition of Ready (critères d'entrée) | Gate DoR (R3) |
| Acceptance Criteria d'une story spécifique | AC dans la User Story (PRD/SRD) |
| Contrat figé — peut être renforcé en Rétro | DoD évolue vers plus d'exigence |
| Check-list optionnelle | DoD = non-négociable — skip = dette cachée |
| Standard d'équipe seulement | DoD org-level + couche équipe (plus strict) |

---

## O4 — Format canonique

1. **Le code est-il reviewé par un pair ?** → Critère Code Review
2. **Les tests automatisés passent-ils ?** → Critère Tests
3. **La documentation est-elle mise à jour ?** → Critère Docs
4. **L'Incrément est-il déployé en staging ?** → Critère Déploiement
5. **Les NFR du PRD sont-ils respectés ?** → Critère Performance/Sécu

---

## Format canonique (checklist org-level)

| Critère | Vérification | Garde-fou |
|---|---|---|
| **Code Review** | Approuvé par ≥ 1 pair | Non-reviewé = dette technique non-auditée |
| **Tests** | Tests unitaires + intégration verts en CI | Aucun test = DoD non-automatisable |
| **Documentation** | README / ADR / changelog mis à jour | Doc non-mise-à-jour = connaissance perdue |
| **Staging** | Déployé et fonctionnel en staging | Non-déployé en staging = surprise en prod |
| **NFR** | Performance / sécurité / accessibilité vérifiés | NFR ignorés = dette PRD |

---

## Ker / Im

| | Contenu |
|---|---|
| **Ker** | Checklist non-négociable · Standard org-level · Révisable uniquement à la hausse (Rétro) |
| **Im → Sprint Review** | Seuls les Incréments Done sont présentés — intégrité du feedback garantie |
| **Im → Rétrospective** | DoD peut être renforcé lors de la Rétro si l'équipe grandit en maturité |
