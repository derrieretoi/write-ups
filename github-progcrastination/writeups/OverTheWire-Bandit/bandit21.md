## Over-The-Wire -writeup-
### Bandit21 (bandit21@bandit.labs.overthewire.org)

---
#### Etape 1

On nous informe qu'un programme est exécuté à intervalles réguliers par **cron**, un programme qui automatise les tâches.  
Il faut regarder dans **/etc/cron.d** et examiner la commande de plus près.

```console
bandit21@bandit:/etc/cron.d$ ls
atop  cronjob_bandit22  cronjob_bandit23  cronjob_bandit24
```

Le programme qui nous intéresse s'appelle donc **cronjob_bandit22**, et voici ce qu'il contient:

```console
bandit21@bandit:/etc/cron.d$ cat cronjob_bandit22 
@reboot bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
* * * * * bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
```

Chaque minute, il éxécute un script (`/usr/bin/cronjob_bandit22.sh`) et redirige `stdout` et `stderr` dans /dev/null.  
Ce qui va nous intéresser va être ce script qui est éxécuté. Allons donc l'examiner de plus près.

---
#### Etape 2

```console
bandit21@bandit:/etc/cron.d$ cat /usr/bin/cronjob_bandit22.sh 
#!/bin/bash
chmod 644 /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
cat /etc/bandit_pass/bandit22 > /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
```

Il semblerait que ce soit un script **bash**, qui affiche puis redirige le mot de passe du niveau suivant, dans un fichier temporaire appelé **t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv**.

---
#### Etape 3

Il ne nous reste plus qu'à regarder le contenu de ce fichier temporaire:

```console
bandit21@bandit:/etc/cron.d$ cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI
```

---
Mot de passe: **Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI** 
