## Over-The-Wire -writeup-
### Bandit5 (bandit5@bandit.labs.overthewire.org)

---
#### Etape 1

On se retrouve avec de nombreux dossiers dans lesquels se trouvent de nombreux fichiers, certains executables, d'autres non, parfois nommés différement...
<details>
<summary>/Voir le log complet de 'find .'/</summary>
./maybehere09
./maybehere09/.file2
./maybehere09/.file1
./maybehere09/-file3
./maybehere09/-file2
./maybehere09/-file1
./maybehere09/spaces file3
./maybehere09/spaces file2
./maybehere09/spaces file1
./maybehere09/.file3
./maybehere01
./maybehere01/.file2
./maybehere01/.file1
./maybehere01/-file3
./maybehere01/-file2
./maybehere01/-file1
./maybehere01/spaces file3
./maybehere01/spaces file2
./maybehere01/spaces file1
./maybehere01/.file3
./maybehere13
./maybehere13/.file2
./maybehere13/.file1
./maybehere13/-file3
./maybehere13/-file2
./maybehere13/-file1
./maybehere13/spaces file3
./maybehere13/spaces file2
./maybehere13/spaces file1
./maybehere13/.file3
./maybehere04
./maybehere04/.file2
./maybehere04/.file1
./maybehere04/-file3
./maybehere04/-file2
./maybehere04/-file1
./maybehere04/spaces file3
./maybehere04/spaces file2
./maybehere04/spaces file1
./maybehere04/.file3
./maybehere06
./maybehere06/.file2
./maybehere06/.file1
./maybehere06/-file3
./maybehere06/-file2
./maybehere06/-file1
./maybehere06/spaces file3
./maybehere06/spaces file2
./maybehere06/spaces file1
./maybehere06/.file3
./maybehere19
./maybehere19/.file2
./maybehere19/.file1
./maybehere19/-file3
./maybehere19/-file2
./maybehere19/-file1
./maybehere19/spaces file3
./maybehere19/spaces file2
./maybehere19/spaces file1
./maybehere19/.file3
./maybehere15
./maybehere15/.file2
./maybehere15/.file1
./maybehere15/-file3
./maybehere15/-file2
./maybehere15/-file1
./maybehere15/spaces file3
./maybehere15/spaces file2
./maybehere15/spaces file1
./maybehere15/.file3
./maybehere18
./maybehere18/.file2
./maybehere18/.file1
./maybehere18/-file3
./maybehere18/-file2
./maybehere18/-file1
./maybehere18/spaces file3
./maybehere18/spaces file2
./maybehere18/spaces file1
./maybehere18/.file3
./maybehere14
./maybehere14/.file2
./maybehere14/.file1
./maybehere14/-file3
./maybehere14/-file2
./maybehere14/-file1
./maybehere14/spaces file3
./maybehere14/spaces file2
./maybehere14/spaces file1
./maybehere14/.file3
./maybehere11
./maybehere11/.file2
./maybehere11/.file1
./maybehere11/-file3
./maybehere11/-file2
./maybehere11/-file1
./maybehere11/spaces file3
./maybehere11/spaces file2
./maybehere11/spaces file1
./maybehere11/.file3
./maybehere00
./maybehere00/.file2
./maybehere00/.file1
./maybehere00/-file3
./maybehere00/-file2
./maybehere00/-file1
./maybehere00/spaces file3
./maybehere00/spaces file2
./maybehere00/spaces file1
./maybehere00/.file3
./maybehere17
./maybehere17/.file2
./maybehere17/.file1
./maybehere17/-file3
./maybehere17/-file2
./maybehere17/-file1
./maybehere17/spaces file3
./maybehere17/spaces file2
./maybehere17/spaces file1
./maybehere17/.file3
./maybehere10
./maybehere10/.file2
./maybehere10/.file1
./maybehere10/-file3
./maybehere10/-file2
./maybehere10/-file1
./maybehere10/spaces file3
./maybehere10/spaces file2
./maybehere10/spaces file1
./maybehere10/.file3
./maybehere16
./maybehere16/.file2
./maybehere16/.file1
./maybehere16/-file3
./maybehere16/-file2
./maybehere16/-file1
./maybehere16/spaces file3
./maybehere16/spaces file2
./maybehere16/spaces file1
./maybehere16/.file3
./maybehere03
./maybehere03/.file2
./maybehere03/.file1
./maybehere03/-file3
./maybehere03/-file2
./maybehere03/-file1
./maybehere03/spaces file3
./maybehere03/spaces file2
./maybehere03/spaces file1
./maybehere03/.file3
./maybehere08
./maybehere08/.file2
./maybehere08/.file1
./maybehere08/-file3
./maybehere08/-file2
./maybehere08/-file1
./maybehere08/spaces file3
./maybehere08/spaces file2
./maybehere08/spaces file1
./maybehere08/.file3
./maybehere02
./maybehere02/.file2
./maybehere02/.file1
./maybehere02/-file3
./maybehere02/-file2
./maybehere02/-file1
./maybehere02/spaces file3
./maybehere02/spaces file2
./maybehere02/spaces file1
./maybehere02/.file3
./maybehere07
./maybehere07/.file2
./maybehere07/.file1
./maybehere07/-file3
./maybehere07/-file2
./maybehere07/-file1
./maybehere07/spaces file3
./maybehere07/spaces file2
./maybehere07/spaces file1
./maybehere07/.file3
./maybehere12
./maybehere12/.file2
./maybehere12/.file1
./maybehere12/-file3
./maybehere12/-file2
./maybehere12/-file1
./maybehere12/spaces file3
./maybehere12/spaces file2
./maybehere12/spaces file1
./maybehere12/.file3
./maybehere05
./maybehere05/.file2
./maybehere05/.file1
./maybehere05/-file3
./maybehere05/-file2
./maybehere05/-file1
./maybehere05/spaces file3
./maybehere05/spaces file2
./maybehere05/spaces file1
./maybehere05/.file3
</details>

On sait également que **le fichier qui contient le mot de passe a des critères précis**:
- Lisible par un humain
- Taille: 1033 bytes
- Non-executable

---
#### Etape 2

Utilisons `find` et quelques uns de ses arguments pour trouver facilement le fichier correct:
La commande `find . -type f -size 1033c ! -executable` demande le `type` > fichier, la taille `size` > 1033 bytes, et que le fichier soit `! -executable` > non-executable *(Négation: '!')*

`find . -type f -size 1033c ! -executable` nous renvoie:
> ./maybehere07/.file2

---
#### Etape 3

`cat ./maybehere07/.file2` renvoie:
> DXjZPULLxYr17uwoI01bNLQbtFemEgo7

---
Mot de passe: **DXjZPULLxYr17uwoI01bNLQbtFemEgo7**

[<< bandit4.md](bandit4.md) | bandit5.md | [bandit6.md >>](bandit6.md)
