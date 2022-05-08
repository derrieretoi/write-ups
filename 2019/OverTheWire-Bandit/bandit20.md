## Over-The-Wire -writeup-
### Bandit20 (bandit20@bandit.labs.overthewire.org)

---
#### Etape 1

Dans notre dossier se trouve un fichier `suconnect`. On sait également que le mot de passe sera donné si `suconnect` reçoit le mot de passe du niveau actuel.

Quand on l'exécute, on a:

```console
bandit20@bandit:~$ ./suconnect 
Usage: ./suconnect <portnumber>
This program will connect to the given port on localhost using TCP. If it receives the correct password from the other side, the next password is transmitted back.
```
Il va donc falloir mettre en place un **'listener'** avec netcat qui renverras le mot de passe actuel quand il y a une connexion entrante.

---
#### Etape 2

Tout d'abord regardons les ports ouverts, pour ne pas les dupliquer.

```console
bandit20@bandit:~$ nmap localhost

Starting Nmap 7.40 ( https://nmap.org ) at 2019-12-17 17:44 CET
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00023s latency).
Not shown: 997 closed pbandit20@bandit:~$ ./suconnect 60000
Read: GbKksEFF4yrVs6il55v6gwY5aVje5f0j
Password matches, sending next password
orts
PORT      STATE SERVICE
22/tcp    open  ssh
6025/tcp  open  x11
30000/tcp open  ndmps

Nmap done: 1 IP address (1 host up) scanned in 0.10 seconds
```

---
#### Etape 3

On va prendre le port 60000 et créer un *listener*. L'option **-l** signifie *listen*, et **-p** signifie le *port*:

```console
bandit20@bandit:~$ echo "GbKksEFF4yrVs6il55v6gwY5aVje5f0j" | nc -l -p 60000
|
```
 
Notre listener est mis en place, prêt à *echo* le mot de passe.  
Maintenant il va falloir que `suconnect` se connecte dessus, autrement dit, ouvrir un second terminal, et se connecter.

---
#### Etape 4

**Dans un nouveau terminal**:

```console
bandit20@bandit:~$ ./suconnect 60000
Read: GbKksEFF4yrVs6il55v6gwY5aVje5f0j
Password matches, sending next password
```

---
`suconnect` à reçu le mot de passe, et indique qu'ils correspondent, puis envoie le prochain mot de passe.  
Le mot de passe en question est envoyé sur le *listener* netcat que l'on a créé. Si on regarde sur notre premier terminal, on peut lire, à la suite de la ligne vide:
> gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr

---
Mot de passe: **gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr**

[<< bandit19.md](bandit19.md) | bandit20.md | [bandit21.md >>](bandit21.md)
