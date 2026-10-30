# 04 — Direction artistique : illustrations « États-Unis »

## Principe

Même grammaire visuelle que la chaîne FR (illustrations fixes animées + surimpressions
anatomiques), mais **chaque décor doit crier « Amérique » en moins d'une seconde**.

## Style unique de la chaîne

- **Rendu** : illustration digitale semi-réaliste, style roman graphique / editorial illustration,
  lumière cinéma, grain léger.
- **Palette** : nuit bleu-acier + orange sodium des lampadaires US ; accents rouges uniquement
  pour le corps (cœur, sang dans les vaisseaux, signaux de douleur).
- **Couche anatomique** : vue « rayons X » translucide, cyan lumineux, superposée au personnage.
  C'est ce qui remplace le gore : on montre l'intérieur du corps, jamais une blessure ouverte.
- **Personnage** : silhouette générique, visage peu détaillé ou de dos — le spectateur doit
  pouvoir s'y projeter. Varier âge/origine d'un épisode à l'autre.
- **Format** : 16:9 (1920×1080) pour le long ; 9:16 (1080×1920) recadré pour le Short —
  composer avec le sujet au centre pour que le recadrage fonctionne.

## Banque de marqueurs « USA » à placer dans les décors

| Catégorie | Éléments |
|---|---|
| Route | Feux jaunes suspendus à un câble, panneau « WALK / DON'T WALK » à main orange, pickup trucks, SUV larges, interstate signs vertes, école jaune bus |
| Ville | Fire hydrant rouge, poteaux électriques en bois, enseignes de diner, parking de Walmart-type (sans logo), stations-service avec auvent |
| Nature | Saguaros (Arizona), cyprès et alligators (Floride), grandes plaines + tornade (Kansas/Oklahoma), Death Valley, Yellowstone, Rocheuses |
| Intérieur | Mobile home, salle de bain avec rideau de douche, motel au néon, cuisine suburbaine |
| Secours | Ambulance US (boxy, rouge et blanc), « 911 », EMT en uniforme bleu marine, bombe de Narcan |
| Unités à l'écran | mph, °F, ft, lb |

**Interdits** : logos et marques réelles, visages de vraies personnes, drapeaux en gros plan
(cliché), uniformes de police réels, armes à feu mises en avant.

## Prompt de base (Midjourney / Flux / Ideogram / etc.)

```
[SCENE], American setting, [US MARKERS], semi-realistic digital illustration,
graphic novel style, cinematic lighting, sodium-orange street lights against
steel-blue night, subtle film grain, 16:9, no text, no logos, no gore
```

Couche anatomique (à générer séparément puis superposer au montage) :
```
translucent x-ray anatomical overlay of a human [ORGAN/SYSTEM], glowing cyan
lines on pure black background, medical illustration, clean, high detail, no text
```

Paramètres conseillés : `--ar 16:9 --style raw` (Midjourney) ; seed fixe par épisode pour la cohérence.

## Animation au montage

- Ken Burns lent (100 % → 108 % sur 4 s) sur les plans calmes.
- Zoom brusque (100 % → 130 % sur 6 images) sur les impacts, synchronisé au son.
- Fondu vers la couche rayons X quand la voix passe à « inside your body ».
- Compteur de temps à l'écran (`00:00.1`) en police monospace blanche — signature visuelle
  qui matérialise le « seconde par seconde ».
- Fin d'épisode : écran noir + battement de cœur qui s'arrête, puis plan « What saves you » en lumière chaude.
