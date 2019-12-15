## Over-The-Wire -writeup-
### Bandit12 (bandit12@bandit.labs.overthewire.org)

---
#### Etape 1

Comme toujours, le mot de passe est dans **data.txt**. Mais là, on nous informe que le fichier est un *hexdump* compressé plusieurs fois.  
Regardons à quoi ressemble *data.txt*:

```console
bandit12@bandit:/tmp/visages$ cat data.txt | head
00000000: 1f8b 0808 d7d2 c55b 0203 6461 7461 322e  .......[..data2.
00000010: 6269 6e00 013c 02c3 fd42 5a68 3931 4159  bin..<...BZh91AY
00000020: 2653 591d aae5 9800 001b ffff de7f 7fff  &SY.............
00000030: bfb7 dfcf 9fff febf f5ad efbf bbdf 7fdb  ................
00000040: f2fd ffdf effa 7fff fbd7 bdff b001 398c  ..............9.
00000050: 1006 8000 0000 0d06 9900 0000 6834 000d  ............h4..
00000060: 01a1 a000 007a 8000 0d00 0006 9a00 d034  .....z.........4
00000070: 0d1a 3234 68d1 e536 a6d4 4000 341a 6200  ..24h..6..@.4.b.
00000080: 0069 a000 0000 0000 d003 d200 681a 0d00  .i..........h...
00000090: 0001 b51a 1a0c 201e a000 6d46 8068 069a  ...... ...mF.h..
```
On peut donc transformer data.txt en son format binaire d'origine avec `xxd -r`:

```console
bandit12@bandit:/tmp/visages$ xxd -r data.txt
�▒▒h��6��@4▒bi���h▒91AY&SY���������ϟ�����������������9��
    �mF�h�h44
▒��B��,0��   ��4@�����@2▒C@h�� �
�ɋ�^-K�����}�\,�▒ǿ�}E�F�_!r�U�g?E�i��9x��TB@�lȲ���BF.hM�SC4�V�F��R�Br"�<(Hت$    $���KBs��%l▒~�_�▒ݿ����g�zM�w�#P"2@������

��\��WQO4�p�i�����S�#&��/�#��[j▒�<D�uԐ^_�H.�-��wAt
                                                  �[��UP�G�CP��&:�2�*�)�\�������H�
```

Il faut également **sauvegarder** le format binaire d'origine dans un nouveau fichier: `xxd -r data.txt output.bin`

---
#### Etape 2

Il faut maintenant trouver la combinaison de -dé-compressions qui nous menera au fichier d'origine. Regardons le type de fichier qu'est *output.bin* avec `file`:

```console
bandit12@bandit:/tmp/visages$ file output.bin 
output.bin: gzip compressed data, was "data2.bin", last modified: Tue Oct 16 12:00:23 2018, max compression, from Unix
```

*output.bin* est donc compressé en **gzip**.
On va donc utiliser `zcat`, un 'companion' de **gzip**, qui renvoie le contenu décompressé en output, idéal pour le *piping*.

Avec cela on va également utiliser la commande `file -` qui renvoie le type du fichier en input du pipe. *(Apprendre la signification du tiret dans le piping)*

---
```console
bandit12@bandit:/tmp/visages$ zcat output.bin | file -
/dev/stdin: bzip2 compressed data, block size = 900k
```

Le fichier a été compressé en bzip2, **puis en gzip** *(on inverse l'ordre puisqu'on décompresse)*.  
On va donc utiliser `bzcat`, qui est exactement pareil que `zcat`, mais pour les compressions **bzip2**.

---
```console
bandit12@bandit:/tmp/visages$ zcat output.bin | bzcat | file -
/dev/stdin: gzip compressed data, was "data4.bin", last modified: Tue Oct 16 12:00:23 2018, max compression, from Unix
```

Encore compressé en **gzip**, on continue les pipes:
```console
bandit12@bandit:/tmp/visages$ zcat output.bin | bzcat | zcat |file -
/dev/stdin: POSIX tar archive (GNU)
```
Cette fois ci on tombe sur une archive **tar**. Et nous avons de la chance, on peut décompresser les fichiers **tar** avec des arguments qui renvoient l'output décompressé: **-x** et **-O**:

---
```console
bandit12@bandit:/tmp/visages$ zcat output.bin | bzcat | zcat | tar xO | file -
/dev/stdin: POSIX tar archive (GNU)
```

Encore une archive **tar**, on continue:

---
```console
bandit12@bandit:/tmp/visages$ zcat output.bin | bzcat | zcat | tar xO | tar xO | file -
/dev/stdin: bzip2 compressed data, block size = 900k
```

et encore:

---
```console
bandit12@bandit:/tmp/visages$ zcat output.bin | bzcat | zcat | tar xO | tar xO | bzcat | file -
/dev/stdin: POSIX tar archive (GNU)
```

et encore...:

---
```console
bandit12@bandit:/tmp/visages$ zcat output.bin | bzcat | zcat | tar xO | tar xO | bzcat | tar xO | file -
/dev/stdin: gzip compressed data, was "data9.bin", last modified: Tue Oct 16 12:00:23 2018, max compression, from Unix
```

et toujours:

---
```console
bandit12@bandit:/tmp/visages$ zcat output.bin | bzcat | zcat | tar xO | tar xO | bzcat | tar xO | zcat | file -
/dev/stdin: ASCII text
```

et enfin !  
Il suffit d'enlever `file -` de la commande pour avoir le résultat final de toute ces décompressions:

```console
bandit12@bandit:/tmp/visages$ zcat output.bin | bzcat | zcat | tar xO | tar xO | bzcat | tar xO | zcat
The password is 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL
```

---
Mot de passe: **8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL**


