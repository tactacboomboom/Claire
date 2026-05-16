# FMATHS — DOCUMENTATION PRODUIT
## Passe 2 : Décodeur Mathématiques (Narration haute précision)

La rigueur mathématique devient l'ossature invisible. Style : podcast/essai organique, zéro symboles logiques, zéro notations ensemblistes.

---

## INTRODUCTION : Le Paradoxe Central

Imagine que tu construises un produit. Tout le monde autour de toi parle du "même produit", mais ils n'en parlent pas du tout de la même façon.

Le commercial parle du **marché** : "il y a une fragmentation, les équipes perdent du temps".  
Le directeur produit parle d'**objectifs business** : "nous, on veut augmenter la rétention de 20%".  
Le product manager parle des **features** : "pour ça, il faut un système de notification temps-réel".  
L'architecte parle de **technologie** : "ça veut dire WebSockets, Redis, une architecture event-driven".  
Le développeur parle du **code** : "mais avec 1M d'utilisateurs, faut indexer comment exactement ?"

Chacun décrit le même objet. Mais à des niveaux d'abstraction si différents qu'on se demande si c'est vraiment la même chose.

La question centrale devient : **Comment la cohérence est-elle possible ?** Qu'est-ce qui garantit que quand le développeur écrit le code, il construit vraiment ce que le commercial a vendu ?

C'est le cœur de ce qu'on va explorer.

---

## ACTE 1 : LE THÉÂTRE DES QUATRE DOCUMENTS

### Le décor : quatre documents, une pièce de théâtre

Quand une entreprise lance un produit, elle ne procède jamais avec un seul document. Elle en produit quatre, généralement dans cet ordre :

**MRD** — Market Requirements Document. Celui-ci répond à une seule question : pourquoi faire ce produit ? Quels sont les problèmes réels dans le marché ? Qui les subit ? À quelle fréquence ? Quel est le coût de l'inaction ?

**BRD** — Business Requirements Document. Celui-ci reformule le MRD à travers le prisme de l'entreprise : d'accord, il y a un problème marché. Mais nous, on en fait quoi ? Quel est notre business case ? Quels objectifs on se fixe ? Qui faut convaincre en interne pour avancer ?

**PRD** — Product Requirements Document. Celui-ci transforme les buts business en **fonctionnalités concrètes**. Le PRD dit : voilà comment on va résoudre le problème avec des features que les utilisateurs peuvent comprendre et utiliser.

**SRD** — Software Requirements Document. Celui-ci traduit les fonctionnalités en **architecture technique**. Le SRD dit : bon, maintenant qu'on sait quoi construire, comment on le construit ? Quelle techno ? Quelle base de données ? Quel découpage en services ?

Puis le développeur écrit le code. Et, presque toujours, il découvre des trucs que personne n'avait pensé à mettre dans les quatre documents précédents.

Cette chaîne — MRD, BRD, PRD, SRD, Code — est la **colonne vertébrale** de tout projet logiciel. Mais elle cache un problème majeur.

### Première rupture : MRD → BRD, ou comment le marché devient stratégie

Imagine que ton MRD dit ceci : "Les développeurs français perdent 2 heures par jour à chercher des snippets de code réutilisables. Le marché potentiel est de 500 000 devs. Si on capture 10 %, on touche 50 000 utilisateurs. C'est un marché de 50M€/an."

Super. Maintenant, la BRD doit dire : nous, dans notre contexte, comment on vise ce marché ?

Peut-être tu dis : "On cible les startups tech, pas le marché entier."  
Ou : "On cible France uniquement pour commencer."  
Ou : "On se concentre sur Python et JavaScript, pas tous les langages."

À ce moment, tu as déjà **réduit l'ambition** du MRD. Le problème global existe, mais tu décides de ne résoudre qu'une partie. C'est une **rupture créatrice** : tu passes du "pourquoi c'est important pour le marché" au "pourquoi c'est important pour nous".

Si ta BRD ne relie pas clairement ce qu'elle fait au problème du MRD, tu as une fuite logique. L'équipe de vente vendra ce qu'elle a lu dans le MRD. L'équipe produit construira ce qu'elle a lu dans la BRD. Et ces deux choses ne seront pas la même.

### Deuxième rupture : BRD → PRD, ou comment la stratégie devient features

