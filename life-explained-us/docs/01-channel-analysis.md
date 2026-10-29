# 01 — Analyse de la chaîne FR « La Vie Expliquée » (données réelles)

Données récupérées le 29/10/2026 via l'API interne de YouTube (`youtubei.googleapis.com`, voir `tools/`).
Catalogues bruts : `research/catalog_fr.json`, `research/catalog_en.json`,
descriptions et commentaires : `research/fr_descriptions_comments.json`.

> ⚠️ **Constat principal : la chaîne FR est elle-même une traduction d'une chaîne américaine,
> [Mr. Death](https://www.youtube.com/@Mr.Death.Official)** (204 k abonnés, bio : *"Death's Explained."*).
> Les titres, durées et dates concordent, et les commentaires FR le disent explicitement
> (« Mais tu plagies Mr Death mot pour mot… », 55 likes ; « vu la même vidéo au détail près en anglais
> il y a 3 jours », « hormis traduire les vidéos de Mr Death en Français… »).
> **La « version américaine » de ce format existe donc déjà : c'est l'original.**

## La chaîne FR en chiffres

- Handle `@LaVieExpliquée`, bio : « J'explique la vie... Ainsi que les raisons pour lesquelles elle peut s'arrêter ! »
- **14 vidéos longues en ~3 semaines** (≈ 1/jour), **8 min 42 à 22 min**, médiane ≈ 13 min. Aucun Short.
- Hit : « Voici ce qu'on Ressent en Mourant de Chute » — **1,1 M vues**. Ensuite 197 k (coupé en deux),
  75 k (voiture), 71 k (Dahmer), 70 k (tir dans la tête), 68 k (Enfer).

| Vidéo FR | Durée | Vues | Équivalent Mr. Death (EN) | Durée EN | Vues EN |
|---|---|---|---|---|---|
| Mourir de Chute | 11:20 | 1,1 M | What Falling to Death Feels Like | 11:02 | 2 M |
| Coupé en deux | 15:58 | 197 k | What Getting Cut in Half Feels Like | 11:15 | 413 k |
| Tir dans la tête | 8:42 | 70 k | What Getting Killed by A Headshot Feels Like | 9:02 | 1,9 M |
| « Gooning » | 10:54 | 35 k | What Dying from Gooning Feels Like | 11:20 | 537 k |
| Fentanyl | 11:02 | 18 k | What Getting Killed by Fentanyl Feels Like | 11:53 | 1,2 M |
| Écrasé par une voiture | 15:18 | 75 k | — (pas d'équivalent Mr. Death trouvé) | | |
| Crucifié | 14:36 | 14 k | — | | |
| Poignardé | 13:21 | 25 k | — | | |
| Mourir comme Ace (One Piece) | 12:50 | 20 k | — | | |
| Mourir de Jeffrey Dahmer | 17:18 | 71 k | — | | |
| Mourir en Enfer (christianisme) | 11:36 | 68 k | — | | |
| Mourir de toutes les maladies | 22:04 | 47 k | — (compilation) | | |
| Les pires façons de se retrouver piégé | 10:16 | 37 k | — (un commentaire cite une source EN identique) | | |
| Overdose de Doliprane | 14:48 | 2,9 k | — | | |

## L'original : Mr. Death (EN)

- **38 vidéos**, ~10 mois d'existence, **8 à 16 min** + compilations de 1 h 26 et 2 h 48.
- Titre unique et constant : **"What [Getting Killed by / Dying from] X Feels Like"**.
- Top vues : Falling 2 M · Headshot 1,9 M · Fentanyl 1,2 M · Meth 1,1 M · Bleeding Out 906 k ·
  Drowning 768 k · Rabies 618 k · Decapitated 616 k · Vaping 590 k · Cancer 578 k · Obesity 541 k · Gooning 537 k.
- Thèmes qui marchent le mieux : **drogues et produits du quotidien** (meth, fentanyl, vaping, energy drinks,
  weed, steroids, smoking, Ozempic) et **morts physiques spectaculaires** (chute, balle, train, réacteur, crocodile).

## Ce que disent les commentaires FR (signal audience)

**Ce qui plaît**
- « Très réaliste », « pédagogique », « une vidéo de prévention » ; le cadrage éducatif/prévention est cité positivement.
- Le ton : « un humour de bon aloi ; un ton badin qui accompagne des informations claires ». Le narrateur
  met en scène un **personnage récurrent** (« force au perso qui nous représente, il ne survit dans aucune vidéo »),
  souvent prénommé (Kevin revient plusieurs fois).
- Visuels : **dessins / animations simples** (« des dessins comme support visuel », « talents d'animation »).
- Public très large : du collégien à « une retraitée de 75 ans ».
- Demandes récurrentes : noyade, brûlé vif, décapitation/guillotine, autres religions, scénario où le perso survit.

**Ce qui est reproché**
- Plagiat de Mr. Death, contenu « full IA », voix ressemblant à un youtubeur FR (« Maru ») → probable clonage vocal.
- **Défauts de montage audio** (coupures, mots mâchés, 20 s sans son) relevés sur presque toutes les vidéos.
- Spoiler de la fin dès l'intro sur une vidéo « histoires ».
- Miniature jugée irrespectueuse sur la crucifixion.

**Signal de risque** : plusieurs commentaires évoquent des idées suicidaires ou demandent des doses
(paracétamol, somnifères). Voir `05-safety-and-monetization.md`.

## Structure narrative (déduite des descriptions + commentaires horodatés, transcriptions non accessibles)

1. Intro qui pose la question + le personnage (« on va voir physiquement, chimiquement, et neurologiquement ce qu'on ressent… »).
2. Déroulé chronologique du point de vue du personnage, avec explications scientifiques.
3. Variantes / cas réels (« le mec aux Philippines crucifié 37 fois » à la fin).
4. Conseils de survie / prévention en fin de vidéo (« petit guide pour survivre en cas de grande chute »,
   « beau message de fin »).

## Ce qui reste inaccessible depuis cet environnement

Vidéos, transcriptions et miniatures : `youtubei.googleapis.com` répond, mais le lecteur exige une
connexion (`LOGIN_REQUIRED`, anti-bot sur IP cloud), l'endpoint de transcription exige un jeton
d'attestation, et `*.googlevideo.com` / `i.ytimg.com` sont bloqués par le réseau.
