Il est possible de cacher du contenue a l'interieur d'une image JPG.
Cela peut permettre de transmettre du contenue sans eveiller les soupcons.



Demarche

L'exemple explique la marche a suivre pour cacher une archive RAR dans une
image JPG.

1. Selectionner une image JPG qui cachera le contenue.
2. Faire une archive RAR avec le contenue a transmettre.
3. Placer l'image et l'archive sur votre bureau.
4. Ensuite, il faut utiliser le gestionnaire de ligne de commande CMD.EXE
	Pour ce faire :


	Il faut ensuite ce deplacer sur le bureau:
		IMG 1
	Puis clicker sur entrer
		IMG 2

	Executer ensuite la commande suivante:
		copy /b NOM_DE_L-IMAGE.JPG + NOM_DE_L-ARCHIVE.RAR NOM_DU_FICHIER_IMAGE_QUI_CACHE_L-ARCHIVE.JPG



Principe

Grâce à la commande copy de windows, nous allons en faite placer notre contenue
à la suite de notre image. L'option /b traite le fichier comme un fichier binaire.
Cela fait que le fichier JPG sera copier entierement, ce qui inclue les
caracteres binaires de fins de fichiers. L'archive est copier ensuite, elle
est cache par une sorte "d'overflow de fichier". Nous depassons la zone de fichier
a traiter et y placon notre archive.

Les logiciels de traitement de fichier JPG ne feont pas de difference entre l'image
originale et la copie qui inclue l'archive.



Pour aller plus loin

Il est egalement possible de cacher des archives comme ZIP, 7ZP...
