## Over-The-Wire -writeup-
### Bandit20 (bandit20@bandit.labs.overthewire.org)

---
#### Etape 1

Dans notre dossier se trouve un fichier `suconnect`.

```console
bandit20@bandit:~$ file suconnect 
suconnect: setuid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=74c0f6dc184e0412b6dc52e542782f43807268e1, not stripped
```

Quand on l'exécute, on a:

```console
bandit20@bandit:~$ ./suconnect 
Usage: ./suconnect <portnumber>
This program will connect to the given port on localhost using TCP. If it receives the correct password from the other side, the next password is transmitted back.
```

---
#### Etape 2

Il faut donc envoyer le mot de passe actuel à un port sur localhost, qui nous renverras le mot de passe du niveau suivant.  
Scannons déjà les ports ouverts sur localhost !

```console
bandit20@bandit:~$ nmap localhost

Starting Nmap 7.40 ( https://nmap.org ) at 2019-12-17 16:02 CET
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00019s latency).
Not shown: 998 closed ports
PORT      STATE SERVICE
22/tcp    open  ssh
30000/tcp open  ndmps

Nmap done: 1 IP address (1 host up) scanned in 0.09 seconds
```

On a donc le port 22 qui est ouvert.

---
#### Etape 3

Envoyons le mot de passe:

```console
bandit20@bandit:~$ ./suconnect 22 |echo GbKksEFF4yrVs6il55v6gwY5aVje5f0j
GbKksEFF4yrVs6il55v6gwY5aVje5f0j
```

---
Mot de passe: **GbKksEFF4yrVs6il55v6gwY5aVje5f0j**
