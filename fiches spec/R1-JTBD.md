# JTBD — Jobs To Be Done
*doc-spec v1 · 2026-05-16 · protocole R1 (MRD → BRD) + R2 (BRD → PRD)*

---

## O1 — Formalisation

```
JTBD : Ω_comportement → Ω_motivation
```

| | Contenu |
|---|---|
| **Domaine** | Comportement observable du client (ce qu'il fait, ce qu'il achète) |
| **Codomaine** | Motivation sous-jacente (le "job" qu'il essaie d'accomplir dans sa vie) |
| **Propriété** | Révélateur · expose la causalité réelle derrière l'achat/usage — stable quand les solutions changent |

> "People don't buy a quarter-inch drill, they buy a quarter-inch hole." — Theodore Levitt

---

## O2 — GAFAM best practices

| Pratique | Source | Apport |
|---|---|---|
| Jobs-to-be-Done theory | Clayton Christensen / HBS | Le client "embauche" un produit pour accomplir un job — stable dans le temps |
| Job Stories (vs User Stories) | Alan Klement / Intercom | "When [situation], I want to [motivation], so I can [outcome]" |
| Switch Interview | Bob Moesta / ReWired | Interview sur le moment de l'achat — révèle le job réel et les "pushes/pulls" |
| JTBD Timeline | Strategyn | Carte des 85 jobs universels par catégorie (functional, emotional, social) |
| "Milkshake Study" | Christensen | Étude classique — les clients embauchent le milkshake pour le trajet matinal ennuyeux |

---

## O3 — Négation talmudique

| Ce que JTBD N'EST PAS | Document correct |
|---|---|
| Persona (description démographique) | Persona PRD |
| User story (tâche à accomplir dans le produit) | User Story PRD/SRD |
| Feature request (solution proposée) | Backlog |
| Customer journey map (séquence d'étapes) | UX mapping |
| Besoin exprimé par le client | JTBD va plus loin — le client ne sait pas son job |

---

## O4 — Format canonique

1. **Dans quelle situation le client se trouve-t-il ?** → Situation
2. **Quel progrès essaie-t-il d'accomplir dans sa vie ?** → Functional Job
3. **Comment veut-il se sentir en accomplissant ce job ?** → Emotional Job
4. **Comment veut-il être perçu par les autres ?** → Social Job
5. **Ce que le client utilisait avant (et pourquoi il changerait) ?** → Competing solution + pushes/pulls

---

## Format canonique (Job Story)

```
When [situation déclenchante],
I want to [motivation — progrès désiré],
So I can [outcome — résultat dans ma vie].
```

| Composant | Question | Garde-fou |
|---|---|---|
| **Situation** | Quel contexte déclenche le besoin ? | Situation trop générale = job flou |
| **Motivation** | Quel progrès fonctionnel veut-on faire ? | Solution déguisée = pas un job |
| **Outcome** | Quel résultat dans la vie (pas dans le produit) ? | Outcome = feature → trop étroit |

---

## Ker / Im

| | Contenu |
|---|---|
| **Ker** | Jobs stables · Motivations fonctionnelles/émotionnelles/sociales · Competing solutions |
| **Im → R1 (BRD)** | Segments validés par job · Problem Statement ancré dans un job réel |
| **Im → R2 (PRD)** | Filtre de priorisation features : "quel job cette feature sert-elle ?" |
