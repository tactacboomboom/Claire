# C4 Model — Architecture Visualization
*doc-spec v1 · 2026-05-16 · pipeline: fmaths + GAFAM + négation talmudique + formulaire science*

---

## O1 — Formalisation

```
C4 : Ω_système → Ω_compréhension
```

| | Contenu |
|---|---|
| **Domaine Ω_système** | Système logiciel complexe (composants, dépendances, acteurs, flux) |
| **Codomaine Ω_compréhension** | Représentation à 4 niveaux de zoom adaptée à chaque audience |
| **Propriété** | Projecteur · C4 projette le même système sur 4 plans orthogonaux sans perte d'information — chaque niveau est une restriction du précédent |

---

## O2 — GAFAM best practices

| Pratique | Source | Apport |
|---|---|---|
| C4 Model (4 niveaux) | Simon Brown (2010+) | Context → Container → Component → Code — zoom progressif |
| Structurizr | Simon Brown | Génère les diagrammes C4 depuis le code (DSL) — living documentation |
| AWS Well-Architected Diagrams | Amazon | Architecture diagrams comme artefacts de review |
| "Just enough architecture" | Microsoft Azure Patterns | Documenter l'essentiel, pas l'exhaustif |
| Living Documentation | ThoughtWorks | Diagrammes versionés dans le repo — évoluent avec le code |

---

## O3 — Négation talmudique

| Ce que C4 N'EST PAS | Document correct |
|---|---|
| Diagramme UML exhaustif (séquence, état, activité) | UML (outil différent) |
| Spécification technique | SRD / ADR |
| Documentation d'implémentation | Code comments / README |
| Diagramme figé — évolue avec le système | Living doc dans le repo |
| Vue unique — C4 EST 4 vues | Les 4 niveaux sont complémentaires |

---

## O4 — Formulaire science (ordre cognitif)

> Du macro vers le micro. Chaque niveau est un zoom sur le précédent.

1. **Qui utilise le système et comment (acteurs externes) ?** → L1 Context Diagram
2. **Quels conteneurs composent le système ?** → L2 Container Diagram
3. **Quels composants composent chaque conteneur ?** → L3 Component Diagram
4. **Comment le code implémente-t-il un composant clé ?** → L4 Code Diagram

---

## Sommaire canonique

| Niveau | Question structurante | Garde-fou |
|---|---|---|
| **L1 — Context** | Système + acteurs externes + interactions de haut niveau | Acteurs sans interactions = inutile |
| **L2 — Container** | Apps, DBs, microservices, files d'attente, canaux de communication | Container sans technologie nommée = flou |
| **L3 — Component** | Composants internes d'un container, leurs responsabilités, interfaces | Granularité trop fine = UML déguisé |
| **L4 — Code** | Classes/interfaces/fonctions implémentant un composant spécifique | Utiliser seulement pour composants critiques — pas par défaut |

---

## Ker / Im

| | Contenu |
|---|---|
| **Ker** (reste dans C4) | Topologie du système · Flux entre acteurs · Technologies choisies · Frontières de responsabilité |
| **Im → SRD / ADR** | Décisions d'architecture justifiées par le C4 · Contraintes d'implémentation identifiées |
| **Position dans la chaîne** | Livrable du SRD — vit dans `docs/architecture/` du repo, à jour via Structurizr |
