## Over-The-Wire -writeup-
### Natas11 (http://natas11.natas.labs.overthewire.org/)

---
#### Etape 1

###### *Aidé pour celui-ci*  

"Les cookies sont protégés par une encryption XOR".  
En regardant le code source, on voit que l'array `$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");` est encodé en Base64, puis encrypté en XOR avec une clé que l'on ne connaît pas.

Cependant on connait l'entrée *(l'array **$defaultdata**)*, et la sortie: notre cookie nommé "data", de valeur **ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw=**.

---
#### Etape 2

L'algorithme d'encryption XOR est le suivant:

```php

function xor_encrypt($in) {
    $key = '<censored>';
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}
```

Pour retrouver, il faut appliquer l'encryption à l'envers, car XOR est commutatif.

*// Draw the fucking owl*
P xor K = C
C xor K = P
P xor C = K

On trouve donc la clé XOR: **"qw8J"**.

---
#### Etape 3

Maintenant, on modifie l'array `"showpassword"=>"no", "bgcolor"=>"#ffffff"` en `"showpassword"=>"yes", "bgcolor"=>"#ffffff"` et on l'encrypte ave la clé avec XOR, et on l'encode en Bas64.  

---
#### Etape 4

Le résultat est donc la valeur que doit avoir notre cookie: **ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK**  
On remplace la valeur, et en rechargeant la page, on obtient:
> The password for natas12 is EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3

---
Mot de passe: **EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3**
