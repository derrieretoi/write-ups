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

Ici, il faut que la clé encryptée ($encodedSecret) soit égale à l'input de l'utilisateur **traitée par la fonction *encodeSecret***.  
L'input de l'utilisateur va être:
- Encodé en Base64
- Inversé
- Converti en représentation hexadécimale (depuis données binaires)

