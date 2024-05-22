# **Analyse du contexte:**

- Tous les bâtiments d'une rue orientée sur l'axe Ouest-Est et le soleil levant de l'Est.
- convertir le format json en une liste 
- Les différents bâtiments sont représentés par une liste d'objets représentant les différents bâtiments de la rue, d'Ouest en Est.
- Un bâtiment peut en cacher un autre
- Augmentation de 5% de la location d'appartements en face du lever du soleil.
- Pour chaque appartement faisant face au soleil levant, le nouveau loyer mensuel sera arrondi à l'euro supérieur après augmentation de 5%.
- calculer la bénéfice de l'année à venir


# **Un résumé de votre approche:**

- Une fonction qui prend en paramètre un bâtiment (une liste d'objets) et un nombre d'augmentation (pourcentage). retourne les nouveaux loyes   mensuel arrondi à l'euro supérieur de chaque appartement orienté à l'Est 
    - Parcourir la liste des objets de gauche à droite et vérifier pour chaque appartement a une orientation vers l'est.
    - Une fonction recevra un argument de tous les bâtiments (une liste d'objets), et cacul le bénéfice total de tous les bâtiments. (temps d'exécution dans le pire de cas est T1(n)))
    - Calculez bénéfice du premier immeuble à l'Est, et conservez la hauteur comme hauteur maximale.
    - Parcourez la liste bâtiments de droite à de gauche c'est-à-dire de l'Est à l'Ouest. Vérifiez chaque immeuble si sa hauteur est plus grand que la hauteur maximale, calculez le benefice de l'immeuble mutipler par sa hauteur moins hauteur maximale et hauteur maximale égale la hauteur du bâtiments. (temps d'exécution dans le pire de cas est T2(n))



# **Exemple:**

![s_0](/uploads/8c6db2e5a33adaa1f2e7bcfef5b4d419/s_0.jpg)

# complexité est de: T1(n) * T2(n) = n * n = O(n2)
