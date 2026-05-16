# FMATHS — DOCUMENTATION PRODUIT
## Passe 1 : Formalisme Mathématique

**Sujet** : L'univers de la documentation produit (MRD, BRD, PRD, SRD)  
**Tension d'entrée** : Chaque document prétend décrire le *même objet* (le produit) mais à des niveaux d'abstraction radicalement différents. Or ces niveaux ne s'empilent pas simplement — ils entrent en tension. Comment la cohérence est-elle garantie ?  
**Opérateurs mathématiques** : Théorie des catégories (morphismes, foncteurs) + Ordres partiels (posets) + Topologie des espaces de projection

---

## 1. ENSEMBLES — Le Décor (Ontologie minimale, fermée, générative)

### 1.1 Ensemble fondamental : les Documents
```
DOC = { MRD, BRD, PRD, SRD }
```

### 1.2 Ensemble des audiences (destinataires)
```
AUDIENCE = { Marketing, Product Manager, Business Analysts, Developers, Testers, Architects }
```

### 1.3 Ensemble des problèmes/niveaux d'analyse
```
PROBLEM_LEVELS = {
  Market    → "Quel est l'espace de marché ? Qui sont les concurrents ?",
  Business  → "Quel est le business case ? Comment aligner les stakeholders ?",
  Product   → "Quelles fonctionnalités résoudront le problème utilisateur ?",
  Technical → "Comment construire les fonctionnalités ? Quelles sont les contraintes ?"
}
```

### 1.4 Ensemble des dimensions de chaque document
```
DIMENSIONS = { Purpose, Key Focus, Audience, Scope, Level of Detail, Ownership, Timeline }
```

### 1.5 Ensemble des transitions attendues
```
TRANSITIONS = {
  MRD → BRD : (Market opportunity) → (Business case),
  BRD → PRD : (Business goals) → (User requirements),
  PRD → SRD : (Functional specs) → (Technical specs),
  ALL → Implementation : (Specs) → (Code)
}
```

### 1.6 Ensemble des invariants de cohérence interne
```
COHERENCE = {
  c_alignment : (Intent in MRD) ≡ (Intent in BRD) ≡ (Intent in PRD) ≡ (Intent in SRD),
  c_coverage : (Problem defined) ⟹ (Solution covers all aspects),
  c_traceability : (Every requirement) traces back to a problem statement,
  c_non_contradiction : ¬(contradictory specs across documents)
}
```

---

## 2. LOGIQUE — Les Règles du Jeu (Gouvernance du monde documentaire)

### 2.1 Règles d'existence : chaque document existe ssi

```
MRD existe ⟺ ∃ market opportunity + ∃ customer needs

BRD existe ⟺ MRD existe ∧ ∃ business objectives ∧ ∃ stakeholder alignment

PRD existe ⟺ BRD existe ∧ ∃ user stories ∧ ∃ acceptance criteria

SRD existe ⟺ PRD existe ∧ ∃ technical architecture ∧ ∃ non-functional requirements

Code existe ⟺ SRD existe ∧ ∃ implementation plan ∧ ∃ test strategy
```

### 2.2 Règles de transformation : flot d'information

```
MRD → BRD : 
  Input  = (market_opportunity, customer_segments, success_metrics)
  Output = (business_case, stakeholder_requirements, scope)
  Invariant preserved = "Why we're building this"

BRD → PRD :
  Input  = (business_goals, stakeholder_scope, constraints)
  Output = (user_stories, functional_requirements, acceptance_criteria)
  Invariant preserved = "What we're building"

PRD → SRD :
  Input  = (functional_specs, user_flows, edge_cases)
  Output = (architecture, technical_constraints, API_design)
  Invariant preserved = "How we're building this"
```

### 2.3 Règles de validité : each document must satisfy

```
∀ doc ∈ DOC : 
  - ∃ clear_purpose(doc)
  - ∃ defined_audience(doc)
  - consistent(problem_statement(doc), solution_proposed(doc))
  - ¬ undefined_terms(doc)  [pas d'ambiguïté]
  - traceable_to_previous(doc)  [lien vers doc précédent]
```

### 2.4 Règles de non-contradiction globale

```
∀ two_docs_in_sequence(d1, d2) :
  ¬ ∃ statement_s : 
    (claims_s(d1) = True) ∧ (claims_s(d2) = False)
  
Exemple : Si MRD dit "feature X résout le problème",
          alors PRD NE PEUT PAS dire "feature X n'existe pas"
```

