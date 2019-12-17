## Over-The-Wire -writeup-
### Bandit14 (bandit14@bandit.labs.overthewire.org)

---
#### Etape 1

On nous fait savoir que le mot de passe peut être récupéré en envoyant le mot de passe du niveau actuel au **port 30000 sur localhost**.

Utilisons `telnet` !  
`telnet [host] [port]` prendra comme argument **localhost** et **30000**:

```console
bandit14@bandit:~/.ssh$ telnet localhost 30000
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
```

---
#### Etape 2

`telnet` est maintenant connecté, et il ne nous reste plus qu'à envoyer le mot de passe du niveau actuel:

```console
4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e
Correct!
BfMYroe26WYalil77FoDi9qh59eK5xNr

Connection closed by foreign host.
```

---
Mot de passe: **BfMYroe26WYalil77FoDi9qh59eK5xNr**
