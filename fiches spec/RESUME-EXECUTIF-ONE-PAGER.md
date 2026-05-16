# RÉSUMÉ EXÉCUTIF — ATLAS DOCUMENTATION PRODUIT
## Comment utiliser ce système complet

---

## TL;DR : La Structure en 30 secondes

**4 documents**, **une chaîne**, **3 socles immuables** :

```
MRD (Pourquoi ?)  →  BRD (Stratégie)  →  PRD (Features)  →  SRD (Architecture)  →  CODE
  Marché              Business           Produit             Technique            Impl.
  Stable              Moyen              Court               Court                Vivant
  1 ans+              1-2 trim           1-2 sprints         1 sprint             Continu
```

**Les 3 socles** : Intention cohérente + Traçabilité bidirectionnelle + Non-redondance.

**Les 4 ruptures** : MRD→BRD, BRD→PRD, PRD→SRD, SRD→Code. À chaque rupture, validation requise.

---

## Les 4 Fichiers Delivérés

| Fichier | Type | Quand l'utiliser | Longueur |
|---------|------|------------------|----------|
| **FMATHS Passe 1** | Analyse formelle | Quand tu veux comprendre la structure sous-jacente (Ensembles, Logique, Invariants, Topologie) | Long (~5000 words) |
| **FMATHS Passe 2** | Narration narrative | Quand tu veux lire une explication organique, comme un essai/podcast | Long (~6000 words) |
| **ATLAS Synthèse** | Fusion + templates | **CELUI-CI EN PREMIER** — contient tout + templates prêts à utiliser + workflow opérationnel | Très long (~8000 words) |
| **Interactive Map (HTML)** | Visualisation | Quand tu veux naviguer visuellement, voir tabs, relations entre documents | Interactive |