---

## 3. INVARIANTS — Le Socle Immuable (Résiste à tous les transformations)

### 3.1 Invariant de l'intention
```
INTENT_INVARIANT :
  Tout document, peu importe son niveau d'abstraction,
  doit pouvoir répondre à "Pourquoi construit-on ceci ?"
  
  La réponse aux différents niveaux doit être COHÉRENTE SYNTAXIQUEMENT
  même si elle varie en détail.
  
  Exemple :
  MRD : "Résoudre la fragmentation du marché de la collaboration"
  BRD : "Offrir une plateforme unique pour équipes distribuées"
  PRD : "Features: chat, files, calendar → unified workspace"
  SRD : "Microservices: chat-svc, file-svc, calendar-svc"
  
  Tous disent la même chose (unified), juste à des niveaux différents.
```

### 3.2 Invariant de la traçabilité
```
TRACEABILITY_INVARIANT :
  ∀ requirement_in_SRD : ∃ functional_feature_in_PRD_that_requires_it
  ∀ feature_in_PRD : ∃ user_story_in_PRD ∧ ∃ business_goal_in_BRD
  ∀ goal_in_BRD : ∃ market_opportunity_in_MRD
  
  La traçabilité est une DAG (Directed Acyclic Graph) :
  Market → Business → Product → Technical → Code
  
  Aucun cycle permis : un requirement ne peut pas justifier sa propre existence.
```

### 3.3 Invariant de la non-redondance stratégique
```
NON_REDUNDANCY_INVARIANT :
  MRD answer "Why + Who" (market side)
  BRD answer "What business goals" (stakeholder side)
  PRD answer "What features" (user side)
  SRD answer "How to build" (developer side)
  
  Chaque document a un rôle unique.
  Si deux documents répondent à la même question, c'est une redondance.
```

### 3.4 Invariant de l'exhaustivité locale
```
EXHAUSTIVITY_INVARIANT :
  ∀ document : doit couvrir TOUT ce qui est de sa responsabilité
  
  PRD ne doit pas laisser des questions "Et ce cas edge ?"
  SRD ne doit pas laisser "Et comment on déploie ?"
  
  Chaque document clôt son univers de responsabilité.
```

---

## 4. AXES DE VARIATION — Ce qui change selon le contexte/l'angle

### 4.1 Axe ABSTRACTION ↔ CONCRÉTION
```
MRD (abstract) ← → SRD (concrete)

MRD : "Les équipes perdent du temps à coordonner"
PRD : "Intégrer un système de notification temps-réel"
SRD : "WebSocket connection → event stream → Redis pub/sub → DB writes"

La même idée, dilatée/contractée selon le grain de détail.
```

### 4.2 Axe BUSINESS ↔ TECHNICAL
```
MRD/BRD (business perspective) ← → PRD/SRD (technical perspective)

Business angle : "Augmenter la rétention de 20%"
Technical angle : "Implémenter un système de recommandations ML"

Même but, framing différent.
```

### 4.3 Axe WHAT ↔ HOW
```
MRD/BRD/PRD (WHAT) ← → SRD (HOW)

WHAT : "L'utilisateur peut chercher des snippets par langage"
HOW : "Index sur la colonne 'language', requête SQL paramétrisée, <500ms latency"
```

### 4.4 Axe SCOPE (Large) ↔ SCOPE (Étroit)
```
MRD : "Transform the entire developer experience"
SRD : "Implement the search endpoint with pagination"

Large scope vs narrow scope = même produit, zoom différent.
```

### 4.5 Axe TIMELINE : Discovery ↔ Implementation
```
MRD : Écrit en Q1, valide jusqu'à Q4
BRD : Reffiné chaque sprint
PRD : Évite pendant l'implémentation
SRD : Générée JIT (Just In Time) juste avant le coding

Les documents ne vivent pas au même rythme.
```

---

## 5. ANALYSE — Les Points de Rupture (Seuils, stabilité, tensions)

### 5.1 Rupture 1 : MRD → BRD (La traduction du marché en business)
```
TENSION : 
  "Le marché dit X, mais nos business objectives disent Y"
  
Exemple :
  MRD : "Marché: augmentation 10% YoY des outils collaboratifs"
  BRD : "Mais nous, on ne vise que nos 100 clients Enterprise (scope réduit)"
  
POINT DE RUPTURE : 
  Si MRD et BRD ne sont pas alignées, 
  tout ce qui suit s'écroule.
  
STABILITÉ : Faible. Nécessite validation business régulière.
```

