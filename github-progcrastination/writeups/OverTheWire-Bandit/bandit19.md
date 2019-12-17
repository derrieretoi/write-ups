## Over-The-Wire -writeup-
### Bandit19 (bandit19@bandit.labs.overthewire.org)

---
#### Etape 1

Il faut utiliser le **fichier setuid** à notre disposition pour pouvoir récupérer la clé. Executez le pour savoir comment l'utiliser.    
`ls` nous révèle `bandit20-do`, un fichier de type:

```console
bandit19@bandit:~$ file bandit20-do 
bandit20-do: setuid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=8e941f24b8c5cd0af67b22b724c57e1ab92a92a1, not stripped
```

Du coup on l'éxecute:

```console
bandit19@bandit:~$ ./bandit20-do 
Run a command as another user.
  Example: ./bandit20-do id
```

---
#### Etape 2

Ce fichier permet donc d'éxecuter des commandes en tant que **bandit20**, ou du moins, avec ses permissions.  
Il ne nous reste plus qu'à trouver le mot de passe dans `/etc/bandit_pass/` !

```console
bandit19@bandit:~$ ./bandit20-do cat /etc/bandit_pass/bandit20
GbKksEFF4yrVs6il55v6gwY5aVje5f0j
```

---
Mot de passe: **GbKksEFF4yrVs6il55v6gwY5aVje5f0j**
