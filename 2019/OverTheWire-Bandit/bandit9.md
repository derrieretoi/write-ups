## Over-The-Wire -writeup-
### Bandit9 (bandit9@bandit.labs.overthewire.org)

---
#### Etape 1

Le mot de passe est *encore* dans **data.txt**, mais cette fois ci, on nous indique qu'il est:
- lisible par un humain
- précédé par plusieurs '='

Un simple aperçu du début du fichier nous montre qu'il va falloir exclure les caractères spéciaux:
> ʿ�|g�{Li&��G�[�W�K��z ...

---
Je vais utiliser `strings` qui va renvoyer:
```console
bandit9@bandit:~$ strings data.txt |head
.MBB
`B6ha
nK)U2u
&y@@2
5Lo%
ru@n
D}U'
e#s.
!:/%p
*'dZ
```

---
#### Etape 2

Il nous reste qu'à trouver les lignes qui contiennent plusieurs '='. On va *pipe* `strings` avec `grep '=='`:

```console
bandit9@bandit:~$ strings data.txt |grep '=='
2========== the
========== password
========== isa
========== truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk
```

---
Mot de passe: **truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk**

[<< bandit8.md](bandit8.md) | bandit9.md | [bandit10.md >>](bandit10.md)
