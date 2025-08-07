"""
Exercice 09 : Création d'une classe Rectangle

Ce script définit une classe Rectangle capable de calculer
l'aire et le périmètre d'un rectangle à partir de sa largeur et sa longueur.
"""


class Rectangle:
    """
    Représente un rectangle avec une largeur et une longueur.
    """

    def __init__(self, width, length):
        """
        Initialise un nouveau rectangle avec la largeur et la longueur données.

        Args:
            width (float or int): La largeur du rectangle.
            length (float or int): La longueur du rectangle.
        """
        # Stocke la largeur du rectangle
        self.width = width
        # Stocke la longueur du rectangle
        self.length = length

    def calculate_area(self):
        """
        Calcule et retourne l'aire du rectangle.

        Returns:
            float or int: L'aire du rectangle (width * length).
        """
        return self.width * self.length  # Formule : Aire = largeur × longueur

    def calculate_perimeter(self):
        """
        Calcule et retourne le périmètre du rectangle.

        Returns:
            float or int: Le périmètre du rectangle (2 * (width + length)).
        """
        return 2 * (
            self.width + self.length
        )  # Formule : Périmètre = 2 × (largeur + longueur)


# 🧪 Partie test de la classe Rectangle

# Création d'une instance de rectangle avec une largeur de 5 et une longueur de 3
rectangle = Rectangle(5, 3)

# Affichage de la largeur du rectangle
print("Largeur :", rectangle.width)

# Affichage de la longueur du rectangle
print("Longueur :", rectangle.length)

# Appel de la méthode pour calculer l'aire, puis affichage du résultat
print("Aire :", rectangle.calculate_area())  # Doit afficher 15

# Appel de la méthode pour calculer le périmètre, puis affichage du résultat
print("Périmètre :", rectangle.calculate_perimeter())  # Doit afficher 16
