# Bilibili → YouTube : formats viraux non exploités (recherche du 29/10/2026)

## Méthode

1. **Côté Bilibili** — 4 axes de recherche en parallèle (~190 recherches web en chinois et en anglais) :
   savoir/science/histoire, mèmes/animation/IA, lifestyle/défis, classements officiels
   (每周必看, 百大UP主 2024 et 2025, rapports trimestriels Bilibili, analyses 新榜/飞瓜).
   ⚠️ `bilibili.com` est bloqué par le réseau de l'environnement cloud : les chiffres viennent de pages
   lues côté serveur par le moteur de recherche (instantanés datés, marqués *non vérifié* quand
   la source est fragile).
2. **Côté YouTube** — mesure directe via l'API interne (`tools/gap.py`) : pour chaque format, ~40
   résultats par requête en anglais, avec médiane de vues, nombre de vidéos ≥ 100 k,
   récence et nombre de chaînes en série. Un format est « ouvert » quand la demande est prouvée
   (vues élevées sur des formats voisins) **et** qu'aucune chaîne ne le fait en série.

## Ce qui a été écarté (déjà pris sur YouTube EN)

| Format Bilibili | Preuve côté Bilibili | Pourquoi écarté |
|---|---|---|
| Maison pour son chat (爱鼓捣的邢志磊) | 13,9 M vues | Saturé : 24/33 résultats ≥ 100 k, le créateur chinois est lui-même sur YouTube |
| Expertise de vidéos virales d'animaux (无穷小亮) | 14,2 M vues (ép. 38) | Forrest Galante, Clint's Reptiles, Zoology With Will le font déjà en série |
| Anime « réincarné avec un système » (沙雕动画) | 25 M vues (长生青牛) | Anime Bunnie, Tide Glow Anime… déjà des dizaines de chaînes |
| Évolution des frontières en timelapse (史图馆) | 3,8 M vues | Ollie Bye, EmperorTigerstar… |
| Folklore chinois animé | — | Nightmare Tales, Merrily Horror Animations… |
| « What it feels like to die » sur Bilibili | Mr. Death doublé : 1,03 M vues | Déjà présent via des repartages IA massifs (voir plus bas) |
| Remakes IA de scènes célèbres, chansons IA (鬼畜) | 5–12 M vues | Droits d'auteur et image des acteurs : intransposable |

## Les 3 propositions retenues

### 1. « The Rules » — horreur à règles, en énigme interactive (规则怪谈动画)

**Bilibili** : une feuille de règles numérotées s'affiche (« Règle 3 : ne réponds jamais si le contrôleur frappe deux fois »).
**Certaines règles sont fausses** et le spectateur doit trouver lesquelles avant le personnage.
Un « donjon » par lieu (dortoir, TGV, supermarché…). 3,65 M vues (高铁怪谈), 2,6 M (列车凝云), compilations de 8 h à 1 M.
Les commentaires qui défilent explosent à chaque règle (« la 4 est fausse ! »).

**YouTube EN** :
- **Demande prouvée** : le genre « strange rules » existe en *lecture audio* (Lighthouse Horror : 400–800 k vues,
  The Dark Somnium : compilation de 6 h à 280 k), l'horreur animée est énorme (Wansee : 10 M),
  et la survie interactive marche (DanPlan *Can You Survive* : 12,8 M).
- **Trou** : « which rule is fake horror puzzle » → **0 vidéo pertinente**. Personne ne fait la version
  *animée + énigme de déduction*.

**Pourquoi ça devrait marcher** : c'est la fusion de deux genres prouvés en anglais (rules creepypasta + « can you survive »)
avec la mécanique que Bilibili a validée. Chaque épisode est un jeu → commentaires (« la règle 3 était fausse »)
→ algorithme. Chaque lieu américain = un épisode (Walmart de nuit, motel, station-service, Amtrak, parc national…).
Compilations longues en bonus pour le temps de visionnage.
**Production** : animation 2D simple (style figurines) + voix + musique, 50–300 $ par épisode de 10 min, 100 % faceless, aucun problème de droits.

### 2. « Adulting 101, told by cats » — tutoriels de vie adulte joués par des chats-mèmes (猫meme科普)

