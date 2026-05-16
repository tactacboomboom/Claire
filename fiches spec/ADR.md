# ADR — Architecture Decision Record
*doc-spec v1 · 2026-05-16 · pipeline: fmaths + GAFAM + négation talmudique + formulaire science*

---

## O1 — Formalisation

```
ADR : Ω_décision → Ω_traçabilité
```

| | Contenu |
|---|---|
| **Domaine Ω_décision** | Contexte décisionnel : alternatives en présence, forces, contraintes, moment |
| **Codomaine Ω_traçabilité** | Décision tracée : choix + raison + conséquences documentées + statut |
| **Propriété** | Idempotent · ADR² = ADR — une décision documentée ne peut pas être redécidée sans nouveau ADR (l'ancien passe en "Deprecated") |

---

## O2 — GAFAM best practices

| Pratique | Source | Apport |
|---|---|---|
| Format MADR (Michael Nygard) | ThoughtWorks / GitHub | Status · Context · Decision · Consequences — format minimal universel |
| Y-Statements | ThoughtWorks | "In the context of X, facing Y, we decided Z, to achieve P, accepting Q" |
| ADRs dans le repo git | GitHub Engineering | Versionné avec le code — évolue au même rythme que l'architecture |
| RFC process | Google / Meta / Rust | Request for Comments avant adoption — collecte objections avant décision |
| Lightweight RFC | Mozilla / Basecamp | Format court pour décisions d'équipe sans comité d'architecture formel |

---

## O3 — Négation talmudique

| Ce que ADR N'EST PAS | Document correct |
|---|---|
| Spécification technique détaillée | SRD |
| Documentation d'implémentation | Code comments / README |
| Décision de scope ou de features | BRD / PRD |
| Meeting notes ou compte-rendu | CR de réunion |
| Backlog de tâches | Jira / SRD |

---

## O4 — Formulaire science (ordre cognitif)

> Du concret vers l'abstrait. Chaque question s'appuie sémantiquement sur la précédente.

1. **Dans quel contexte cette décision est-elle prise ?** → Context
2. **Quelle décision exacte a été prise ?** → Decision
3. **Quelles alternatives ont été évaluées et pourquoi rejetées ?** → Alternatives Considered
4. **Quelles sont les conséquences (positives et négatives) ?** → Consequences
5. **Quel est le statut de cette décision ?** → Status

---

## Sommaire canonique

| Section | Question structurante | Garde-fou |
|---|---|---|
| **Status** | Proposed / Accepted / Deprecated / Superseded by ADR-XXX ? | Status absent = ADR fantôme |
| **Context** | Quel problème, quelles forces en présence, quel moment ? | Context flou = décision injustifiable |
| **Decision** | Quelle décision exacte a été prise ? | Sans justification = copié-collé |
| **Alternatives Considered** | Quelles alternatives rejetées et pourquoi ? | Pas d'alternatives = biais de confirmation |
| **Consequences** | Quelles conséquences positives ET négatives acceptées ? | Conséquences ignorées = dette cachée |

---

## Ker / Im

| | Contenu |
|---|---|
| **Ker** (reste dans ADR) | Contexte décisionnel · Alternatives · Trade-offs · Raison du choix · Date |
| **Im → Code** | Contraintes architecturales à respecter dans l'implémentation · Conventions à suivre |
| **Position dans la chaîne** | Protocole interne au SRD — vit dans `docs/decisions/ADR-XXX.md` du repo |