Là, c'est plus délicat encore. Ton BRD dit : "Augmenter la rétention de 20% en ciblant les freelances."

Comment en features ? Aucune façon "correcte" unique. Tu pourrais :
- Ajouter un système de notifications pour les rappeler de revenir
- Ajouter un plan tarifaire freemium pour les accrocher
- Ajouter une communauté où les freelances se parlent
- Ajouter un système de recommandations basé sur l'IA

Toutes ces features adressent le même objectif business. Mais c'est au product manager de **trancher**. Et ce choix ne découle pas logiquement du BRD — c'est un choix de conception, presque artistique. Il est basé sur la compréhension du marché, les données utilisateur, l'intuition.

C'est pour ça que c'est compliqué. Le PRD n'est pas une **déduction** du BRD. C'est une **interprétation créative** du BRD.

Si le PM ne peut pas retracer chaque feature PRD jusqu'à un objectif BRD, alors il y a des features "orphelines" — des choses construites juste parce que c'était cool. Ce sont des sièges éjectables sur un avion de chasse.

### Troisième rupture : PRD → SRD, ou comment les features deviennent architecture

Ton PRD dit : "L'utilisateur peut chercher un snippet par langage et le copier en un clic."

Simple. Maintenant, l'architecte demande : comment ? Techniquement ?

Il faut une base de données. Mais laquelle ? SQLite pour le MVP ? PostgreSQL pour la scalabilité ? Redis en cache ?

Il faut une API. REST ? GraphQL ? Quel endpoint ? Quelle latence cible ? Que se passe-t-il si l'utilisateur a 1 million de snippets ? (Oups, pagination.)

Il faut une UI. Qui la fait ? React ou vanilla JS ? Comment on fait la syntaxe highlighting ? Avec Prism ? Avec Highlight.js ?

Chaque choix affecte le code, le timing, le coût. Et le PRD ne dit rien de tout ça. La PRD dit "utilisateur peut copier". La SRD doit dire "voilà comment c'est possible sans que le serveur ne s'écroule".

C'est ici qu'on voit émerger la **dette d'intention**. Le PRD disait une chose simple. Le SRD découvre que c'est plus compliqué qu'on pensait. Et si la SRD n'est pas bien structurée, le développeur va improviser. Il va choisir une solution rapide qui marche "pour le MVP" mais qui casse après.

### Quatrième rupture : SRD → Code, ou comment la théorie rencontre la réalité

C'est la pire rupture, parce qu'elle est **programmée** pour être une surprise.

Le SRD dit : "Requête de recherche en <500ms."  
Le développeur code. Et découvre : avec 1M de snippets en base, c'est 5 secondes, pas 500ms.

Le PRD ne mentionne pas "1M de snippets". Le SRD supposait une croissance lente. Mais la réalité est qu'au jour J du lancement, tu ne sais pas combien de snippets tu vas avoir.

Donc le développeur doit refaire l'architecture. Index sur la colonne langage. Pagination. Peut-être même un moteur de recherche dédiée (Elasticsearch ?). Tout ça rallonge le timeline.

Et à qui la faute ? À tous les étapes précédentes qui n'ont pas anticipé ce problème.

C'est pour ça qu'on dit que le développeur est un **"révélateur d'implicites"**. Le code force à affronter les choses qu'on n'a pas dites en blanc-noir dans les specs.

---

## ACTE 2 : LES TROIS SOCLES QUI NE PEUVENT JAMAIS ÊTRE VIOLÉS

Si tu ignores les quatre ruptures ci-dessus, ton projet va bien. Mais si tu violes l'un des trois socles, ton projet va **mal** de façon irrémédiable.

### Socle 1 : L'intention doit rester cohérente

À chaque étape (MRD → BRD → PRD → SRD → Code), tu dois pouvoir répondre à la même question : "Pourquoi on fait ça ?"

Et ta réponse doit être la **même idée**, juste à un niveau d'abstraction différent.

Exemple d'une intention cohérente :

MRD : "Les développeurs passent 2h/jour à chercher des snippets."  
BRD : "Nous allons résoudre ce problème avec une plateforme de partage de code."  
PRD : "Les features principales : créer, chercher, copier des snippets."  
SRD : "Architecture : backend API + frontend UI + base de données de snippets."  
Code : "Implémentation de ces trois composants."

