## Over-The-Wire -writeup-
### Natas3 (http://natas3.natas.labs.overthewire.org/)

#### Etape 1

"Il n'y a rien sur cette page" encore. On inspecte le code source (Ctrl+U):

```html
<html>
<head>
<!-- This stuff in the header has nothing to do with the level -->
<link rel="stylesheet" type="text/css" href="http://natas.labs.overthewire.org/css/level.css">
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/jquery-ui.css" />
<link rel="stylesheet" href="http://natas.labs.overthewire.org/css/wechall.css" />
<script src="http://natas.labs.overthewire.org/js/jquery-1.9.1.js"></script>
<script src="http://natas.labs.overthewire.org/js/jquery-ui.js"></script>
<script src=http://natas.labs.overthewire.org/js/wechall-data.js></script><script src="http://natas.labs.overthewire.org/js/wechall.js"></script>
<script>var wechallinfo = { "level": "natas3", "pass": "sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14" };</script></head>
<body>
<h1>natas3</h1>
<div id="content">
There is nothing on this page
<!-- No more information leaks!! Not even Google will find it this time... -->
</div>
</body></html>
```

On trouve ce commentaire :
*<!-- No more information leaks!! Not even Google will find it this time... -->*
*//Plus de fuites d'informations ! Même Google ne le trouvera pas cette fois ci...*

Indice : Indexation Google > robots.txt

#### Etape 2

On regarde le robots.txt du site:
http://natas3.natas.labs.overthewire.org/robots.txt

On obtient:
> User-agent: *  
> Disallow: /s3cr3t/

Encore un indice > On doit se rendre dans le dossier /s3cr3t/

#### Etape 3

Allons dans le dossier:
natas3.natas.labs.overthewire.org/s3cr3t/

Bingo ! **users.txt** est ici ! On obtient les identifiants:
> natas4:Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ

Mot de passe: **Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ**
