## Over-The-Wire -writeup-
### Bandit11 (bandit11@bandit.labs.overthewire.org)

---
#### Etape 1

Encore une fois, **data.txt** contient le mot de passe. Cette fois ci, le contenu est **encrypté en ROT13**, c'est à dire que l'alphabet est déplacé de 13 lettres.

On peut donc soit:
- Utiliser un site de décodage *(decipher)* comme dCode
- Utiliser `tr` *(translate)* et transposer les lettres de 13 places avec des arguments

Regardons le contenu de *data.txt*:
> Gur cnffjbeq vf 5Gr8L4qetPEsPk8htqjhRK8XSP6x2RHh

---
### Etape 2

`tr '[A-Za-z]' '[N-ZA-Mn-za-m]'` va prendre chaque lettre et la tourner de 13 positions, le A devient N et le b devient o.  
Plus simplement, l'alphabet n'ira pas de A à Z, mais de N à M.

Regardons donc le résultat de la commande:
```console
bandit11@bandit:~$ cat data.txt |tr '[A-Za-z]' '[N-ZA-Mn-za-m]'
The password is 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu
```

---
Mot de passe: **5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu**
