# 06 — Pipeline de production d'un épisode

Objectif : un épisode long + son Short en ~1 journée de travail.

| # | Étape | Sortie | Outil suggéré |
|---|---|---|---|
| 1 | Choisir le sujet dans le backlog | ligne cochée dans `07-content-backlog.md` | — |
| 2 | (Si adaptation) transcrire la vidéo FR | `reference-fr/<slug>.txt` | yt-dlp + Whisper |
| 3 | Écrire le script US depuis `templates/script-template.md` | `episodes/epXX-<slug>.md` | — |
| 4 | Fact-check : chaque chiffre a une source US | section *Sources* remplie | CDC, NHTSA, NIH, NWS |
| 5 | Shot list (1 plan ≈ 4 s) + prompts d'images | tableau dans l'épisode | `templates/shotlist-template.md` |
| 6 | Générer les illustrations (seed fixe) + couches rayons X | `assets/epXX/` (hors Git, trop lourd) | Midjourney / Flux |
| 7 | Voix off | `voice.wav` | ElevenLabs ou voix humaine |
| 8 | Montage 16:9 (Ken Burns, compteur, sound design) | `epXX-long.mp4` | CapCut / Premiere / DaVinci |
| 9 | Recadrage + condensé 9:16 du Short | `epXX-short.mp4` | idem |
| 10 | Métadonnées (titre, description, tags, chapitres) | bloc *YouTube metadata* de l'épisode | `templates/youtube-metadata-template.md` |
| 11 | Upload + miniature + carte de fin vers l'épisode suivant | — | YouTube Studio |

## Conventions de fichiers

```
life-explained-us/
  episodes/epXX-<slug>.md      # script + short + shot list + métadonnées, un seul fichier
  reference-fr/<slug>.txt      # transcriptions FR (à créer si besoin)
  assets/                      # images/voix/montages — à garder hors Git (voir .gitignore)
```

## Checklist avant publication

- [ ] Hook : la scène US est identifiable en < 1 s
- [ ] Aucun chiffre français, toutes les unités US
- [ ] Partie « What saves you » présente
- [ ] Bandeau ressource si drogue / chute / noyade
- [ ] Pas de gore, pas de marque, pas de vraie victime
- [ ] Short : boucle fin → début testée
