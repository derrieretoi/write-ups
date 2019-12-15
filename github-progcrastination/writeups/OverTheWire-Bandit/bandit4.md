## Over-The-Wire -writeup-
### Bandit4 (bandit4@bandit.labs.overthewire.org)

---
#### Etape 1

Dans le dossier `inhere` se trouve des fichiers `-file0...`:
> bandit4@bandit:~/inhere$ ls  
> -file00  -file01  -file02  -file03  -file04  -file05  -file06  -file07  -file08  -file09

Le mot de passe se trouve dans le seul fichier qu'un humain peut lire, et effectivement, en essayant `cat ./-file00`, on trouve des caractères invalides, qui ne sont pas en UTF-8.

---
#### Etape 2

Il va donc falloir trouver lequel de ces fichiers contient une ligne avec **uniquement** des caractères UTF-8 valides.  
Pour cela on utilise **grep**:
`grep -x ".*" ./-file0*`

---
***Essayons de comprendre***:  
`grep -x` signifie *--line-regexp*, qui va trouver les correspondances exactes dans une ligne complète, et l'argument `".*"` signifie littéralement *tous les caractères*, soit les caractères encodés en UTF-8.  

On demande donc à grep de trouver une ligne complète de caractères valides dans les fichiers `./-file0*`, c'est à dire tout les fichiers qui commencent par **file0** (car on utilise une *wildcard* (le caractère *)).

`grep -x ".*" ./-file0*` nous retourne donc:
> ./-file07:koReBOKuIDDepwhWk7jZC0RTdopnAYKh

---
Mot de passe: **koReBOKuIDDepwhWk7jZC0RTdopnAYKh**