### 5.2 Rupture 2 : BRD → PRD (De la stratégie business aux fonctionnalités)
```
TENSION :
  "L'objectif business est clair, mais comment en fonctionnalités ?"
  
Exemple :
  BRD : "Augmenter la rétention"
  PRD : "Comment ? Chat ? Notifications ? Gamification ?"
  → Plusieurs chemins possibles. Laquelle choisir ?
  
POINT DE RUPTURE :
  Le product manager doit trancher. 
  Mais sur quels critères ? (User research ? Data ? Intuition ?)
  C'est un choix de conception, pas une déduction logique.
  
STABILITÉ : Moyenne. Une fois tranché, reste stable.
```

### 5.3 Rupture 3 : PRD → SRD (De la description utilisateur à la construction technique)
```
TENSION :
  "Je dois savoir si c'est techniquement faisable et à quel coût"
  
Exemple :
  PRD : "Notifications en temps réel"
  SRD : "WebSocket ou polling ? Redis ou Kafka ? 
         Cela change drastiquement l'architecture."
  
POINT DE RUPTURE :
  L'architecte doit faire des trade-offs :
  - Coût vs performance
  - Simplicité vs extensibilité
  - Timeframe vs robustesse
  
STABILITÉ : Basse. Les tech choices se regrettent souvent.
```

### 5.4 Rupture 4 : SRD → Implementation (La réalité du code)
```
TENSION :
  "Le spec dit X, mais le code doit gérer les détails que le spec ignore"
  
Exemple :
  SRD : "Requête DB en <500ms"
  Code : "Oups, avec 1M de rows, c'est 5s. Faut indexer comment ?"
  
POINT DE RUPTURE :
  Le développeur découvre que le spec était incomplet ou optimiste.
  → RÉVÉLATEUR D'IMPLICITES (le dev révèle ce qu'on ne savait pas)
  
STABILITÉ : Très basse. C'est ici que les surprises arrivent.
```

### 5.5 Points de rupture globaux : la "dette d'intention"
```
CONCEPT CLÉ — Dette d'intention (gap entre what was meant vs what was encoded)

Au fil des phases, l'intention originelle du MRD peut se dissoudre :

Phase 1 : MRD = "Résoudre fragmentation"
Phase 2 : BRD = "Offrir plateforme unifiée"
Phase 3 : PRD = "Build chat + calendar + files"
Phase 4 : SRD = "3 microservices découplés"
Phase 5 : Code = "3 services qui ne se parlent pas, données dupliquées"

Résultat : le produit "unifié" est techniquement fragmenté.

La dette d'intention s'accumule à chaque rupture.
```

---

## 6. CATÉGORIES — Cohérence Interne (Pas de jugement externe)

### 6.1 Catégorie 1 : Documents de JUSTIFICATION (MRD, BRD)

**Rôle** : Répondre à "POURQUOI et POUR QUI ?"

**Structure interne** :
```
Problem space
  ↓ analysis
Opportunity space
  ↓ filtering
Business case
  ↓ stakeholder alignment
Strategic goals
```

**Cohérence interne** : 
- Chaque problème doit être réel (basé sur données/research)
- La solution proposée doit adresser le problème (nexus logique)
- Les bénéfices doivent être quantifiables

### 6.2 Catégorie 2 : Documents de SPÉCIFICATION (PRD, SRD)

**Rôle** : Répondre à "QUOI et COMMENT ?"

**Structure interne** :
```
User stories (PRD) or Technical specs (SRD)
  ↓ detailed
Acceptance criteria (PRD) or Architecture (SRD)
  ↓ validated
Ready for implementation
```

**Cohérence interne** :
- Chaque user story doit mapper à un business goal
- Chaque acceptance criterion doit être testable
- L'architecture doit couvrir tous les requirements

### 6.3 Matrice de cohérence inter-documents

```
              MRD              BRD              PRD              SRD
PURPOSE   Market+need  Business case    User features   Technical build
AUDIENCE  Marketing     PM+Execs         PM+UX+Dev       Dev+Arch+QA
KEY FOCUS Market data   Stakeholder req  User workflows  Implementation
DETAIL    Low          Medium           High (UX)       High (Tech)
CHANGED   Quarterly    Per sprint       During exec     During coding
OWNER     Product      Product          Product         Tech Lead
```