**Bilibili** : la percée la plus rapide de 2026. 咕噜耄 : première vidéo le 26/02/2026, **≈ 1–1,5 M d'abonnés en un mois**,
« comment louer un appartement » à 4,6 M vues. Copies réussies : finance (基米大科普, 509 k en ~3 mois),
philosophie (猫的哲学, 180 k en 91 jours), séries de fiction (猫meme电影院, 12 M vues).
Format : vidéos d'environ 1–1,5 min (série de fiction plus longue) ; des chats-mèmes jouent la scène pendant qu'une voix explique quelque chose d'utile.

**YouTube EN** :
- **Demande prouvée** : les chats-mèmes existent en anglais, mais seulement en *fiction*
  (NO1 CAT MEMES : 3,7 M il y a 2 mois, Kitty POVs : 11,6 M). L'éducatif avec gimmick marche aussi
  (Primate Economics, *Credit Cards / Tax Explained with Bananas* : 1,2–1,6 M en moins d'un an).
- **Trou** : « how credit scores work explained cat memes », « adulting explained cat memes » →
  **aucune chaîne**. Le besoin « personne ne m'a appris ça » est le même aux États-Unis
  (crédit, impôts, assurance santé, bail, 401k, premier job), avec en plus des mots-clés où la pub paie bien.

**Pourquoi ça devrait marcher** : format le moins cher de toute l'étude, croissance la plus rapide mesurée,
et un public anglophone déjà habitué aux chats-mèmes. Il marche en Short (1 min) et en long (8 min).
**Risques** : (a) les extraits de chats-mèmes appartiennent à leurs auteurs → créer **nos propres chats**
(IA ou banque libre de droits), ce qui rend en plus la chaîne reconnaissable ; (b) en Chine, l'audience par vidéo est retombée
après la mode → miser sur des sujets utiles (recherchés toute l'année), pas sur la nouveauté.

### 3. « Weird Little Countries » — l'histoire des pays méconnus, racontée avec des mèmes (奇葩小国, 小约翰可汗)

**Bilibili** : 小约翰可汗 = **10,9 M d'abonnés**, dans les 百大 de 2021 à 2025, série « pays bizarres »
à 3–4,5 M vues de moyenne. Format : un hamster narrateur (pas de visage), l'histoire chronologique
d'un petit pays ou d'un dictateur absurde, une image-mème toutes les quelques secondes, des running gags
(les surfaces mesurées « en unités de sa ville natale »), 15–30 min.

**YouTube EN** :
- **Demande prouvée** : vidéos isolées énormes sur ce sujet (Casual Scholar, Turkmenistan : 7,2 M ;
  Scribble Scholar : 10 M il y a 8 mois ; Witness : 1,5 M) et un modèle de ton orphelin :
  Sam O'Nella Academy (16–24 M par vidéo), dont les succès datent tous de 6 à 10 ans (activité récente non vérifiée).
- **Trou** : 29 chaînes différentes sur « dumbest dictator », **aucune en série**.
  « weirdest small country history memes » → 4 résultats, dont aucun à plus de 360 k vues.

**Pourquoi ça devrait marcher** : la demande est énorme et éparpillée ; personne n'en a fait une
*série* avec une mascotte et des running gags. C'est le format le plus durable des trois (des centaines
de pays, régimes, coups d'État, micronations) et il vise le long format, où le temps de visionnage rapporte le plus.
**Production** : script lourd (recherche), visuels peu chers (cartes, photos du domaine public, mèmes),
100–300 $ par épisode.

## Option risquée : « Vibe knowledge » (Vibe知识)

比特新语 : **0 → 650 k abonnés en 15 jours (octobre 2026)**. Concepts abstraits (entropie, optogénétique)
en animations générées par code, montées comme un clip musical de 3–5 min. Sur YouTube EN, la vulgarisation visuelle
est dominée par 3Blue1Brown en format long, mais personne ne fait le format court « clip musical ».
La presse chinoise prévoit cependant que la fenêtre se fermera très vite. À tenter seulement en complément.

## Constat annexe : Bilibili importe YouTube à grande échelle

Mr. Death est déjà sur Bilibili en version doublée en chinois (« 被切成两半是什么感觉 », 1,03 M vues),
via des comptes de repartage qui doublent automatiquement à l'IA des milliers de vidéos YouTube
(« 黑纹白斑马 » : plusieurs milliers à plusieurs dizaines de milliers de vidéos selon les sources).
Le flux inverse (Bilibili → YouTube) est quasi inexistant : c'est l'opportunité.

## Outils

```bash
python3 tools/gap.py "query 1" "query 2"   # analyse de concurrence YouTube
python3 tools/search.py "query"            # résultats bruts
```
