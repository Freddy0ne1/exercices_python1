"""
Exercice 07 : Calcul du carré d'un nombre

Écrire une fonction square(n) qui prend un nombre en paramètre et retourne son carré.
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
    try:
        # Essaie de multiplier le nombre par lui-même
        return n * n
    except TypeError:
        # Si une erreur de type se produit (ex : "texte" * "texte"), on gère ici
        print("\nLe paramètre doit être un nombre !")
        return None


# 🧪 Exemples d'utilisation de la fonction

print(square(5))  # Affiche : 25
print(square(3.2))  # Affiche : 10.24
print(square("texte"))  # Affiche un message d'erreur et retourne None
