"""
Exercice 08 - Décorateurs

Dans cet exercice, nous allons créer un décorateur qui affiche un message
avant et après l'exécution d'une fonction qui ne prend pas d'arguments.
Ce décorateur sera appliqué à une fonction de test.
"""


def log_decorator(func):
    """
    Décorateur qui affiche un message avant et après
    l'exécution d'une fonction sans argument.

    Args:
        func (function): La fonction cible à exécuter.

    Returns:
        function: Une nouvelle fonction qui ajoute des messages
        autour de l'exécution de la fonction d'origine.
    """

    def wrapper():
        """Fonction interne qui exécute la fonction cible
        et affiche des messages avant et après son exécution.
        """
        # Message avant l'exécution de la fonction
        print("🔹 Début de l'exécution de la fonction...")

        # Appel de la fonction originale
        result = func()

        # Message après l'exécution de la fonction
        print("✅ Fin de l'exécution de la fonction.")

        # Retour du résultat éventuel
        return result

    return wrapper


# 🎯 Fonction de test à décorer
@log_decorator
def function_test():
    """
    Fonction de test qui ne prend pas d'arguments
    et affiche simplement un message.
    """
    print("Cette fonction ne prend pas d'arguments.")


# ▶️ Appel de la fonction décorée
function_test()
