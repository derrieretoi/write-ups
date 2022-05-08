## Over-The-Wire -writeup-
### Leviathan0 (leviathan0@leviathan.labs.overthewire.org)
---
#### Etape 1

Le dossier `home` ne contient à première vue pas grand chose. L'accès au fichier `/etc/leviathan_webpass/leviathan1` nous est inaccessible.

Cependant, `ls -la` révèle un dossier `.backup` qui contient un **bookmarks.html** !

```console
leviathan0@leviathan:~/.backup$ cat bookmarks.html | head
<!DOCTYPE NETSCAPE-Bookmark-file-1>
<!-- This is an automatically generated file.
     It will be read and overwritten.
     DO NOT EDIT! -->
<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
<TITLE>Bookmarks</TITLE>
<H1 LAST_MODIFIED="1160271046">Bookmarks</H1>

<DL><p>
    <DT><H3 LAST_MODIFIED="1160249304" PERSONAL_TOOLBAR_FOLDER="true" ID="rdf:#$FvPhC3">Bookmarks Toolbar Folder</H3>
```

Ce sont donc des *marques-pages de navigateurs*, avec des liens et des descriptions.  
Le fichier compte de nombreux marques-pages, **trop nombreux pour les examiner un par un**.

---
#### Etape 2

Cherchons si un des marques pages contient le mot *leviathan*:

```console
leviathan0@leviathan:~/.backup$ grep leviathan bookmarks.html 
<DT><A HREF="http://leviathan.labs.overthewire.org/passwordus.html | This will be fixed later, the password for leviathan1 is rioGegei8m" ADD_DATE="1155384634" LAST_CHARSET="ISO-8859-1" ID="rdf:#$2wIU71">password to leviathan1</A>
```

Et bingo. Un lien qui qui nous donne le mot de passe pour *leviathan1*: rioGegei8m

---
Mot de passe: **rioGegei8m**

leviathan0.md | [leviathan1.md >>](leviathan1.md)
