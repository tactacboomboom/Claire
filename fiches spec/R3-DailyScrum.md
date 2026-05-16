# Daily Scrum
*doc-spec v1 · 2026-05-16 · protocole R3c (dans le sprint)*

---

## O1 — Formalisation

```
DailyScrum : Ω_sprint_state → Ω_plan_24h
```

| | Contenu |
|---|---|
| **Domaine** | État du sprint à J (progression vers le Sprint Goal, blocages) |
| **Codomaine** | Plan adapté pour les 24h suivantes + blocages remontés |
| **Propriété** | Synchroniseur · inspecte la trajectoire vers le Sprint Goal · adapte le Sprint Backlog si nécessaire · 15 min strictes |

---

## O2 — GAFAM best practices

| Pratique | Source | Apport |
|---|---|---|
| Daily Scrum (15 min) | Scrum Guide 2020 | Inspection + adaptation quotidienne — format libre si Sprint Goal inspecté |
| Stand-up militaire | US Army (origine) | Debout = court = focus |
| Focus Sprint Goal | Scrum Guide 2020 | Les 3 questions classiques supprimées — seul le Goal compte |
| Walking the board | Kanban / LeSS | Parcourir le board de droite à gauche (proche-Done → à-faire) |
| Async Daily | Remote teams | Slack/Loom update — évite le meeting si équipe distribuée |

---

## O3 — Négation talmudique

| Ce que Daily Scrum N'EST PAS | Document correct |
|---|---|
| Rapport de statut au management | One-on-one / Sprint Review |
| Réunion de résolution de problèmes | Spike / réunion ad-hoc après le Daily |
| Assignation de tâches par le Scrum Master | Auto-organisation de l'équipe |
| Présence obligatoire du PO | Dev-only event (PO peut écouter) |
| Mesure de performance individuelle | Rétro / évaluation RH |

---

## O4 — Format canonique

1. **Le Sprint est-il sur la bonne trajectoire vers le Sprint Goal ?** → Inspection
2. **Qu'est-ce qui a changé depuis hier qui nécessite d'adapter le plan ?** → Adaptation
3. **Y a-t-il des blocages à remonter hors du Daily ?** → Impediments

---

## Format canonique

| Critère | Règle | Garde-fou |
|---|---|---|
| **Durée** | 15 min strictes — même heure, même lieu | > 15 min = réunion de statut déguisée |
| **Focus** | Sprint Goal inspecté — pas les individus | "Qu'as-tu fait hier ?" = rapport de statut |
| **Participants** | Developers — PO et SM optionnels | SM qui anime = mauvaise habitude (équipe dépendante) |
| **Output** | Plan adapté pour 24h + impediments identifiés | Daily sans adaptation = rituel vide |

---

## Ker / Im

| | Contenu |
|---|---|
| **Ker** | Inspection quotidienne du Sprint Goal · Adaptation du Sprint Backlog · Impediments identifiés |
| **Im → Sprint Review** | Sprint Goal atteint ou non · Impediments résolus ou remontés |
