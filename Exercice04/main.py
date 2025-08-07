"""Exercice 04 - Classes et méthodes (version débutant)
# 📝 Cet exercice présente deux classes : MyClass pour un nom complet
# et OtherClass pour un prénom et un nom séparés."""

# Exercice 04 - Classes et méthodes (version débutant)


# 🎓 Classe pour afficher un nom complet (prénom + nom ensemble)
class MyClass:
    """Classe représentant une personne avec un nom complet."""

    def __init__(self, full_name):
        # Attribut pour stocker le nom complet
        self.full_name = full_name

    def display_name(self):
        """Affiche le nom complet."""
        print("Le nom complet est :", self.full_name)


# ➕ Classe séparée pour gérer prénom et nom individuellement
class OtherClass:
    """Classe représentant une personne avec un prénom et un nom."""

    def __init__(self, first_name, last_name):
        # Attributs pour stocker le prénom et le nom séparément
        self.first_name = first_name
        self.last_name = last_name

    def display_name(self):
        """Affiche le prénom suivi du nom."""
        print("Nom complet :", self.first_name, self.last_name)


# 🧪 Partie test pour voir comment les classes fonctionnent

# Exemple 1 : Utilisation de la classe MyClass
print("\nExemple avec MyClass - Nom complet")
person1 = MyClass("Alice Dupont")
person1.display_name()

# Ligne vide pour séparer les sorties
print()

# Exemple 2 : Utilisation de la classe OtherClass
print("Exemple avec OtherClass - Prénom et nom séparés")
identity1 = OtherClass("Alice", "Dupont")
identity1.display_name()
# Ligne vide pour séparer les sorties
print()