### 6.4 Règle de cohérence transversale

```
∀ statement_s ∈ MRD :
  ∃ corresponding_statement_t ∈ {BRD, PRD, SRD}
  where meaning(s) ≈ meaning(t)
  
Ou en français : 
Aucune idée du MRD ne doit être perdue
au fil de la cascade documentaire.

(C'est le test ultime contre la "dette d'intention")
```

---

## 7. TOPOLOGIE — La Forme Globale (Ce que la structure révèle)

### 7.1 Structure en DAG (Directed Acyclic Graph)
```
                    MRD
                     ↓
                    BRD
                   ↙   ↘
                PRD     (Implementation planning)
                 ↓
                SRD
                 ↓
              CODE
              
Propriétés :
- Ordre total : MRD ⊆ BRD ⊆ PRD ⊆ SRD ⊆ Code (en raffinement)
- Pas de cycle : pas de document qui justifie sa propre existence
- Arborescence croissante de détail
```

### 7.2 Structure en entonnoir de divergence puis convergence
```
MRD   (1 market opportunity)
  ↓
BRD   (Peut diverger en 2-3 business models possibles)
  ↓
PRD   (Peut diverger en N features possibles)
  ↓
SRD   (Peut diverger en M architectures possibles)
  ↓
CODE  (Doit converger : une implémentation unique)

RÉVÉLATION : À chaque étape, il y a plus de possibilités qu'à la précédente.
Puis tout doit converger à la fin.
```

### 7.3 Espaces de projection
```
L'univers documentaire peut être vu comme un espace multidimensionnel :

Dimensions :
- Abstraction (MRD) ← → Concrétion (Code)
- Largeur (marché entier) ← → Étroitesse (fonction locale)
- Business (BRD) ← → Technical (SRD)
- Strategic (MRD/BRD) ← → Tactical (PRD/SRD)

Chaque document est une PROJECTION de ce même objet (le produit)
sur un axe différent.

Cohérence = projections sont compatibles (Théorème de Tychonoff en topologie)
```

### 7.4 La "dimension manquante" : FEEDBACK LOOP

```
L'architecture documentaire ci-dessus est linéaire :
MRD → BRD → PRD → SRD → Code

MAIS dans la réalité, les feedback loops sont essentielles :

Code révèle que SRD était irréaliste
  ↘
    → SRD doit être revu
      ↘
        → PRD doit être revu (features coupées ?)
          ↘
            → BRD doit-il être revu ? (objectif business inatteignable ?)
              ↘
                → MRD était-il bon ? (market opportunity réelle ?)

LA TOPOLOGIE RÉELLE EST :
                    MRD
                     ↕ (feedback)
                    BRD
                     ↕
                    PRD
                     ↕
                    SRD
                     ↕
                    CODE

C'est un espace du type "Fiber bundle" où chaque strate peut
affecter la strate précédente. Pas une simple tour de raffinement.
```

---

## 8. PROBABILITÉS/MESURE — Architecture d'apprentissage & Endomorphisme final

### 8.1 Entropie informationnelle des documents

```
H(MRD)  = hauteur moyenne d'ambiguïté sur la définition du problème
H(BRD)  = hauteur moyenne d'ambiguïté sur les objectifs business
H(PRD)  = hauteur moyenne d'ambiguïté sur les fonctionnalités
H(SRD)  = hauteur moyenne d'ambiguïté sur l'implémentation
H(Code) = hauteur moyenne de bugs / malentendus résidus

PROPRIÉTÉ THERMODYNAMIQUE :
H(MRD) > H(BRD) > H(PRD) > H(SRD) > H(Code)

L'entropie diminue au fil des phases (le système devient plus déterministe).

MAIS : si H(Code) n'est pas zéro, cela signifie que le Code révèle
des ambiguïtés qu'aucun document n'avait couvertes. 
→ C'est l'effet RÉVÉLATEUR D'IMPLICITES du développeur.
```

### 8.2 Distributions de probabilité conditionnelle

