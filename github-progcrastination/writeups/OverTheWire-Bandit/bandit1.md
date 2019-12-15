## Over-The-Wire -writeup-
### Bandit1 (bandit1@bandit.labs.overthewire.org)

---
#### Etape 1

Le mot de passe se trouve dans le fichier nommé `-`, mais `cat` reconnais le tiret comme un *argument*.  
Il faut donc appeler le fichier par son chemin *absolu ou relatif*:

- Comme par exemple `cat ./-`
- Ou bien`cat ~/-` *(puisque nous nous trouvons dans le répertoire home/bandit1)*

`cat ~/.` nous renvoie:
> CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9

---
Mot de passe: **CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9**
