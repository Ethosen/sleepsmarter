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

## ⚠️ Constat après analyse des vraies données (29/10/2026)

**La chaîne FR traduit une chaîne américaine existante : [Mr. Death](https://www.youtube.com/@Mr.Death.Official)**
(204 k abonnés, 38 vidéos « What … Feels Like »). Détail et tableau de correspondance dans
[`docs/01-channel-analysis.md`](docs/01-channel-analysis.md).

Conséquences :
- Retraduire les vidéos FR en anglais reviendrait à republier Mr. Death sur son propre marché :
  risque de réclamation pour droits d'auteur et de démonétisation pour « contenu réutilisé ».
- Les vidéos du format font **11 à 16 min**. Les 4 épisodes actuels (~6 min) sont des scripts
  originaux, mais il faudra les doubler en longueur.

## Données & outils

| Dossier | Contenu |
|---|---|
| [`research/`](research/) | Catalogues FR (14 vidéos) et EN Mr. Death (38 vidéos), descriptions et commentaires FR |
| [`tools/`](tools/) | Client minimal de l'API interne YouTube (`python3 tools/list_videos.py <channelId>`) |

## Limites

- Transcriptions, vidéos et miniatures restent inaccessibles depuis cet environnement cloud
  (connexion exigée par YouTube + hôtes vidéo/images bloqués). Pour les obtenir, lancer en local
  la commande de [`reference-fr/README.md`](reference-fr/README.md) et déposer les `.srt` dans le dépôt.
- Tous les chiffres des scripts sont sourcés en fin d'épisode ; à revérifier avant publication.
