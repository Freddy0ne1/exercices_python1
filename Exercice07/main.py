"""Exercice 07 : Calcul du carré d'un nombre

Écrire une fonction `square(n)` qui prend un nombre en paramètre et retourne son carré.
Si le paramètre n'est pas un nombre, la fonction doit afficher
un message d'erreur et retourner None.
"""


def square(n):
    """
    Calcule le carré d'un nombre.

    Args:
        n (int ou float): Un nombre entier ou décimal à mettre au carré.

    Returns:
        int ou float ou None: Le carré du nombre n si c'est un nombre valide,
        sinon None si le paramètre n'est pas un nombre.
    """

    # Vérifie si n est bien un nombre (int ou float)
    if not isinstance(n, (int, float)):
        print(
            "\nLe paramètre doit être un nombre !"
        )  # Message d'erreur pour l'utilisateur
        return None  # Retourne None si n n'est pas un nombre

    # Retourne le carré du nombre
    return n * n


# 🧪 Exemples d'utilisation de la fonction

# Test avec un entier
print(square(5))  # Affiche : 25

# Test avec un nombre à virgule
print(square(3.2))  # Affiche : 10.24

# Test avec une chaîne de caractères (cas invalide)
print(square("texte"))  # Affiche un message d'erreur et retourne None