**Recommandation d'ordre de lecture** :
1. Lis **cette page** (30 sec)
2. Ouvre **Interactive Map (HTML)** (2 min) — pour voir les relations visuellement
3. Pour un nouveau projet → utilise **ATLAS Synthèse** (c'est le workflow exact)
4. Si tu veux la rigueur → lis **FMATHS Passe 1** ou **Passe 2** (selon si tu préfères formule ou narrative)

---

## Situation : Tu commences un nouveau projet

### ÉTAPE 1 : MRD (15 min)

**Tu** + **Product Owner / Executive**

**Remplis** :
```markdown
# PROJECT CHARTER

## Problem Statement
- Quel est le problème réel ? (data-based, pas intuition)
- Qui le souffre le plus ? (segmentation)
- À quelle fréquence ? (magnitude)
- Quel coût si on ne résout pas ? (urgency)

## Market Opportunity
- Market size (TAM/SAM/SOM)
- Growth rate

## Success Metrics
- Primary metric que prouverait qu'on a résolu le problème
- Secondary metrics
```

**Validation** : ✓ Problème est réel | ✓ Nous pouvons le résoudre | ✓ Success metrics mesurables

---

### ÉTAPE 2 : BRD (40-50 min brainstorm)

**Tu** + **PM** + **Execs** (stakeholder alignment)

**Pont avec MRD** : "Le MRD décrit le marché entier. Nous, quel segment on cible ?"

**Remplis** :
```markdown
# BRD — Business Requirements

## Business Objectives
- Primary goal (métrique de succès business)
- Target segments (lequel du MRD on vise réellement)

## Business Case
- Revenue model
- Timeline to profitability
- Investment required
- ROI projection

## Phase 1 Scope
- In: [Features/problèmes on résout]
- Out: [Features/problèmes for phase 2+]
```

**Validation** : 
- ✓ Chaque objectif BRD trace au MRD
- ✓ Scope est clairement défini ("phase 1" vs "future")
- ✓ Stakeholders sont alignés

---

### ÉTAPE 3 : PRD (50 min brainstorm)

**Tu** + **PM** + **UX Designer**

**Pont avec BRD** : "L'objectif business est clair. Comment en features ? Quelles fonctionnalités le réalisent ?"

**Remplis** :
```markdown
# PRD — Product Requirements

## Personas
- Qui utilise ?
- Quels pain points ?

## Features (Phase 1)
### Feature X
- User story
- Acceptance criteria (testables, précis)

## User Workflows
- Step-by-step pour chaque persona
- Happy path + edge cases

## Out of Scope
- Ce qu'on ne fait PAS
```

**Validation** : 
- ✓ Chaque feature trace à un objectif BRD
- ✓ User workflows sont testables
- ✓ Acceptance criteria sont précis

---

### ÉTAPE 4 : SRD (50 min brainstorm)

**Tu** + **Tech Lead** + **Architect**

**Pont avec PRD** : "Chaque feature est claire. Techniquement, comment on la construit ?"

**Remplis** :
```markdown
# SRD — Software Requirements

## System Architecture
- Components (Frontend, Backend, Database, etc.)
- Diagram (ASCII ok)

## Technology Choices & Trade-offs
| Decision | Choice | Reason | Sacrifice |
|----------|--------|--------|-----------|
| Database | SQLite | MVP simplicity | Scale limits |
| API | REST | Easy to cache | Over-fetching |

## Data Model
- SQL schema (tables, relationships)

## API Specification
- GET /endpoint → response format
- POST /endpoint → request format

## Non-Functional Requirements
- Performance: <500ms latency
- Scalability: 10k users min
- Security: OAuth, encryption, rate limiting
```

**Validation** : 
- ✓ Chaque feature PRD peut être implémentée
- ✓ Trade-offs explicites
- ✓ Performance targets mesurables

---

### ÉTAPE 5 : Checklist Cohérence (10 min)

**Avant de coder, vérifie** :

✓ **Cohérence MRD ↔ BRD**
- Chaque problème du MRD adressé dans le BRD ?
- BRD justifie la réduction de scope ?

✓ **Cohérence BRD ↔ PRD**
- Chaque objectif a une feature qui l'adresse ?
- Pas de features "orphelines" ?

✓ **Cohérence PRD ↔ SRD**
- Chaque feature peut être implémentée ?
- Performance targets réalistes ?

✓ **Traçabilité Bidirectionnelle**
- ✗ Requirement orphelin = construction inutile
- ✗ Problème non-couvert = spec incomplète

✓ **Absence de Redondance**
- MRD ≠ BRD | BRD ≠ PRD | PRD ≠ SRD
- Chaque document un rôle unique

---

### ÉTAPE 6 : Coding avec Claude Code (120+ min)

**Copie-colle le SRD complet dans Claude Code** :

```
SITUATION :
Projet: [nom]
Stack: [tech choices du SRD]
Artefacts fournis (ci-dessous) :
[Colle PRD complèt]
[Colle SRD complet]
[Colle checklist]

TA MISSION : Construis tout en une session sans poser de questions.
Si ambiguïté : référence-toi au SRD/PRD, ne demande pas de clarif.
```

**Résultat** : Code prêt à déployer, minimal aller-retour.

---

## Situation : Ton projet est en difficulté

**Diagnostic via les 4 ruptures** :

### "Le code ne matche pas le PRD"
→ **Rupture 3 cassée** (SRD incomplet / irréaliste)
→ Retour à l'architecture
→ Question : Cette feature est vraiment faisable ? À quel coût ?

### "Le PRD a trop de features et on peut pas les livrer"
→ **Rupture 2 cassée** (PRD sur-spécifié)
→ Retour au BRD
→ Question : Laquelle de ces features adresse vraiment l'objectif business ?

### "On a des features cool mais inutiles"
→ **Rupture 2 cassée** (Features orphelines)
→ Retour au BRD
→ Question : Quel objectif BRD cette feature adresse-t-elle ? Si aucun, coupe-la.

### "Personne ne sait pourquoi on fait ce produit"
→ **Rupture 1 cassée** (MRD/BRD désalignés)
→ Retour au charter et revalidation avec execs
→ Question : Le problème du MRD, c'est vraiment celui qu'on veut résoudre ?

---

## Les 3 Socles Immuables (Ne jamais violer)

### Socle 1 : Cohérence d'Intention
**Même idée à chaque niveau, juste plus détaillée.**

❌ **Mauvais** :
```
MRD: "Fragmenté" 
BRD: "Plateforme unifiée"
PRD: "3 services découplés"
SRD: "3 databases indépendantes"
→ Code : Services ne partagent rien
```
Résultat : "Plateforme unifiée" qui est techniquement fragmentée. Intention perdue.

✓ **Bon** :
```
MRD: "Fragmenté" 
BRD: "Intégration facile"
PRD: "Features interconnectées"
SRD: "API qui se parlent, data partagée"
→ Code : Vraiment intégré
```

### Socle 2 : Traçabilité Bidirectionnelle
**Vers le bas** : Chaque requirement trace à une feature.
**Vers le haut** : Chaque feature trace à un objectif.

❌ **Mauvais** : Requirement "JWT validation" dans SRD, mais aucune feature PRD ne la demande.
✓ **Bon** : Feature PRD "Secure login" → SRD "Implement JWT validation"

### Socle 3 : Non-Redondance
**Chaque document a un rôle unique.**

❌ **Mauvais** : BRD spécifie des features. (C'est le job du PRD)
✓ **Bon** : BRD dit "Augmenter rétention". PRD dit "Comment : Feature X, Y, Z".

---

## Les 5 Axes de Variation (Où chaque document se situe)

```
      Abstrait ←———————————→ Concret
        ↓                        ↓
       MRD                      SRD
      "Market"               "WebSocket"

      Business ←——————————→ Technical
        ↓                      ↓
     BRD/MRD                 SRD
    "Rétention"           "Redis cache"

    WHAT ←——————————————————→ HOW
      ↓                        ↓
   MRD/BRD/PRD              SRD
  "Résoudre X"          "Via architecture Y"

   Large ←———————————————→ Narrow
    Scope                   Scope
      ↓                        ↓
   Marché entier          Une feature
```

Chaque document occupe un endroit différent dans cet espace multidimensionnel.

---

## Concepts Clés

### **Dette d'Intention**
Gap entre ce qu'on voulait faire (MRD) et ce qu'on a fait (Code).
**S'accumule à chaque rupture** si on n'est pas vigilant.

Exemple :
```
MRD: "Plateforme collaborative"
BRD: "Pour les startups"
PRD: "Chat, files, calendar"
SRD: "3 microservices"
Code: "Services qui ne se parlent pas"

Intention originale : "Collaborative"
Intention finale : "Fragmented"
→ Dette d'intention = 100%
```

### **Révélateur d'Implicites**
Le développeur découvre les choses que les specs ont oubliées.
**C'est pas un bug, c'est un diagnostic.**

"Le code révèle que la spec était incomplète" → Occasion d'améliorer le process pour les futurs projets.

### **Entropie Informationnelle**
Ambiguïté diminue à chaque phase.

MRD: "Plusieurs interprétations possibles"
→ BRD: "Moins d'interprétations"
→ PRD: "Presque une seule interprétation"
→ SRD: "Exécutable directement"
→ Code: "Zéro ambiguïté"

Si l'ambiguïté augmente à une étape, tu as un problème.

### **Feedback Loop**
Code révèle que SRD était irréaliste → revoir SRD → revoir PRD → ...

**Normal.** Mais doit être court (quelques itérations, pas des semaines).

Si tu réécris la BRD chaque semaine, quelque chose s'est mal passé au départ.

---

## Checklist Avant Coding

### ✓ Documents Complets
- [ ] MRD couvert tous les problèmes
- [ ] BRD couvert tous les objectifs business
- [ ] PRD couvert toutes les features nécessaires
- [ ] SRD couvert toute l'architecture

### ✓ Pas de Contradictions
- [ ] Aucun statement du PRD contredit le BRD
- [ ] Aucun statement du SRD contredit le PRD
- [ ] Performance targets du SRD sont réalistes pour le scope

### ✓ Traçabilité
- [ ] Chaque feature du PRD traces à au moins un objectif BRD
- [ ] Chaque requirement du SRD traces à au least une feature PRD
- [ ] Chaque objectif BRD addresses un problème MRD

### ✓ Validation Stakeholders
- [ ] Execs validé le MRD
- [ ] Stakeholders validé le BRD
- [ ] PM validé le PRD
- [ ] Tech Lead validé le SRD

### ✓ Readiness
- [ ] Pas de "TBD" ou "TK" majeur
- [ ] Tous les endpoints API listés
- [ ] Data model complet
- [ ] Non-functionals mesurables

---

## Les 4 Ruptures & Comment les Valider

```
MRD                          Validation Check
 ↓ [RUPTURE 1]              "MRD et BRD disent-ils la même chose ?"
BRD                          BRD réduit le scope ? C'est intentionnel ?
 ↓ [RUPTURE 2]              "BRD objectifs et PRD features alignés ?"
PRD                          Chaque feature adresse un objectif ?
 ↓ [RUPTURE 3]              "PRD features et SRD architecture compatible ?"
SRD                          Réaliste pour le timeframe ?
 ↓ [RUPTURE 4]              "Code peut-il implémenter le SRD ?"
CODE                         Développeur découvre-t-il des implicites ?
```

À chaque rupture → valider avant d'avancer.

---

## Résumé : Comment utiliser cet atlas

### Pour un nouveau projet
1. **15 min** : Remplis le MRD
2. **40 min** : Brainstorm BRD avec stakeholders
3. **50 min** : Brainstorm PRD avec PM/UX
4. **50 min** : Brainstorm SRD avec Tech Lead
5. **10 min** : Checklist cohérence
6. **120+ min** : Coding sans friction

**Total temps non-coding** : ~3 heures pour specs complètes et validées.
**Résultat** : Code prêt, zéro aller-retour.

### Pour débugger un problème existant
Utilise les 4 ruptures comme diagnostic :
- Code ≠ PRD ? → Rupture 3 cassée
- PRD ≠ Objectifs biz ? → Rupture 2 cassée
- Features orphelines ? → Rupture 2 cassée
- Personne sait pas pourquoi ? → Rupture 1 cassée

Identifie la rupture → remonte et reclarifie.

### Pour comprendre la structure mathématiquement
Lis **FMATHS Passe 1** (Ensembles, Logique, Invariants, Topologie, Probabilités).

### Pour comprendre la structure narrativement
Lis **FMATHS Passe 2** (9 actes, podcast-style, zéro symboles).

---

## Deeplinks vers les Concepts Avancés

| Concept | Où le trouver |
|---------|---|
| **Dette d'Intention** | FMATHS Passe 2, Acte 5, Section "Rupture 4" |
| **Révélateur d'Implicites** | FMATHS Passe 2, Acte 5, Intro + Acte 9 |
| **Topologie : Entonnoir + Feedback** | FMATHS Passe 1, Section 7; Passe 2, Acte 7 |
| **Entropie Informationnelle** | FMATHS Passe 1, Section 8; Passe 2, Acte 8 |
| **Les 3 Socles** | FMATHS Passe 1, Section 3; Passe 2, Acte 2 |
| **Les 5 Axes** | FMATHS Passe 1, Section 4; Passe 2, Acte 3 |
| **Ruptures Détaillées** | FMATHS Passe 1, Section 5; Passe 2, Acte 1 |

---

## Fichiers Fournis

Tous dans `/outputs/` :

1. **FMATHS-DOCUMENTATION-PRODUIT-PASSE1.md** — 8 sections d'analyse formelle
2. **FMATHS-DOCUMENTATION-PRODUIT-PASSE2.md** — 9 actes de narration
3. **ATLAS-DOCUMENTATION-PRODUIT-SYNTHESE.md** — Fusion fmaths + templates + workflows (CELUI À UTILISER POUR LES PROJETS)
4. **DOCUMENTATION-PRODUIT-INTERACTIVE-MAP.html** — Visualisation interactive
5. **PROTOCOL-BRAINSTORM-SPECS.md** — 6 phases opérationnelles (bonus, fourni avant)
6. **CE FICHIER** — Résumé exécutif one-pager

---

## Derniers Mots

Cette cartographie t'a pris longtemps à lire si tu as tout consumé. Mais une fois que tu l'as internalisé :

- **MRD est le fondement** : Si le MRD est mauvais, tout ce qui suit s'écroule.
- **BRD c'est la traduction** : Du marché à la stratégie interne. Ça doit justifier la réduction de scope.
- **PRD c'est le choix** : Des objectifs aux features. Il y a plusieurs réponses possibles.
- **SRD c'est la contrainte** : Des features à l'architecture. Les trade-offs sont conscients.
- **Code c'est la réalité** : Révélateur d'implicites. Feedback loops courtes.

Les 3 socles (Intention, Traçabilité, Non-redondance) ne peuvent JAMAIS être violés.

Les 4 ruptures sont les points de validation. À chacune, tu dois valider.

Les 5 axes expliquent pourquoi les documents ne peuvent pas être écrits identiquement.

Le système entier est un **contrôle de cohérence multi-étapes** : maximiser la chance que ce qu'on livre correspond à ce qu'on voulait.

C'est tout. Bon courage sur tes projets.
