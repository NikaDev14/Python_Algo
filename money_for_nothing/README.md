# Analyse du contexte:

- Stratégie d'achat et de vente d'une bourse de produit
- convertir le format json en une liste
- Les différents prix des produits sont représentés par une liste des entiers.
- Acheter un produit forcément le vendre
- Vendre un produit forcément s'il y a un achat

# Un résumé de votre approche:

- Une fonction recevra un argument une liste des prix des produites (une liste des entiers)et retourne une liste des entiers (index de achat suivi l'index de vente ...).
  - Crée une liste de nombres entiers vides pour stocker tous les index d'achats et de ventes.
  - Ajouter un boolean pour l'achat et la vente. Pour eviter de faire un achat suivi d'un achat.
  - Vérification si le premier element à gauche de la liste est plus petit que son voisin de droite.
  - Parcourez la liste des entiers de gauche à droite à partir du deuxième element.
  - Pour faire un achat, vérifiez chaque element que :
    - voisin_gauche >= element < voisin_droite
  - Pour faire un vente, Vérifiez chaque element que :
    - voisin_gauche <= element > voisin_droite
  - convertir les resultat en format json

# Exemple:

![money](/uploads/deac4eb1fdcf926320b31eb1e3d54a94/money.jpg)

# complexité est de: O(n)
