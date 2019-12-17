## Over-The-Wire -writeup-
### Bandit22 (bandit22@bandit.labs.overthewire.org)

---
#### Etape 1

Encore une fois, une tâche automatisée est éxécutée par **cron** dans `/etc/cron.d`, et il faut examiner tout ça de plus près.  
`/etc/con.d` contient un fichier `cronjob_bandit23`, regardons le de plus près:

```console
bandit22@bandit:/etc/cron.d$ cat cronjob_bandit23 
@reboot bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
* * * * * bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
```

La tâche s'éxécute encore une fois chaque minute, et le script exécuté est `/usr/bin/cronjob_bandit23.sh`.

---
#### Etape 2

Décortiquons le script:

```console
bandit22@bandit:/etc/cron.d$ cat /usr/bin/cronjob_bandit23.sh 
#!/bin/bash

myname=$(whoami)
mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)

echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"

cat /etc/bandit_pass/$myname > /tmp/$mytarget
```

**Analyse**:
`myname = $(whoami)` attribue la valeur `bandit22` à *myname*
`mytarget = $(echo I am user $myname...` a pour valeur **"I am user bandit22"**, cependant, le résultat du *echo* est *pipé* à **md5sum** !  
Voilà ce qu'effectue **md5sum**:

```console
bandit22@bandit:/etc/cron.d$ echo I am user bandit22 | md5sum
8169b67bd894ddbb4412f91573b38db3  -
```

Donc `mytarget = $(8169b67bd894ddbb4412f91573b38db3  - | cut -d ' ' -f 1)` mais le résultat précédent est *encore* pipé vers une autre commande !  
Examinons la:
`cut -d ' ' -f 1` utilise l'option **-d** *delimiter*, et **-f** *fields*.  
*fields* marche si les mots sont séparés par des virgules, alors *delimiter* avec l'argument ' ' (espace) va permettre à *field* de découper les mots séparés par des espaces.

---
La commande **cut** sert à enlever l'espace et le tiret que **md5sum** créée. Ce qui nous donne finalement:
`mytarget = $(8169b67bd894ddbb4412f91573b38db3)`

Finalement, on lit qu'un message est affiché, puis que le programme affiche puis redirige le mot de passe dans un fichier temporaire:
`/tmp/$mytarget`. Ou autrement dit: `/tmp/8169b67bd894ddbb4412f91573b38db3`.

---
#### Etape 2 - Alternative

On peut également exécuter le programme pour regarder ce qu'il fait, tout simplement:

```console
bandit22@bandit:/etc/cron.d$ /usr/bin/cronjob_bandit23.sh 
Copying passwordfile /etc/bandit_pass/bandit22 to /tmp/8169b67bd894ddbb4412f91573b38db3
```

et regarder le résultat:

```console
bandit22@bandit:/etc/cron.d$ cat /tmp/8169b67bd894ddbb4412f91573b38db3
Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI
```

---
Mot de passe: **Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI**
