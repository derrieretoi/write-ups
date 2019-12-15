## Over-The-Wire -writeup-
### Bandit8 (bandit8@bandit.labs.overthewire.org)

---
#### Etape 1

Le mot de passe se trouve encore dans **data.txt**, et n'apparaît qu'une fois dans le fichier.  
On examine le début de *data.txt*:

```console
bandit8@bandit:~$ cat data.txt |head
KerqNiDbY0zV2VxnOCmWX5XWxumldlAe
MsxcvOe3PGrt78wpZG2bBNF5wfXpZhET
L0nxAwlfV9V3J5onKIT8KYQ9InTcQ7yE
4c7EsUtqLnLR9hiepV5EQVhdMgyi8onL
1drBmDT7PYS7hVgoTWkJSjUZUK7ZAIAa
L0nxAwlfV9V3J5onKIT8KYQ9InTcQ7yE
78rgduVcLZjLzZmooObdaN541MKV6IfQ
x0bga8Oxz5lgM8k52HrYy4ez7XJI0lM0
irGm6F73sbUrFhHukhp6JXgMQyLxJTz1
YzZX7E35vOa6IQ9SRUGdlEpyaiyjvWXE
```

Il va donc falloir *trier*, puis *dédoublonner* les lignes, avec **sort** et **uniq** respectivement.

---
#### Etape 2

`sort data.txt` va trier les lignes par ordre alphabétique.  
`uniq -u` renvoie uniquement les lignes *uniques*.

On *pipe* donc ces deux commandes:
```console
bandit8@bandit:~$ sort data.txt |uniq -u
UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR
```

---
Mot de passe: **UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR**
