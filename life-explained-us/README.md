# Life Explained (US) — adaptation américaine de « La Vie Expliquée »

Ce dossier contient tout le projet d'adaptation de la chaîne française
[La Vie Expliquée](https://www.youtube.com/@lavieexpliquee) pour un public américain.

**Principe directeur : on ne réinvente pas la roue.** Même concept, même structure de
vidéo, mêmes mécaniques de hook et de rétention. On change la langue, les références,
les chiffres (sources US), les décors des illustrations (États-Unis) et les unités
(mph, °F, ft, lb).

> Le concept FR : *« J'explique la vie… ainsi que les raisons pour lesquelles elle peut s'arrêter. »*
> Formats phares : « Voici ce qu'on ressent en mourant [écrasé par une voiture / poignardé /
> par le fentanyl / crucifié…] » et « La vraie raison pour laquelle on meurt (personne ne te l'explique) ».
>
> Version US : **"This is what it feels like to die from [X]"** + **"The real reason you die
> (nobody tells you this)"**.

## Contenu

| Fichier | Rôle |
|---|---|
| [`docs/01-channel-analysis.md`](docs/01-channel-analysis.md) | Décorticage du format FR : concept, titres, hook, structure, rythme, visuels |
| [`docs/02-us-format-bible.md`](docs/02-us-format-bible.md) | La bible de la chaîne US : nom, promesse, ton, voix, règles de traduction culturelle |
| [`docs/03-hook-playbook.md`](docs/03-hook-playbook.md) | Les 8 patterns de hook, traduits FR → US, avec exemples prêts à l'emploi |
| [`docs/04-visual-style-guide.md`](docs/04-visual-style-guide.md) | Direction artistique des illustrations « américaines » + prompts IA |
| [`docs/05-safety-and-monetization.md`](docs/05-safety-and-monetization.md) | Garde-fous YouTube (contenu choquant, suicide, drogues) pour rester monétisable |
| [`docs/06-production-workflow.md`](docs/06-production-workflow.md) | Pipeline de production d'un épisode (script → voix → images → montage → upload) |
| [`docs/07-content-backlog.md`](docs/07-content-backlog.md) | 40 sujets : adaptations directes des vidéos FR + sujets 100 % US |
| [`reference-fr/`](reference-fr/) | Transcriptions des vidéos FR (à déposer) |
| [`templates/`](templates/) | Template de script, template de shot list, template de métadonnées YouTube |
| [`episodes/`](episodes/) | Épisodes prêts à produire (script long + version Short + shot list + titres/miniature) |

## Épisodes prêts

1. [`ep01-hit-by-a-car`](episodes/ep01-hit-by-a-car.md) — adaptation de « …écrasé par une voiture » (piéton, SUV, crosswalk US) — **avec shot list complète + prompts d'images**
2. [`ep02-fentanyl`](episodes/ep02-fentanyl.md) — adaptation de « …par le fentanyl » (le sujet le plus américain du catalogue)
3. [`ep03-the-real-reason-you-die`](episodes/ep03-the-real-reason-you-die.md) — adaptation de « La vraie raison pour laquelle on meurt »
4. [`ep04-struck-by-lightning`](episodes/ep04-struck-by-lightning.md) — sujet 100 % US (Floride, « lightning capital »)

## Limites de cette première passe (à lire)

- **YouTube est bloqué par le réseau de cet environnement cloud** : je n'ai pas pu regarder les
  vidéos ni lire les transcriptions. L'analyse du format repose sur la description de la chaîne et
  les titres trouvés via recherche web. Les points marqués *(à vérifier)* dans
  `01-channel-analysis.md` doivent être confirmés en regardant 3-5 vidéos FR.
- **Aucune vidéo n'était présente dans le dépôt** (seulement le site Smarter Tonight). Si tu as
  la « stack » de vidéos en local, deux options :
  1. autoriser `youtube.com` dans les réglages réseau de l'environnement, ou
  2. déposer les transcriptions (`.txt`/`.srt`) dans `reference-fr/` et je calerai les scripts
     US phrase par phrase sur la structure exacte des originaux.
- Tous les chiffres des scripts sont des ordres de grandeur sourcés en fin d'épisode ;
  à revérifier au moment de publier (les stats CDC/NHTSA changent chaque année).
