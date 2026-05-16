# Outils workflow Claude Code — Analyse & intégration CPE

> Source : session de recherche 2026-05-12
> Repos analysés via recommandation.

---

## Les 3 repos

### 1. Superpowers — `obra/superpowers`
**Rôle :** Framework de skills pour agents IA. Injecte des workflows structurés dans Claude Code.
**Installation :** Via le marketplace Claude Code (plugin officiel).
**14 skills disponibles :**
- `brainstorming` — Questions de clarification avant de coder
- `writing-plans` — Découpage en tâches de 2-5 min avec fichiers et specs complètes
- `executing-plans` — Exécution avec checkpoints
- `test-driven-development` — RED-GREEN-REFACTOR obligatoire
- `systematic-debugging` — Root cause analysis en 4 phases
- `requesting-code-review` / `receiving-code-review` — Workflow de review
- `using-git-worktrees` — Isolation du travail sur des branches propres
- `finishing-a-development-branch` — Merge/PR + cleanup
- `subagent-driven-development` — Délégation à des sous-agents
- `dispatching-parallel-agents` — Coordination multi-agents parallèles
- `verification-before-completion` — Validation avant de déclarer terminé
- `using-superpowers` — Introduction au framework
- `writing-skills` — Écrire ses propres skills

**Valeur ajoutée :** Remplace les bonnes intentions ("je vais faire du TDD") par des workflows enforced à chaque session.

---

### 2. Claude-Mem — `thedotmack/claude-mem`
**Rôle :** Système de mémoire persistante automatique cross-sessions pour Claude Code.
**Installation :** `npx claude-mem install`
**Fonctionnement — 5 hooks du cycle de vie :**
- `SessionStart` — Initialise le contexte au démarrage
- `UserPromptSubmit` — Prépare avant chaque prompt
- `PostToolUse` — Capture les résultats de chaque outil
- `Stop` — Gère les pauses
- `SessionEnd` — Finalise et stocke le résumé de session

**Stockage :** SQLite (FTS5 pour recherche keyword) + Chroma (vecteurs pour recherche sémantique).
**Stratégie "Progressive Disclosure" :** Récupère d'abord les IDs (~50-100 tokens), puis contexte chronologique, puis détails complets si nécessaire. Réduction de ~90% de la consommation de tokens.
**Privacy :** Balises `<private>` pour exclure du contenu sensible.
**Config :** `~/.claude-mem/settings.json`
**Stack technique :** 100% TypeScript/Node.js. Chroma tourne en Python via API HTTP.

**Maths derrière la compression :**
- Résumé LLM via l'API Claude (pas de SVD/PCA runtime).
- Embeddings denses (~768 dims, sentence-transformers) avec similarité cosinus.
- Index HNSW pour le k-NN approximé.
- SQLite FTS5 utilise BM25 (extension de TF-IDF) pour la recherche keyword.

---

### 3. Graphify — `safishamsi/graphify`
**Rôle :** Transforme un codebase entier en knowledge graph queryable.
**Installation :** `uv tool install graphifyy && graphify install`
**Commandes clés :**
```bash
/graphify .                          # Construire le graph du dossier courant
/graphify . --update                 # Mise à jour incrémentale (fichiers changés seulement)
/graphify query "auth flow"          # Requête en langage naturel
/graphify path "ServiceA" "ServiceB" # Chemin le plus court entre deux concepts
graphify hook install                # Rebuild automatique sur git commit
graphify export callflow-html        # Diagrammes d'architecture
```

**Fichiers générés :**
- `graph.html` — Visualisation interactive (vis.js, forceAtlas2Based layout)
- `GRAPH_REPORT.md` — God nodes, connexions inattendues, rationale de design
- `graph.json` — Graph complet requêtable sans re-extraction

**Combinaison avec DDD / OOP / GoF / SOLID :**
| Concept | Usage avec Graphify |
|---|---|
| DDD | Les clusters isolés dans le graph = bounded contexts candidats |
| SOLID | Les god nodes (trop de connexions) = violations SRP/ISP visibles |
| GoF | `/graphify query "observer pattern"` remonte les implémentations |
| OOP | Arêtes `extends/implements` forment la hiérarchie de classes navigable |

**Privacy :** Code traité localement (tree-sitter AST).

---

## Workflow — Sprints en parallèle avec Git Worktrees

**Principe :** 1 sprint = 1 branche = 1 worktree = 1 agent. Deux agents sur la même branche = catastrophe.

```bash
git worktree add ../projet-sprint1 -b feature/sprint-1
git worktree add ../projet-sprint2 -b feature/sprint-2

# Terminal 1
cd ../projet-sprint1
claude "Sprint 1 — [contexte complet : objectif, fichiers concernés, critères de done]"

# Terminal 2
cd ../projet-sprint2
claude "Sprint 2 — [contexte complet : objectif, fichiers concernés, critères de done]"
```

**3 questions avant de paralléliser :**
1. Les sprints touchent-ils les mêmes fichiers ? → séquencer si oui
2. Sprint B dépend-il du résultat de Sprint A ? → séquencer si oui
3. Migration DB ou changement de config globale ? → toujours séquentiel

---

## Analyse — Intégration dans le workflow CPE

### claude-mem — priorité haute

C'est le plus immédiatement utile. Il automatise ce que `task_plan.md` / `findings.md` font manuellement : capturer les faits bruts de session.

**Mais** il ne remplace pas le raisonnement N1-N4. claude-mem capture *ce qui s'est passé*. Le pipeline CPE extrait *ce que ça signifie*. Les deux sont complémentaires :
- claude-mem = couche de capture (automatique, exhaustif)
- N1-N4 = couche de sens (manuel, sélectif)

La reduction ~90% tokens via Progressive Disclosure est directement alignée avec les règles P5/P6 du skill ecosystem-sprint.

### superpowers — priorité moyenne

`writing-plans` et `verification-before-completion` ressemblent fortement au protocole CPE (Goal → Backlog → DoD). À comparer ligne à ligne avec `/cpe-sprint` pour voir si :
- leurs patterns enrichissent le contrat CPE
- ou si `/cpe-sprint` est déjà plus précis (scoring μA/μV, binôme review)

`dispatching-parallel-agents` + `using-git-worktrees` = infrastructure pour les sprints parallèles futurs (Phase 5 claire-app).

### graphify — priorité basse (court terme)

Utile uniquement quand `claire-app` aura suffisamment de code pour justifier une analyse de dépendances. Pertinent pour Phase 5 (refactor SOLID-compliant) : graphify révèle visuellement les violations SRP/ISP avant de toucher au code.

À revisiter quand claire-app dépasse ~10 fichiers sources.
