## Over-The-Wire -writeup-
### Natas8 (http://natas8.natas.labs.overthewire.org/)

---
#### Etape 1

Comme Natas7, on regarde le code source donné par le bouton, et on y trouve encore du PHP:

```php
<?

$encodedSecret = "3d3d516343746d4d6d6c315669563362";

function encodeSecret($secret) {
    return bin2hex(strrev(base64_encode($secret)));
}

if(array_key_exists("submit", $_POST)) {
    if(encodeSecret($_POST['secret']) == $encodedSecret) {
    print "Access granted. The password for natas9 is <censored>";
    } else {
    print "Wrong secret";
    }
}
?>
```

Ici, il faut que la clé encryptée ($encodedSecret, de valeur 3d3d516343746d4d6d6c315669563362) soit égale à l'input de l'utilisateur **traitée par la fonction *encodeSecret***.  

**L'input de l'utilisateur va être**:
- 1: Encodé en Base64
- 2: Inversé
- 3: Converti en représentation hexadécimale (depuis données binaires)  
*La ligne qui effectue ces manipulations: return bin2hex(strrev(base64_encode($secret)));*

---
#### Etape 2

On a donc le processus de manipulation de l'input de l'utilisateur, et la clé qui doit correspondre une fois que ces manipulations ont été effectuées.

Pour trouver l'input correct que l'utilisateur doit entrer, il suffit de prendre la clé finale encodée ($encodedSecret) et appliquer les transformations **à l'envers, à l'envers !** C'est à dire dans cet ordre :
- **1: hex2bin** (au lieu de bin2hex)
- **2: strrev** (inverser une phrase n'a pas d'inverse. Inverser va dans les deux sens : maison > nosiam > maison)
- **3: decode64** (au lieu de encode64)

**Entamons les transformations dans l'ordre**. La clé finale encodée est : *3d3d516343746d4d6d6c315669563362*  
- *3d3d516343746d4d6d6c315669563362* > **hex2bin** > ==QcCtmMml1ViV3b ;  
- ==QcCtmMml1ViV3b > **strrev** > b3ViV1lmMmtCcQ== ;  
- b3ViV1lmMmtCcQ== > **decode64** > oubWYf2kBq .  

---
#### Etape 3

Notre input devrait donc être **oubWYf2kBq**.  
Après avoir rentré cet input, du texte est inséré dans l'HTML :
> Access granted. The password for natas9 is W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl

---
Mot de passe: **W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl**



