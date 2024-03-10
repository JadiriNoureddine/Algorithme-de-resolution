# Algorithme-de-resolution

Ce projet présente un programme Python capable de déterminer automatiquement la validité d'expressions logiques en s'appuyant sur la logique propositionnelle.
Le programme exploite la bibliothèque sympy pour simplifier les expressions sous forme normale conjonctive (CNF). Il utilise ensuite la méthode de résolution par résolvants pour établir la validité d'une formule logique donnée.


* Début 
* Ecrire la négation de F ;
* Mettre F sous forme d'un ensemble de clauses ;
* Tant que la clause vide n'est pas rencontrée et qu'il 
  existe des paires réductibles faire
* Début
* Chercher des clauses résolvantes ;
* Ajouter ce résultat à la liste des clauses ;
* Fintantque ;
* Si on trouve la clause vide alors F est valide
* sinon F est invalide
* Finsi ;
* Fin ;
