## Over-The-Wire -writeup-
### Bandit27 (bandit27@bandit.labs.overthewire.org)
---
#### Etape 1

*"Il y a un dépôt git sous **ssh://bandit27-git@localhost/home/bandit27-git/repo**.  
Le mot de passe pour l'utilisateur **bandit27-git** est le même que pour **bandit27**. Clonez le dépôt."*

Aussi, nous n'avons pas la permission d'accéder au dossier directement.  
On va donc cloner directement le dépôt.

```console
bandit27@bandit:/tmp/visages$ git clone ssh://bandit27-git@localhost/home/bandit27-git/repo
Cloning into 'repo'...
Could not create directory '/home/bandit27/.ssh'.
The authenticity of host 'localhost (127.0.0.1)' can't be established.
ECDSA key fingerprint is SHA256:98UL0ZWr85496EtCRkKlo20X3OPnyPSB5tB5RPbhczc.
Are you sure you want to continue connecting (yes/no)?
```
Puis après avoir répondu oui:
```console
Failed to add the host to the list of known hosts (/home/bandit27/.ssh/known_hosts).
This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

bandit27-git@localhost's password: |
```
Et après avoir donné le mot de passe:
```console
remote: Counting objects: 3, done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 0 (delta 0)
Receiving objects: 100% (3/3), done.
```

---
#### Etape 2

*git clone* nous a donné un dossier `repo` qui contient un *README*
```console
bandit27@bandit:/tmp/visages$ ls repo/
README
```

Qui nous donne:

```console
bandit27@bandit:/tmp/visages$ cat repo/README 
The password to the next level is: 0ef186ac70e04ea33b4c1853d2526fa2
```


---
Mot de passe: **0ef186ac70e04ea33b4c1853d2526fa2**

[<< bandit26.md](bandit26.md) | bandit27.md | [bandit28.md >>](bandit28.md)
