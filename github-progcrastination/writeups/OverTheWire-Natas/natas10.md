## Over-The-Wire -writeup-
### Natas10 (http://natas10.natas.labs.overthewire.org/)

---
#### Etape 1

En inspectant le code source, on trouve que la fonction `preg_match()` nous empêche d'exploiter la fonction grep avec ";".  
Cependant on peut quand même exploiter *grep*, en cherchant plusieurs fichiers en même temps:

Tout d'abord on rentre `.` (car `.*` renvoie les fichiers avec un caractère ou plus (* = repetition (?))) puis le second fichier: `/etc/natas_webpass/natas11`.

Après avoir entré `. /etc/natas_webpass/natas11` on nous renvoie
> /etc/natas_webpass/natas11:U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK

---
Mot de passe: **U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK**
