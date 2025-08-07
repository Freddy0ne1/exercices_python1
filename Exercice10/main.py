"""
Exercice 10 : Héritage en Python

Dans cet exercice, nous créons une classe de base `Person` et une classe dérivée `Employee`.
La classe `Employee` hérite de `Person` et ajoute un attribut pour le salaire.
Chaque classe possède une méthode pour afficher ses propres informations.
"""


class Person:
    """
    Représente une personne avec un nom et un âge.
    """

    def __init__(self, name, age):
        """
        Initialise une nouvelle personne avec un nom et un âge.

        Args:
            name (str): Le nom de la personne.
            age (int): L'âge de la personne.
        """
        self.name = name  # Attribut pour stocker le nom
        self.age = age  # Attribut pour stocker l'âge

    def display_details(self):
        """
        Affiche les détails de la personne (nom et âge).
        """
        print(f"Nom : {self.name}")
        print(f"Âge : {self.age} ans")


class Employee(Person):
    """
    Représente un employé, hérite de la classe Person et ajoute un salaire.
    """

    def __init__(self, name, age, salary):
        """
        Initialise un nouvel employé avec un nom, un âge et un salaire.

        Args:
            name (str): Le nom de l'employé.
            age (int): L'âge de l'employé.
            salary (float or int): Le salaire de l'employé.
        """
        super().__init__(name, age)  # Appelle le constructeur de la classe mère
        self.salary = salary  # Attribut supplémentaire pour le salaire

    def display_details(self):
        """
        Affiche les détails de l'employé (nom, âge, salaire).
        """
        super().display_details()  # Affiche nom et âge depuis Person
        print(f"Salaire : {self.salary} €")  # Affiche le salaire


# 🧪 Partie test

# Création d'une instance de la classe Person
person = Person("Alice", 30)
print("Détails de la personne :")
person.display_details()

print("\nDétails de l'employé :")

# Création d'une instance de la classe Employee
employee = Employee("Bob", 40, 3500)
employee.display_details()
