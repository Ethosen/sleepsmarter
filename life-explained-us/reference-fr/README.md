# reference-fr/

Dépose ici les transcriptions des vidéos de La Vie Expliquée (`<slug>.txt` ou `.srt`),
une par vidéo, pour caler les scripts US phrase par phrase sur les originaux.

Exemple pour les récupérer en local (là où YouTube est accessible) :

```bash
pip install yt-dlp
yt-dlp --skip-download --write-auto-subs --sub-langs fr --convert-subs srt \
  -o "%(title)s.%(ext)s" "https://www.youtube.com/@lavieexpliquee/videos"
```
