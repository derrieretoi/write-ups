## Over-The-Wire -writeup-
### Natas3 (http://natas3.natas.labs.overthewire.org/)

---
#### Etape 1

"Accès refusé, vous visitez le site depuis "..", et les utilisateurs authorisés doivent venir depuis "http://natas5.natas.labs.overthewire.org/"
On va donc **changer notre referer**, une en-tête de requette HTTP qui informe les sites de la provenance des utilisateurs (d'où ils viennent, de quel lien), par le lien demandé:

