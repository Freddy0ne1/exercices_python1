"""Exercice 06 - Calcul de la moyenne
Ce script contient une fonction pour calculer la moyenne d'une liste de nombres.
"""


# Fonction pour calculer la moyenne d'une liste de nombres
def calculate_average(list_numbers):
    """
    Calcule la moyenne des nombres dans une liste.

    Args:
        list_numbers (list of int or float): Liste contenant des nombres.

    Returns:
        float: La moyenne des nombres. Retourne 0 si la liste est vide.
    """

    # Si la liste est vide, on retourne 0 pour éviter une division par zéro
    if not list_numbers:
        return 0

    # On calcule la somme de tous les nombres de la liste
    total = sum(list_numbers)

    # On compte combien de nombres il y a dans la liste
    count = len(list_numbers)

    # On calcule la moyenne en divisant la somme par le nombre de valeurs
    return total / count


# 🧪 Exemple d'utilisation de la fonction

# On crée une liste de nombres
numbers = [10, 20, 30, 40, 50]

# On appelle la fonction pour calculer la moyenne
average = calculate_average(numbers)

# On affiche le résultat à l'utilisateur
print(f"La moyenne est : {average}")
