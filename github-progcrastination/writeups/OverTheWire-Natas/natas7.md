## Over-The-Wire -writeup-
### Natas7 (http://natas7.natas.labs.overthewire.org/)

---
#### Etape 1

On observe le code source (Ctrl+U) et on trouve un commentaire:
> <!-- hint: password for webuser natas8 is in /etc/natas_webpass/natas8 -->

Il y aurait une faille pour piocher des fichiers dans les disques distants.  
L'URL du site se compose comme ceci:
> http://natas7.natas.labs.overthewire.org/index.php?page=home < pour la page *home*
et
> http://natas7.natas.labs.overthewire.org/index.php?page=about < pour la page *about*
