## Over-The-Wire -writeup-
### Bandit29 (bandit29@bandit.labs.overthewire.org)
---
#### Etape 1

*Voir [bandit27](bandit27.md) pour cloner un dépôt.* Ensuite, il faut dénicher le mot de passe.  
On a un **README.md**, encore une fois, mais cette fois ci qui ne contient pas de modifications particulières dans les logs:

```console
bandit29@bandit:/tmp/visage/repo$ cat README.md 
# Bandit Notes
Some notes for bandit30 of bandit.

## credentials

- username: bandit30
- password: <no passwords in production!>
```

Et seulement 2 commits qui ne nous intéressent pas:

```console
commit 84abedc104bbc0c65cb9eb74eb1d3057753e70f8
Author: Ben Dover <noone@overthewire.org>
Date:   Tue Oct 16 14:00:41 2018 +0200

    fix username

diff --git a/README.md b/README.md
index 2da2f39..1af21d3 100644
--- a/README.md
+++ b/README.md
@@ -3,6 +3,6 @@ Some notes for bandit30 of bandit.
 
 ## credentials
 
-- username: bandit29
+- username: bandit30
 - password: <no passwords in production!>
 

commit 9b19e7d8c1aadf4edcc5b15ba8107329ad6c5650
Author: Ben Dover <noone@overthewire.org>
Date:   Tue Oct 16 14:00:41 2018 +0200

    initial commit of README.md

diff --git a/README.md b/README.md
new file mode 100644
index 0000000..2da2f39
--- /dev/null
+++ b/README.md
@@ -0,0 +1,8 @@
+# Bandit Notes
+Some notes for bandit30 of bandit.
+
+## credentials
+
+- username: bandit29
+- password: <no passwords in production!>
```

---
#### Etape 2

Alors on va vérifier si il n'existe pas d'autres branches dans le dépôt *git*:

```console
bandit29@bandit:/tmp/visage/repo$ git branch -a
* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/dev
  remotes/origin/master
  remotes/origin/sploits-dev
```

Allons voir ce que la branche *dev* contient

---
#### Etape 3

```console
bandit29@bandit:/tmp/visage/repo$ git pull origin dev

[...]

From ssh://localhost/home/bandit29-git/repo
 * branch            dev        -> FETCH_HEAD
Updating 84abedc..33ce2e9
Fast-forward
 README.md         | 2 +-
 code/gif2ascii.py | 1 +
 2 files changed, 2 insertions(+), 1 deletion(-)
 create mode 100644 code/gif2ascii.py
```

On a pu récupérer un script Python, et un fichier README.md, modifié.  
Regardons le README.md de plus près:

```console
bandit29@bandit:/tmp/visage/repo$ cat README.md 
# Bandit Notes
Some notes for bandit30 of bandit.

## credentials

- username: bandit30
- password: 5b90576bedb2cc04c86a9e924ce42faf
```

---
Mot de passe: **5b90576bedb2cc04c86a9e924ce42faf**

[<< bandit28.md](bandit28.md) | bandit29.md | [bandit30.md >>](bandit30.md)
