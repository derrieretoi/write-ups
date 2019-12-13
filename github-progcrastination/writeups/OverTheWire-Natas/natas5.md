## Over-The-Wire -writeup-
### Natas5 (http://natas5.natas.labs.overthewire.org/)

---
#### Etape 1

"Accès non-autorisé. Vous n'êtes pas connecté".  
Le code source ne contient aucune information.  
On doit vérifier les cookies:  

On ouvre les *outils de développement* (Ctrl+Shift+I) et on se rend dans l'onglet *Stockage*:
> **Cookies** -> loggedIn = 0

Il suffit donc de changer la valeur à 1, et de recharger la page.  
Un autre texte s'affiche:  
> Access granted. The password for natas6 is aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1

---
Mot de passe : **aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1**
