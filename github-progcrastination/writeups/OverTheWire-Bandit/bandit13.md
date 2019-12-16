## Over-The-Wire -writeup-
### Bandit13 (bandit13@bandit.labs.overthewire.org)

---
#### Etape 1

Le mot de passe se trouve désormais dans `/etc/bandit_pass/bandit14`, **et n'est lisible que par l'utilisateur bandit14**.  
On nous donne également un fichier `sshkey.private`, qui est une clé SSH privée.

Il faut donc se connecter via SSH en tant que **bandit14** avec la clé SSH privée donnée *(avec l'option **-i** qui permet de se connecter avec une clé privée)*.

```console
bandit13@bandit:~$ ssh -i sshkey.private bandit14@localhost
Could not create directory '/home/bandit13/.ssh'.
The authenticity of host 'localhost (127.0.0.1)' can't be established.
ECDSA key fingerprint is SHA256:98UL0ZWr85496EtCRkKlo20X3OPnyPSB5tB5RPbhczc.
Are you sure you want to continue connecting (yes/no)? 
```

On confirme, et nous voilà connecté en tant que **bandit14**.

---
#### Etape 2

Il ne nous reste plus qu'à aller chercher le mot de passe:
```console
bandit14@bandit:~$ cat /etc/bandit_pass/bandit14 
4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e
```

---
Mot de passe: **4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e**
