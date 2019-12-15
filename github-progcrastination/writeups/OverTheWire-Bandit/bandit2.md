## Over-The-Wire -writeup-
### Bandit2 (bandit2@bandit.labs.overthewire.org)

---
#### Etape 1

Le mot de passe se trouve dans le fichier `spaces in this filename` ce qui pose évidemment problème pour notre `cat`.

La solution va être d'*échapper* les caractères problématiques pour que `cat` reconnaisse le nom du fichier *comme un vrai nom*:

- Une solution serait de laisser faire automatiquement le shell en écrivant `~/spaces`, puis en appuyant sur tabulation, qui va compléter le nom pour nous.  
*Cependant si le nom de plusieurs fichiers commençaient tous avec `spaces in fi...` alors notre technique ne marcherait pas.*

- Pour proprement *échapper* le caractère *'espace'* il faut rajouter des *backslashs* après chaque mot: `spaces\ in\ this\ filename`

`cat spaces\ in\ this\ filename` nous renvoie donc:
> UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK

---
Mot de passe: **UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK**
