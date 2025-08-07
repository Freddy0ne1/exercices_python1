"""
Ce fichier fait partie du projet Exercice05.
Il contient des fonctions arithmétiques de base.
"""


# ➕ Fonction pour additionner deux nombres
def addition(a, b):
    """
    Additionne deux nombres.

    Args:
        a (float ou int): Le premier nombre.
        b (float ou int): Le deuxième nombre.

    Returns:
        float ou int: La somme de a et b.
    """
    return a + b


# ➖ Fonction pour soustraire deux nombres
def soustraction(a, b):
    """
    Soustrait le deuxième nombre du premier.

    Args:
        a (float ou int): Le premier nombre.
        b (float ou int): Le nombre à soustraire à a.

    Returns:
        float ou int: La différence entre a et b.
    """
    return a - b


# 🧪 Partie test pour utiliser les fonctions
# On définit deux nombres
NUMBER1 = 10
NUMBER2 = 4

# On utilise la fonction addition
RESULT_ADD = addition(NUMBER1, NUMBER2)
print(f"\nRésultat de l'addition : {RESULT_ADD}")  # Affiche : 14

# On utilise la fonction soustraction
RESULT_SUB = soustraction(NUMBER1, NUMBER2)
print(f"Résultat de la soustraction : {RESULT_SUB}\n")  # Affiche : 6
