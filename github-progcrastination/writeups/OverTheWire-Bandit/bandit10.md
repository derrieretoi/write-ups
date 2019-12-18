## Over-The-Wire -writeup-
### Bandit10 (bandit10@bandit.labs.overthewire.org)

---
#### Etape 1

Le mot de passe se trouve **encore** dans data.txt, et comme d'habitude quelque chose à encore changé: le contenu du fichier est **encodé en Base64**.  
Mais nous sommes chanceux, la commande `base64` va tout faire pour nous.

On exécute la commande `base64 -d [filename]` qui va, avec l'argument **-d**, décoder notre fichier et nous donner le résultat:
```console
bandit10@bandit:~$ base64 -d data.txt 
The password is IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR
```

---
Mot de passe: **IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR**

[<< bandit9.md](bandit9.md) | bandit10.md | [bandit11.md >>](bandit11.md)
