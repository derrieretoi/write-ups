## Over-The-Wire -writeup-
### Bandit18 (bandit18@bandit.labs.overthewire.org)

---
#### Etape 1

Le mot de passe est dans le fichier *readme**. Malheureusement quelqu'un a modifié le fichier **bashrc** qui nous déconnecte quand on se connecte avec SSH.

La solution serait d'utiliser l'option **-t** qui force un *pseudo-tty*, et ajouter une commande après notre commande ssh, comme par exemple:
`ssh -t bandit18@bandit.labs.overthewire.org -p 2220 cat readme` qui nous renvoie le mot de passe.

Cependant, il serait plus propre d'appeler `/bin/sh` après la commande SSH, pour avoir accès à un terminal et trouver le mot de passe:

```console
leo@oleole:~$ ssh -t bandit18@bandit.labs.overthewire.org -p 2220 /bin/sh
```

nous demande le mot de passe, qui nous renvoie ensuite `$`, un terminal prêt à l'emploi.

---
#### Etape 2

Trouvons donc le mot de passe:

```console
$ ls
readme
```

puis:

```console
$ cat readme
IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x
```

---
Mot de passe: **IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x**
