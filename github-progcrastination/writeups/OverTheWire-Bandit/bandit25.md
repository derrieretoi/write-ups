## Over-The-Wire -writeup-
### Bandit25 (bandit25@bandit.labs.overthewire.org)

---
#### Etape 1

On a a disposition un fichier **bandit26.sshkey** avec lequel on doit se connecter en tant que **bandit26**.  
Cependant, **bandit26 n'utilise pas /bin/shell** ! Il va falloir connaître le shell, savoir comment il fonctionne, et savoir s'en échapper.

Tout d'abord, **bandit26.sshkey** contient une *clé SSH privée*.  
Si on essaie de se connecter directement avec cette clé (et l'option **-i**):
