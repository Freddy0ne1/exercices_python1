"""
Exercice : Gestion d'une bibliothèque

Ce script permet de gérer une bibliothèque avec des fonctionnalités pour :
- Ajouter, supprimer, emprunter et rendre des livres
- Afficher les livres disponibles et empruntés
"""


class Book:
    """
    Représente un livre avec un titre, un auteur et une année de publication.
    """

    def __init__(self, title, author, year):
        """
        Initialise un nouveau livre.

        Args:
            title (str): Titre du livre.
            author (str): Nom de l'auteur.
            year (int): Année de publication.
        """
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        """
        Retourne une représentation lisible du livre.

        Returns:
            str: Format "Titre (Auteur, Année)"
        """
        return f"{self.title} ({self.author}, {self.year})"


class Library:
    """
    Classe représentant une bibliothèque avec des livres disponibles et empruntés.
    """

    def __init__(self):
        """
        Initialise une bibliothèque vide.
        """
        self.books = []  # Liste des livres disponibles
        self.borrow_books = []  # Liste des livres empruntés

    def add_book(self, book):
        """
        Ajoute un livre à la bibliothèque.

        Args:
            book (Book): Le livre à ajouter.
        """
        self.books.append(book)
        print(f"📗 Livre ajouté : {book.title}")

    def remove_book(self, book_title):
        """
        Supprime un livre de la bibliothèque.

        Args:
            book_title (str): Le titre du livre à supprimer.
        """
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                print(f"❌ Livre supprimé : {book.title}")
                return
        print("Livre non trouvé dans les livres disponibles.")

    def borrow_book(self, book_title):
        """
        Permet d'emprunter un livre par son titre.

        Args:
            book_title (str): Le titre du livre à emprunter.
        """
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                self.borrow_books.append(book)
                print(f"📕 Livre emprunté : {book.title}")
                return
        print("Livre non disponible ou déjà emprunté.")

    def return_book(self, book_title):
        """
        Permet de rendre un livre par son titre.

        Args:
            book_title (str): Le titre du livre à rendre.
        """
        for book in self.borrow_books:
            if book.title == book_title:
                self.borrow_books.remove(book)
                self.books.append(book)
                print(f"📘 Livre rendu : {book.title}")
                return
        print("Ce livre n'a pas été emprunté.")

    def available_books(self):
        """
        Retourne la liste des titres disponibles.

        Returns:
            list of str: Titres des livres disponibles.
        """
        return [book.title for book in self.books]

    def borrowed_books(self):
        """
        Retourne la liste des titres empruntés.

        Returns:
            list of str: Titres des livres empruntés.
        """
        return [book.title for book in self.borrow_books]


# 🧪 --- Partie test ---

# Création de livres
book1 = Book("L'Étranger", "Albert Camus", 1942)
book2 = Book("Harry Potter à l'école des sorciers", "J.K. Rowling", 1997)
book3 = Book("Madame Bovary", "Gustave Flaubert", 1857)

# Création de la bibliothèque
library = Library()

# Ajout des livres à la bibliothèque
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Emprunter un livre existant
library.borrow_book("L'Étranger")

# Affichage des livres disponibles
print("📚 Livres disponibles :", library.available_books())

# Affichage des livres empruntés
print("📕 Livres empruntés :", library.borrowed_books())

# Rendre un livre emprunté
library.return_book("L'Étranger")

# Affichage mis à jour
print("📚 Livres disponibles après retour :", library.available_books())
print("📕 Livres empruntés après retour :", library.borrowed_books())