Tout ça dit la même chose. "On aide les devs à retrouver du code réutilisable." À chaque étape, c'est juste plus détaillé, plus spécifique.

Contre-exemple : une intention qui s'évapore

MRD : "Les développeurs veulent une plateforme collaborative."  
BRD : "Nous allons la monétiser via un modèle SaaS."  
PRD : "Features : chat, notifications, analytics d'usage."  
SRD : "Architecture : trois microservices découplés, chacun avec sa base de données."  
Code : (Chat et notifications marche, mais l'analytics est cassée, trop de données à traiter.)

Quelque part entre le SRD et le Code, l'intention "plateforme collaborative" est devenue "trois services qui ne se parlent pas et ne partagent pas les données". L'intention s'est perdue.

C'est la **dette d'intention** : le gap entre ce qu'on voulait faire et ce qu'on a vraiment fait. Et elle s'accumule à chaque étape.

### Socle 2 : Chaque niveau doit tracer jusqu'au précédent

Un développeur qui code une feature doit pouvoir dire : "Cette ligne de code existe parce qu'il y a un requirement dans le SRD. Ce requirement existe parce qu'il y a une feature dans le PRD. Cette feature existe parce qu'il y a un objectif business dans le BRD. Cet objectif existe parce qu'il y a un problème dans le MRD."

C'est la **traçabilité**.

Dès qu'une ligne de code (ou une feature, ou un objectif) ne peut pas tracer jusqu'à un problème original, tu as une dette. Tu construis quelque chose sans savoir pourquoi.

En pratique, on pose la question : "Pourquoi on a cette ligne de code ?"

Réponse correcte : "Parce que le PRD demande des notifications temps-réel."  
Réponse suspecte : "Parce que ça semblait cool."  
Réponse catastrophique : "Parce qu'on ne sait pas. Personne ne se souvient."

### Socle 3 : Aucune redondance stratégique

Chaque document a une responsabilité unique. Si deux documents répondent à la même question, c'est une redondance.

MRD répond : "Pourquoi et pour qui ?"  
BRD répond : "Quel est le business case ?"  
PRD répond : "Quelles features construire ?"  
SRD répond : "Comment les construire techniquement ?"

Si le PRD commence à parler de technology, c'est une redondance. (Ça va être du bruit, confondre les lect

eurs.)  
Si le BRD tente de spécifier des features, c'est une redondance. (Le PM va ignore, parce que c'est le boulot du PRD.)

Chaque document fait un travail. Il ne fait pas le travail du suivant.

---

## ACTE 3 : LES CINQ AXES DE VARIATION — COMMENT LE MÊME PRODUIT CHANGE DE FORME

Quand tu regardes ces quatre documents, tu ne vois pas juste une accumulation de détails. Tu vois le même produit vu sous **cinq angles différents**, simultanément.

### Axe 1 : Abstraction ↔ Concrétion

MRD est très abstrait : "Les développeurs ont un problème d'efficacité."

SRD est très concret : "Index SQLite sur la colonne language, requête paramétrisée, timeout 500ms."

PRD et BRD sont au milieu.

C'est normal. Plus tu te rapproches du code, plus tu dois être concret. Mais trop d'abstraction dès le départ, et personne ne peut l'implémenter. Trop de concrétion au MRD, et tu inventes des détails sur des trucs qui n'ont pas de valeur.

### Axe 2 : Business ↔ Technical

MRD et BRD parlent le langage du business : "client", "rétention", "revenu", "marché".

PRD commence à basculer : c'est plus "utilisateur" que "client". Ça parle de "fonctionnalités" plutôt que "revenu".

SRD parle le langage de la technique : "microservices", "latency", "indexation", "cache".

Et pourtant, tu parles du même produit. Juste, tu le parles en trois langues.

### Axe 3 : WHAT ↔ HOW

MRD, BRD, PRD répondent à "WHAT" : Quoi construire ? Quel problème résoudre ?

SRD répond à "HOW" : Comment le construire ?

Le Code répond à "HOW" en ultra-détail.

Ces trois perspectives ne se contredisent jamais si tout est bien fait. Mais elles ne parlent pas de la même chose.

### Axe 4 : Large scope ↔ Étroit scope

MRD parle du marché entier, de tous les développeurs du monde.

BRD réduit : "Nous, on cible France, startups, Python et JavaScript."

