"""
Exercice 11 : Gestion d'un compte bancaire

Ce script définit une classe BankAccount qui permet de gérer un compte bancaire :
- dépôt d'argent
- retrait d'argent
- affichage du solde

Des vérifications sont incluses pour s'assurer que les montants sont valides.
"""


class BankAccount:
    """
    Représente un compte bancaire avec un titulaire et un solde.
    """

    def __init__(self, account_holder, balance):
        """
        Initialise un nouveau compte bancaire.

        Args:
            account_holder (str): Nom du titulaire du compte.
            balance (float or int): Solde initial du compte.
        """
        self.account_holder = account_holder  # Nom du titulaire
        self.balance = balance  # Solde du compte

    def deposit(self, amount):
        """
        Dépose un montant sur le compte, si celui-ci est positif.

        Args:
            amount (float or int): Le montant à déposer.

        Returns:
            None
        """
        if amount > 0:
            self.balance += amount  # Ajoute le montant au solde
            print(f"{amount} € déposés avec succès.")
        else:
            print("❌ Le montant du dépôt doit être positif.")

    def withdraw(self, amount):
        """
        Retire un montant du compte si le solde est suffisant et que le montant est positif.

        Args:
            amount (float or int): Le montant à retirer.

        Returns:
            None
        """
        if amount <= 0:
            print("❌ Le montant du retrait doit être positif.")
        elif amount > self.balance:
            print("❌ Fonds insuffisants pour ce retrait.")
        else:
            self.balance -= amount  # Retire le montant du solde
            print(f"{amount} € retirés avec succès.")

    def display_balance(self):
        """
        Affiche le nom du titulaire et le solde actuel du compte.

        Returns:
            None
        """
        print("\n📄 Détails du compte bancaire\n")
        print(f"Titulaire du compte : {self.account_holder}")
        print(f"Solde actuel : {self.balance} €")


# 🧪 Partie test - Création d’un compte bancaire

# Création d’un compte au nom de Freddy avec un solde initial de 1000 €
account = BankAccount("Freddy", 1000)

# Affiche les informations de départ
account.display_balance()

# Dépôt de 500 €
account.deposit(500)

# Retrait de 300 €
account.withdraw(300)

# Tentative de retrait supérieur au solde
account.withdraw(1500)  # Doit afficher une erreur

# Tentative de dépôt avec un montant invalide
account.deposit(-50)  # Doit afficher une erreur

# Affichage final du solde
account.display_balance()
