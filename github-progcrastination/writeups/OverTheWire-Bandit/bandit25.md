## Over-The-Wire -writeup-
### Bandit25 (bandit25@bandit.labs.overthewire.org)
###### Aidé pour celui-ci
---
#### Etape 1

On a a disposition un fichier **bandit26.sshkey** avec lequel on doit se connecter en tant que **bandit26**.  
Cependant, **bandit26 n'utilise pas /bin/shell** ! Il va falloir connaître le shell, savoir comment il fonctionne, et savoir s'en échapper.

Tout d'abord, **bandit26.sshkey** contient une *clé SSH privée*.  
Si on essaie de se connecter directement avec cette clé (et l'option **-i**):

```console
bandit25@bandit:~$ ssh -i bandit26.sshkey bandit26@localhost
Could not create directory '/home/bandit25/.ssh'.
The authenticity of host 'localhost (127.0.0.1)' can't be established.
ECDSA key fingerprint is SHA256:98UL0ZWr85496EtCRkKlo20X3OPnyPSB5tB5RPbhczc.
Are you sure you want to continue connecting (yes/no)? 
```
Puis...
```console
  _                     _ _ _   ___   __  
 | |                   | (_) | |__ \ / /  
 | |__   __ _ _ __   __| |_| |_   ) / /_  
 | '_ \ / _` | '_ \ / _` | | __| / / '_ \ 
 | |_) | (_| | | | | (_| | | |_ / /| (_) |
 |_.__/ \__,_|_| |_|\__,_|_|\__|____\___/ 
Connection to localhost closed.
```

Nous sommes déconnectés à chaque ouverture de session. Il va falloir regarder le shell utilisé par **bandit26** de plus près.

---
#### Etape 2

Pour regarder ceci, on va afficher le contenu de `/etc/passwd` et examiner la ligne de **bandit26** avec `grep`:

```console
bandit25@bandit:~$ grep bandit26 /etc/passwd
bandit26:x:11026:11026:bandit level 26:/home/bandit26:/usr/bin/showtext
```

**bandit26** utilise donc `/usr/bin/showtext`... qui n'est pas un shell...

---
#### Etape 3

Jetons un oeil à ce `showtext`:

```
bandit25@bandit:~$ cat /usr/bin/showtext 
#!/bin/sh

export TERM=linux

more ~/text.txt
exit 0
```

Il semblerait que `showtext` soit un script qui affiche un ~/text.txt, puis `exit 0` fermant le terminal aussitôt.  
On a donc bien trouvé ce qui nous posait problème. Notre but maintenant, c'est de pouvoir s'interposer entre le début du script, et la fin, pour pouvoir exécuter du code avec ssh dans la session de **bandit26**, avant qu'elle ne se ferme.

Et une propriété intéressante de `more`, et que le code suivant ne s'exécute pas tant que la "visualisation" de more est active.

En d'autres termes, **redimensionner notre fenêtre de terminal nous permettrait d'entrer en mode *more*, et ainsi de pouvoir exécuter des commandes**.

---
#### Etape 4

Reconnectons-nous avec une petite fenêtre:

```console
  _                     _ _ _   ___   __  
 | |                   | (_) | |__ \ / /  
 | |__   __ _ _ __   __| |_| |_   ) / /_  
 | '_ \ / _` | '_ \ / _` | | __| / / '_ \ 
--More--(66%)
```

Pendant que nous sommes dans le rendu de *more*, on appuie sur **v**, pour lancer l'éditeur de texte *(vi par défault)*.  

```console
  _                     _ _ _   ___   __
 | |                   | (_) | |__ \ / /
 | |__   __ _ _ __   __| |_| |_   ) / /_
 | '_ \ / _` | '_ \ / _` | | __| / / '_ \
"~/text.txt" [readonly] 6L, 258C
```

On peut voir qu'on est bien dans ~/text.txt  
Maintenant il ne nous reste plus qu'à aller modifier le fichier `/etc/bandit_pass/bandit26`, avec la commande **:e** pour ouvrir un fichier:

```console
  _                     _ _ _   ___   __
 | |                   | (_) | |__ \ / /
 | |__   __ _ _ __   __| |_| |_   ) / /_
 | '_ \ / _` | '_ \ / _` | | __| / / '_ \
:e /etc/bandit_pass/bandit26
```

Et bingo

```console
5czgV9L3Xx8JPOyRbXh6lQbmIOWvPT6Z
~                                                                                                                                                    
~                                                                                                                                                    
~                                                                                                                                                    
"/etc/bandit_pass/bandit26" [readonly] 1L, 33C 
```

Le challenge est génie, c'est dommage de pas l'avoir trouvé seul.

---
Mot de passe: **5czgV9L3Xx8JPOyRbXh6lQbmIOWvPT6Z**