PRD réduit encore : "Phase 1 : une seule feature, la recherche. Les autres features attendent phase 2."

SRD réduit encore plus : "Pour cette session de coding : créer l'API search endpoint uniquement."

Chaque document zoome davantage. C'est normal. Tu commences en visionnaire (MRD), et tu termines en développeur hyper-focalisé sur une ligne de code (Code).

### Axe 5 : Timeline — Rythme de changement

MRD : écrit une fois, valide pendant un an ou plus. Si le marché a changé radicalement, tu le rewrite.

BRD : revu chaque trimestre. Les objectifs business changent avec les cycles.

PRD : peut changer plusieurs fois par sprint. Une feature peut être découpée différemment, une user story reformulée.

SRD : générée juste avant le coding. Elle change constamment pendant l'implémentation.

Code : écrit et reécrit pendant des mois.

Ces documents ne vivent pas au même rythme. Et c'est OK. Mais ça signifie que tu dois les traiter différemment. Tu ne gères pas un PRD "stable" de la même façon qu'un MRD "stable".

---

## ACTE 4 : LES QUATRE POINTS DE RUPTURE CRITIQUES

Avant chaque rupture, tu dois valider. Sinon, tu propages l'erreur vers le bas.

### Rupture 1 : Du marché au business

**Question critique** : "Le problème qu'on a identifié dans le MRD, c'est vraiment notre problème ?"

Le MRD dit : "Marché : 500 000 devs, 2h perdues par jour".  
La BRD dit : "Nous : on cible 50 000 devs français dans les startups."

C'est une réduction volontaire. Pas un problème. Mais tu dois le **faire intentionnellement**, pas par accident.

Signes d'une rupture cassée :
- Le BRD ignore complètement ce que le MRD a dit (tu crées un produit différent)
- Le BRD promet plus que ce qu'a découvert le MRD (tu es trop optimiste)
- Le BRD ne mentionne pas le MRD du tout (tu ne sais pas pourquoi tu fais ça)

### Rupture 2 : De la stratégie aux features

**Question critique** : "Chaque feature PRD adresse un objectif BRD ?"

La BRD dit : "Augmenter rétention de 20%".  
La PRD dit : "Features : créer, chercher, copier, versions, partage".

Toutes ces features aident la rétention ? Ou quelques-unes sont juste... cool ?

Signes d'une rupture cassée :
- Features "orphelines" que personne ne peut justifier
- Features qui adressent des besoins secondaires, pas l'objectif principal
- Le PM n'a pas vraiment tranché : il a mis **toutes** les idées à la place d'en choisir **les bonnes**

### Rupture 3 : Des features à l'architecture

**Question critique** : "Chaque requirement SRD est nécessaire pour implémenter le PRD ?"

Le PRD dit : "L'utilisateur cherche des snippets par langage".  
Le SRD dit : "Index sur langage. API REST avec pagination. Cache Redis. Monitoring Datadog."

Le cache Redis est nécessaire ? Pour l'MVP, peut-être pas. Pour production avec 1M users, oui. **Quand** faut-il l'ajouter ? Le SRD doit le dire.

Signes d'une rupture cassée :
- L'architecte ajoute de la complexité "au cas où"
- L'architecte oublie des contraintes non-fonctionnelles (sécurité, perf, scalabilité)
- Le SRD fait 200 pages et tu ne sais pas par où commencer

### Rupture 4 : Du SRD au code

**Question critique** : "Peut-on vraiment implémenter le SRD dans le timeframe donné ?"

Le SRD dit : "WebSocket pour notifications temps-réel. Latency <100ms."  
Le développeur code. Ça ne marche qu'en <500ms. Peut-on rendre <100ms possible ? À quel coût (complexité, maintenance) ? Le SRD l'a-t-il anticipé ?

