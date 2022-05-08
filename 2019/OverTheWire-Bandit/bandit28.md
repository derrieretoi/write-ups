## Over-The-Wire -writeup-
### Bandit28 (bandit28@bandit.labs.overthewire.org)
---
#### Etape 1

*Voir [bandit27](bandit27.md) pour cloner le dépôt de **bandit28-git** depuis **ssh://bandit28-git@localhost/home/bandit28-git/repo**.*

On trouve dans ce dépôt un fichier **README.md**:

```console
bandit28@bandit:/tmp/visages/repo$ cat README.md 
# Bandit Notes
Some notes for level29 of bandit.

## credentials

- username: bandit29
- password: xxxxxxxxxx
```

Cependant, le mot de passe est caché.

---
#### Etape 2

L'extension **.md** *(Markdown)*, ne permet pas de cacher du texte si on l'ouvre avec un éditeur. Et ici, le texte est littéralement 'xxxxxx'.

Cependant, on peut fouiller dans les *logs git* pour vérifier que le fichier *README.md* n'ai pas été modifié:

```console
bandit28@bandit:/tmp/visages/repo$ git log --oneline
073c27c fix info leak
186a103 add missing data
b67405d initial commit of README.md
```

---
#### Etape 3

*add missing data* semble être un *commit* intéressant. On peut examiner les changements avec l'argument **-p** (et l'argument **-2** qui sélectionne le 2eme commit précédent):

```console
bandit28@bandit:/tmp/visages/repo$ git log -p -2
commit 073c27c130e6ee407e12faad1dd3848a110c4f95
Author: Morla Porla <morla@overthewire.org>
Date:   Tue Oct 16 14:00:39 2018 +0200

    fix info leak

diff --git a/README.md b/README.md
index 3f7cee8..5c6457b 100644
--- a/README.md
+++ b/README.md
@@ -4,5 +4,5 @@ Some notes for level29 of bandit.
 ## credentials
 
 - username: bandit29
-- password: bbc96594b4e001778eee9975372716b2
+- password: xxxxxxxxxx
 

commit 186a1038cc54d1358d42d468cdc8e3cc28a93fcb
Author: Morla Porla <morla@overthewire.org>
Date:   Tue Oct 16 14:00:39 2018 +0200

    add missing data

diff --git a/README.md b/README.md
index 7ba2d2f..3f7cee8 100644
--- a/README.md
+++ b/README.md
@@ -4,5 +4,5 @@ Some notes for level29 of bandit.
 ## credentials
 
 - username: bandit29
-- password: <TBD>
+- password: bbc96594b4e001778eee9975372716b2
```

C'est long, mais on peut voir qu'il y a eu des modifications!

---
#### Etape 4

Dans le commit: **fix info leak**
- -- password: bbc96594b4e001778eee9975372716b2
- +- password: xxxxxxxxxx

Dans le commit: **add missing data**
- -- password: <TBD>
- +- password: bbc96594b4e001778eee9975372716b2

On remarque que le mot de passe a été ajouté, puis retiré dans un commit suivant.

---
Mot de passe: **bbc96594b4e001778eee9975372716b2**

[<< bandit27.md](bandit27.md) | bandit28.md | [bandit29.md >>](bandit29.md)
