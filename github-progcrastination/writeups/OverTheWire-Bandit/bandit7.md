## Over-The-Wire -writeup-
### Bandit7 (bandit7@bandit.labs.overthewire.org)

---
#### Etape 1

Le mot de passe se trouve dans le fichier **data.txt**, à côté du mot **millionth**.  
Regardons déjà comment se compose le fichier *data.txt*:

```console
bandit7@bandit:~$ cat data.txt |head
humiliation's	47r0YuNylaQ3k6HqGF5NsPPiGuolDCjn
malarkey's	0huyJeRwvtJaoyRmJjQFsRnQcYG4gDir
prioress	ocudTlq9CbpCw9aByrqGffAuoYvCmLNV
enlivened	a7zT1gFekL2pB54py3NmJkYluxdAscwO
bony	r5GbTRzr0dsAMEuiBO8sznt0v56nci5z
transatlantic	ttoxcePeynPXWS1fnQTBWtij9uQwbBfJ
earliness	ikmPFX39MF1mrIfRvTMIFnBGyZV3T2Fa
rump's	nFY7k2ua3xfV5oScoBQsPhrwKjeKVwam
rink's	vzsUxoBeDiy7wo7SW1CnXZUYEOIUuoiw
sierras	fUB5nuau8pLD55Wi4u6R8x4SDxqBUXfd
```

---
#### Etape 2

Utilisons **grep** pour trouver le mot **millionth** et ce qui suit:
`grep "millionth.*"` va chercher le mot *millionth*, puis n'importe quel caractère après ça, dans la ligne.

```console
bandit7@bandit:~$ cat data.txt |grep "millionth.*"
millionth	cvX2JJa4CFALtqS87jk27qwqGhBM9plV
```

---
Mot de passe: **cvX2JJa4CFALtqS87jk27qwqGhBM9plV**
