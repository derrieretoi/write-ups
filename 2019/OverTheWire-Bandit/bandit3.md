## Over-The-Wire -writeup-
### Bandit3 (bandit3@bandit.labs.overthewire.org)

---
#### Etape 1

Il n'y a qu'un seul dossier nommé `inhere` dans le répertoire, et dans ce même dossier, rien ne s'y trouve.

Il faut donc utiliser des arguments supplémentaires avec `ls` pour vérifier si aucun fichier n'est caché dans le dossier `inhere`

On éxecute `ls -la inhere/` et on a:
>total 12  
>drwxr-xr-x 2 root    root    4096 Oct 16  2018 .  
>drwxr-xr-x 3 root    root    4096 Oct 16  2018 ..  
>-rw-r----- 1 bandit4 bandit3   33 Oct 16  2018 .hidden  

#### Etape 2

Il se trouve qu'il y a un fichier `.hidden` caché dans ce dossier.

On peut donc faire `cat inhere/.hidden`, qui nous donne:
> pIwrPrtPN36QITSp3EQaw936yaFoFgAB

---
Mot de passe: **pIwrPrtPN36QITSp3EQaw936yaFoFgAB**

[<< bandit2.md](bandit2.md) | bandit3.md | [bandit4.md >>](bandit4.md)