```
P(BRD_valid | MRD_valid) = ?
P(PRD_valid | BRD_valid) = ?
P(SRD_valid | PRD_valid) = ?
P(Code_works | SRD_valid) = ?

Chaque transition a une "probabilité de préservation de validité".

En pratique :
P(BRD_valid | MRD_valid) ≈ 0.7   (30% des cas, BRD rate l'intention du MRD)
P(PRD_valid | BRD_valid) ≈ 0.6   (40% des cas, features ne matchent pas goals)
P(SRD_valid | PRD_valid) ≈ 0.5   (50% des cas, tech choices critiques)
P(Code_works | SRD_valid) ≈ 0.4  (60% des cas, bugs, edge cases)

Product of transitions : 0.7 × 0.6 × 0.5 × 0.4 = 0.084 (8.4%)

Cela signifie : Sans gestion active de la cohérence,
il n'y a que 8% de chance que le produit final fasse ce que le MRD demandait.
```

### 8.3 Endomorphisme de correction iterative

```
Le système documentaire devrait inclure un OPÉRATEUR DE RÉTROACTION :

Feedback : Code → (test révèle problème) → ajustement SRD → ajustement PRD → ...

Formellement :
φ : (MRD, BRD, PRD, SRD, Code) → (MRD', BRD', PRD', SRD', Code')

Cet endomorphisme φ est le processus d'itération/amélioration.

Points fixes (φ(x) = x) = documents que l'implémentation ne remet pas en question.

EN PRATIQUE :
- Un bon PRD résiste à plusieurs itérations sans changement majeur
- Un mauvais SRD se fait détruire dès qu'on code
- Un bon MRD peut servir pendant 2-3 ans

Mesuré en "nombre d'itérations avant convergence" ou "stabilité du document".
```

### 8.4 Métrique globale : Indice de cohérence (CohesionIndex)

```
Défini comme la moyenne pondérée de :

CI = w1 * align(MRD, BRD)
   + w2 * align(BRD, PRD)
   + w3 * align(PRD, SRD)
   + w4 * align(SRD, Code)
   
Où align(d1, d2) ∈ [0, 1] mesure l'absence de contradictions.

CI ∈ [0, 1] :
- CI = 1.0 : Cohérence parfaite (rare)
- CI = 0.7 : Acceptable (30% de malentendus tolérables)
- CI < 0.5 : Projet risqué (plus de contradictions que cohérence)

Idée clé : Mesurer la cohérence n'est pas normatif,
c'est juste une santé-check du système documentaire.
```

---

## SYNTHÈSE FORMELLE

| Élément | Définition | Implications |
|---------|-----------|-------------|
| **Ensembles** | 4 documents × 6+ audiences × infini problèmes | Combinatoire explosive sans structure |
| **Logique** | Règles d'existence + transformation + validité | Chaque document doit justifier son existence |
| **Invariants** | Intention, traçabilité, non-redondance, exhaustivité | Ces 4 piliers ne peuvent pas être violés |
| **Axes de variation** | 5+ axes orthogonaux (abstraction, business/tech, what/how, scope, timeline) | Chaque document occupe une région différente |
| **Ruptures** | 4 transitions critiques (MRD→BRD, BRD→PRD, PRD→SRD, SRD→Code) | Chaque rupture accumule risque de perte d'intention |
| **Catégories** | Justification vs Spécification | Deux métier radicalement différents |
| **Topologie** | DAG + Fiber bundle avec feedback loops | Structure complexe, pas simple empilement |
| **Probabilités** | Entropie décroissante + endomorphisme itératif | Mesurabilité de la cohérence |

---

## TENSIONS NON RÉSOLUES (Ouvertes volontairement)

1. **Contradiction timing** : Les documents doivent-ils être finalisés ou vivants ?
   - Si vivants : comment gérer les versions ?
   - Si finalisés : comment incorporer le feedback du dev ?

2. **Qui est responsable de la cohérence inter-documents ?**
   - Le PM ? L'architecte ? Un rôle d'AMOA dédié ?
   - Cette responsabilité est floue dans la plupart des orgas.

3. **Qu'est-ce qu'une "bonne" PRD ?**
   - Plus de détail = plus de clarté OU plus de contrainte ? 
   - Il existe un sweet spot, mais il est context-dependent.

4. **Le feedback code → spec est-il une itération normale ou un symptôme d'échec ?**
   - Les deux. C'est un diagnostic : bon feedback ≠ mauvais spec.

5. **Peut-on formellement prouver que deux documents sont cohérents ?**
   - Partiellement. Pas d'algorithme universel. Le jugement humain reste nécessaire.
