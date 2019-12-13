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

Le fichiers "secret.inc" est inclus dans la page HTML, et ensuite PHP compare ce que l'utilisateur entre comme code ($_POST['secret']) et le code secret du serveur (qui se trouve dans secret.inc)  

On va donc récupérer le fichier secret.inc qui se trouve dans le dossier /includes/ du site.

Pour cela j'utilise **wget** :

*Structure de la commande*
