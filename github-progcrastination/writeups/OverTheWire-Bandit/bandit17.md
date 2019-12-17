## Over-The-Wire -writeup-
### Bandit17 (bandit17@bandit.labs.overthewire.org)

---
#### Etape 1

**passwords.old** et **passwords.new** sont deux fichiers à comparer pour trouver le mot de passe. Le fichier *.new* contient le mot de passe que nous cherchons.

On utilise `diff` avec l'option **-u** qui nous donne les lignes enlevées et rajoutées, avec un peu plus de précisions:

 ```console
 bandit17@bandit:~$ diff -u passwords.old passwords.new
--- passwords.old	2018-10-16 14:00:27.742867000 +0200
+++ passwords.new	2018-10-16 14:00:27.762867000 +0200
@@ -39,7 +39,7 @@
 gZ5U640FLMMChheWKHNdaQ1lKzLuqjxZ
 Al0xVJb5bEzhnFG8nPFe6IJa2FjXVSzo
 CT2ZJy6MoLkTqdHuhL5zUIsW41WCntAA
-hlbSBPAWJmL6WFDb06gpTx1pPButblOA
+kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd
 46lUvvv0JJzyY0IOhWgGp5IjfsllmvaC
 FcSd4Me936rwbk2pAU9ylx9NXTrzdCaX
 vfU4mCzATtqUMNLg3a7mPs3OY6Dr4jaZ
 ```
 
 On peut y voir que la ligne précédée par `-` a été enlevée, et la lignes précédée par `+` a été rajoutée. *(A noter: on projète les modifications de *old* sur *new*. Inverser l'ordre des fichiers inverserait les signes !)*  
 En conclusion, la ligne a été changée en **kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd** dans le fichiers *passwords.new*
 
 ---
 Mot de passe: **kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd**