Signes d'une rupture cassée :
- Le développeur découvre que le SRD était irréaliste
- Le développeur doit couper des features parce que le SRD était trop ambitieux
- Le développeur code une solution "pour l'instant" en se disant "on l'améliorera plus tard" (il n'y a jamais de "plus tard")

---

## ACTE 5 : LA MÉCANIQUE DE LA COHÉRENCE

Comment garantir que tout ça tient ensemble ?

### Première mécanique : La traçabilité bidirectionnelle

Chaque feature doit tracer jusqu'à un problème.  
Mais aussi : chaque problème doit être couvert par au moins une feature.

Sinon, tu as des trous. Ou des trucs qui ne se justifient pas.

C'est un travail de **crosscheck** : prend une features du PRD. Peux-tu la tracer au BRD ? Peux-tu la tracer au MRD ? Si non, où vient-elle ?

### Deuxième mécanique : La réduction d'ambiguïté

À chaque étape, l'ambiguïté diminue.

MRD : très ambigu. "Les développeurs perdent du temps." (Quel type de développeur ? Quel temps exactement ? Où dans leur workflow ?)

BRD : moins ambigu. "Nous ciblons les développeurs Python/JS en France."

PRD : encore moins ambigu. "Feature : recherche full-text de snippets par langage."

SRD : presque aucune ambiguïté. "API GET /api/search?q=...&lang=... retourne un JSON avec pagination."

Code : aucune ambiguïté. (Ou il y a un bug.)

Si à une étape, tu **augmentes** l'ambiguïté au lieu de la réduire, tu as un problème.

Exemple d'augmentation d'ambiguïté :
BRD clairement dit "ciblons France uniquement".  
PRD dit "plateforme multilingue, pour les développeurs du monde entier".

Oups. Tu as augmenté l'ambiguïté, pas réduit. Quelqu'un va faire le mauvais choix.

### Troisième mécanique : Les feedback loops

En théorie, on progresse linéairement : MRD → BRD → PRD → SRD → Code.

En pratique, ça boucle.

Le code révèle que le SRD était irréaliste → tu revois le SRD.  
Le SRD revu implique qu'on peut moins de features → tu revois le PRD.  
Le PRD revu change l'objectif business → tu revois le BRD.  
Le BRD revu questionne si le marché en vaut la peine → tu questionnes le MRD.

Ces boucles sont **essentielles**. Elles transforment un plan statique en un processus qui répond à la réalité.

Mais elles doivent être **courtes** et **focalisées**. Si tu revois le MRD entièrement parce que le développeur a eu un bug, quelque chose s'est mal passé avant le code.

---

## ACTE 6 : LES DEUX RÔLES (ET POURQUOI C'EST IMPORTANT)

Fondamentalement, ces quatre documents font deux choses très différentes.

### Type 1 : Documents de JUSTIFICATION (MRD, BRD)

"Pourquoi faisons-nous ça ? Pourquoi maintenant ? Pour qui ?"

Ces documents justifient l'existence du projet. Ils argumentent. Ils vendent une vision. Ils alignent les stakeholders sur un même objectif.

Caractéristique clé : ils répondent à une question existentielle. Si tu n'as pas de bonne réponse à cette question, tu ne devrais pas construire le produit.

### Type 2 : Documents de SPÉCIFICATION (PRD, SRD)

"Quoi exactement allons-nous construire ? Comment ?"

Ces documents disent exactement ce qu'on fait. Ils donnent des détails. Ils sont exécutables : on peut coder basé dessus.

Caractéristique clé : ils répondent à des questions opérationnelles. Plus ambiguës = plus d'aller-retours pendant le coding.

**Confusion courante** : traiter un PRD comme une justification.

Genre : "Explique-moi pourquoi cette feature en particulier existe."

Mauvaise réponse (justification) : "Parce que c'est innovant et ça changera le marché."  
Bonne réponse (spécification) : "Parce que c'est dans le PRD et ça couvre ce user story."

Le PRD ne s'excuse pas. Il spécifie. Point.

**Autre confusion** : traiter un BRD comme une spécification.

Genre : "Quels endpoints API il faut créer ?"

Le BRD ne sait pas. C'est le SRD qui sait. Le BRD dit qu'il faut "un système de recherche". Pas "un endpoint GET /search avec pagination".

Quand les responsabilités sont clairs, tout devient plus simple.

---

## ACTE 7 : LA TOPOLOGIE SECRÈTE — CE QU'ON NE VOIT PAS

Visuellement, les quatre documents ressemblent à une tour qui s'empile :

```
MRD (top, marché)
 ↓
BRD (business)
 ↓
PRD (produit)
 ↓
SRD (technique)
 ↓
Code (bottom, implémentation)
```

C'est simple, linéaire. Mais ce n'est pas la vraie topologie.

### La vraie topologie : un entonnoir bidirectionnel

Au départ (MRD), il y a une idée simple.  
Puis (BRD), tu as 2-3 chemins possibles.  
Puis (PRD), tu as 5-10 features possibles.  
Puis (SRD), tu as 20+ choix architecturaux.  
Puis (Code), tout diverge complètement.

L'espace des **possibilités** explose à chaque étape.

Mais au final, tu dois **converger** sur UNE implémentation unique.

Donc en vrai, la topologie est :

```
     MRD (1 idée)
      ↓
     BRD (2-3 chemins)
      ↙ ↓ ↘
    PRD (5-10 features)
    ↙ ↓ ↓ ↓ ↘
  SRD (20+ choices)
  ↙ ↓ ↓ ↓ ↓ ↓ ↘
CODE (1 implémentation)
```

C'est un entonnoir : tu commences large (beaucoup de directions possibles) puis tu converges (une seule direction finale).

C'est pour ça qu'une bonne PRD réduit les dégats. Chaque décision prise au PRD élimine N possibilités du SRD. Donc moins tu dois décider tard.

### Deuxième révélation : le feedback loop est une **boucle de correction**

Théoriquement, les documents s'empilent proprement.

Pratiquement, ça ne marche jamais la première fois.

Quand le code sort, il révèle que le SRD était incomplet. Donc tu revois le SRD. Mais les revisions du SRD impliquent parfois des revisions du PRD (parce que certaines features ne sont pas faisables). Les revisions du PRD impliquent des revisions du BRD (parce que les objectifs business ne peuvent plus être atteints). Et ainsi de suite.

Cette boucle de correction est **pas un bug**. C'est un feature du système. C'est le processus d'apprentissage qui fait converger vers une implémentation réelle.

**Mais** : elle ne doit pas remonter trop haut ni trop vite. Si chaque semaine tu dois réécrire le MRD entièrement, quelque chose s'est mal passé au départ. Si tu dois réécrire le PRD chaque jour, le SRD est trop flou. Si tu dois réécrire le SRD chaque heure, c'est du coding pur, pas de la spécification.

### Troisième révélation : chaque document est une **projection** du même objet

Imagine le produit comme un objet 5-dimensionnel (Abstraction, Business/Tech, What/How, Scope, Timeline).

Le MRD est une projection sur l'axe "Abstraction + Business + Large scope".  
Le BRD est une projection sur "Abstraction-moyen + Business + Medium scope".  
Le PRD est une projection sur "Concret + What + Narrow scope".  
Le SRD est une projection sur "Très concret + Technical + Étroit scope".

En mathématiques, deux projections du même objet ne se contredisent jamais si l'objet est bien formé. Mais si tes projections se contredisent, ça veut dire que l'objet sous-jacent n'est pas bien défini.

Donc : "Le PRD et le SRD se contredisent" = "Le produit n'est pas bien défini".

C'est un diagnostic puissant. Ça te dit précisément où creuser.

---

## ACTE 8 : MESURABILITÉ DE LA COHÉRENCE (Ou : Comment savoir si on va bien ?)

On peut mesurer à quel point ton système documentaire tient ensemble.

### Métrique 1 : Entropie informationnelle

À chaque étape, l'ambiguïté du système diminue. Mesure-la.

MRD : "Résoudre un problème majeur." (Très ambigu. 100 interprétations possibles.)  
BRD : "On cible les freelances français en Python." (Moins ambigu. 10 interprétations.)  
PRD : "Features : créer, chercher, copier snippets." (Beaucoup moins ambigu. 2-3 interprétations.)  
SRD : "API REST, SQLite, <500ms latency." (Quasi pas ambigu. 1 interprétation.)  
Code : Aucune ambiguïté. Ou il y a un bug.

Si à une étape, l'ambiguïté **augmente** au lieu de diminuer, tu as un problème.

### Métrique 2 : Traçabilité directe

Pour chaque requirement du SRD, peux-tu tracer jusqu'au PRD ?  
Pour chaque feature du PRD, peux-tu tracer jusqu'au BRD ?  
Pour chaque objectif du BRD, peux-tu tracer jusqu'au MRD ?

Si tu as un requirement orphelin (qui ne trace nulle part), tu construis quelque chose dont tu ignores pourquoi.

### Métrique 3 : Absence de contradiction

Prend deux documents consécutifs. Y a-t-il une affirmation dans le premier qui contredit une affirmation du second ?

Exemple de contradiction :
BRD : "On cible multilingue."  
PRD : "MVP en anglais uniquement, multilingue en phase 2."

C'est une contradiction douce. Pas catastrophique, mais tu dois le noter et le résoudre.

Exemple de contradiction catastrophique :
BRD : "Les snippets sont versionés."  
SRD : "Base de données stateless, pas d'historique."

Ça ne marche pas. Quelqu'un doit trancher.

### Métrique 4 : Densité de feedback

Combien de fois le code a causé une révision du SRD ? Du PRD ? Du BRD ?

Si ça arrive rarement, ça signifie que tes specs étaient bonnes upfront. (Rare, mais possible.)  
Si ça arrive fréquemment, ça signifie qu'il y avait des trous.  
Si ça arrive TRÈS fréquemment, ça signifie que tu es entrain de coder plutôt que de spécifier.

Idéal : "2-3 feedback loops PRD→SRD durant le coding, 0-1 feedback loop BRD→PRD, 0 feedback loop MRD→BRD."

Mauvais : "5+ feedback loops à chaque niveau."

---

## ACTE 9 : LES TENSIONS QUI NE SERONT JAMAIS RÉSOLUES

Après tout ça, il reste des tensions qu'aucun protocole ne peut complètement résoudre. Ce ne sont pas des bugs, ce sont des traits fondamentaux.

### Tension 1 : Détail vs Clarté

Plus tu mets de détail dans un document, plus c'est clair. Mais plus c'est aussi lourd à lire.

PRD de 20 pages : ultra-clair, 0 ambiguïté, mais personne ne le lit.  
PRD d'une page : tout le monde le lit, mais il manque 20 cas edge.

Il y a un sweet spot, mais il est différent pour chaque projet.

### Tension 2 : Changement vs Stabilité

Les documents doivent-ils être "écrits une fois et gelés" ou "vivants et changeants" ?

Gelés : tu peux planifier, mais tu es rigide quand la réalité change.  
Vivants : tu es flexible, mais personne ne sait ce que vous faites vraiment.

C'est une balance. Pas une réponse unique.

### Tension 3 : Responsabilité de la cohérence

Qui s'assure que le PRD et le SRD ne se contredisent pas ? Le PM ? L'architecte ? Un rôle dédié (l'AMOA) ?

Beaucoup d'organisations n'ont pas clairement assigné cette responsabilité. Donc elle se glisse entre les cracks.

### Tension 4 : Révélateur d'implicites vs Mauvaise spec

Quand le développeur découvre un cas edge qu'aucun document n'a mentionné, est-ce que c'est :
- Un bon dev qui révèle des implicites ? (Bonne chose, on apprend)
- Une mauvaise spec du départ ? (Mauvaise chose, on aurait dû anticiper)

En vrai : les deux. C'est un diagnostic, pas un blâme.

---

## CODA : CE QUE TU AS COMPRIS

En raccourci :

**Le problème central** : Quatre documents prétendent décrire la même chose à des niveaux différents. Mais les niveaux ne s'empilent pas simplement — ils entrent en tension à chaque rupture.

**Les trois socles immuables** : L'intention doit rester cohérente. Chaque niveau doit tracer au précédent. Aucune redondance.

**Les cinq axes de variation** : Abstraction, Business/Tech, What/How, Scope, Timeline. Le même produit vu sous cinq angles.

**Les quatre ruptures critiques** : MRD→BRD, BRD→PRD, PRD→SRD, SRD→Code. À chaque rupture, tu accumules le risque de perte d'intention.

**La mécanique** : Traçabilité, réduction d'ambiguïté, feedback loops courtes.

**La topologie** : Un entonnoir. Tu commences large, tu termines convergent.

**La mesure** : Entropie, traçabilité, absence de contradiction, densité de feedback.

**Les tensions irrésolues** : Détail vs clarté, changement vs stabilité, responsabilité floue, révélateur vs mauvaise spec.

Tout ça ensemble forme un système. Pas parfait, mais fonctionnel si tu le manages bien.

Et c'est pour ça qu'une bonne documentation produit, c'est comme une symphonie. Chaque mouvement (document) a son rôle. Et si tu joues l'un faux, toute la symphonie s'écroule.
