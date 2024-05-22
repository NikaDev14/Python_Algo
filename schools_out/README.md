# Analyse du contexte:

- Optimisation au maximum l'allocation des salles de classe
- Avoir en argument le chemin d'un fichier contenant les données à traiter au format JSON.
- Ouvrez le fichier, puis récupérez les données.
- Convertir le format json en une liste
- Déterminer le nombre minimal de salles nécessaires à la planification du jour.
- Dans une salle, on ne peut pas avoir deux emplois du temps à la fois.
- Un cours se terminant à 9h00 et un cours commençant à 10h00 peuvent s'enchaîner dans la même salle.


# Un résumé de votre approche:

- Une fonction recevra un argument une liste des objets (une liste de planings) et afficher un nombre minimal de salles.
  - Intialisation un conteur à 0 pour compter le nombre de salles.
  - Utiliser la methode de Glonton pour pour faciliter à resoudre notre prbléme.
  - trier la liste par valeurs croissantes d'heures de dèbut. (au pire de cas le temps d'exécution est de : T1(n))
  - Puis trier la liste par valeurs croissantes d'heures de fin. (au pire de cas le temps d'exécution est de : T2(n))
  - Intialisation un champ planing à 0 pour identifier par le premier planing de la liste.
  - Parcourir la liste de gauche a droite a partir de deuxième element et verifions: (au pire de cas le temps d'exécution est de : T3(n))
    - si heures_de_fin_planing >= heures_de_debut_planing donc ajouter le champ planing + = 1
    - sinon ajouter le conteur + = 1:
  -convertir le resultat en format json

# Exemple:
![Capture_d_écran_2022-09-26_à_17.51.06](/uploads/101ab330005b44405f68e3c7499336d6/Capture_d_écran_2022-09-26_à_17.51.06.png)

# complexité est de: T1(n) + T2(n) + T3(n) = n + n + n = O(n)
