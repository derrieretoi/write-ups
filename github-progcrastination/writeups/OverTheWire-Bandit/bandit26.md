## Over-The-Wire -writeup-
### Bandit26 (bandit26@bandit.labs.overthewire.org)
###### /Tout petit peu/ Aidé pour celui-ci
---
#### Etape 1

*"Bonne chance pour avoir un shell ! Dépéchez-vous et attrapez le mot de passe!"*  
Nous avons maintenant le mot de passe pour nous connecter directement à **bandit26**.

Mais nous nous heurtons toujours au shell `/usr/bin/showtext` de **bandit26**, on va donc ouvrir un terminal depuis vim !

Pendant que nous sommes dans `more`, on appuie sur **v** pour entrer une commande, et on tape `shell`.  
Mais cela nous renvoie à la bannière de texte. Car on invoque le shell, mais le shell est `showtext` !

Il va donc falloir **déclarer le chemin du shell à Vim**. Pour cela, on tape la commande `set shell=/bin/sh` dans vim.

---
#### Etape 2

Maintenant que le shell est définit correctement, on l'invoque dans vim, avec `shell`.

Regardons ce qu'il se trouve dans `/home/bandit26` !

```console
 | |                   | (_) | |__ \ / /
 | |__   __ _ _ __   __| |_| |_   ) / /_
 | '_ \ / _` | '_ \ / _` | | __| / / '_ \
:shell
$ ls
bandit27-do  text.txt
```

Il y a un *bandit27-do* qui, si on se souvient des challenges précédents, permet d'exécuter des commandes **en tant que** bandit27, ou plutôt, avec ses permissions.

---
#### Etape 3

Il ne nous reste plus qu'à prendre le mot de passe de **bandit27**, grâce à ses permissions:

```console
$ ./bandit27-do cat /etc/bandit_pass/bandit27
3ba3118a22e93127a4ed485be72ef5ea
```

---
Mot de passe: **/**

[<< bandit25.md](bandit25.md) | bandit26.md | [bandit27.md >>](bandit27.md)
