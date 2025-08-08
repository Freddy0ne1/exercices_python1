"""# Exercice 03 : Compter les voyelles dans des mots
# 📝 Cet exercice demande à l'utilisateur de compter le nombre de voyelles dans une liste de mots.
"""

# 📝 Liste de mots à analyser
words = ["python", "programmation", "langage", "ordinateur", "apprentissage"]

# 🟡 Liste des voyelles à rechercher
VOYELLES = "aeiouy"

# 📊 Liste vide pour stocker les résultats sous forme de tuples (mot, nombre de voyelles)
results = []

# 🔄 Parcours de chaque mot de la liste
for word in words:
    # 🔢 Initialisation du compteur de voyelles
    COUNTER = sum(
        1 for letter in word if letter.upper() in "AEIOU"
    )  # Utilisation de la compréhension de liste pour compter les voyelles

    # ➕ Ajoute le mot et son nombre de voyelles dans la liste
    results.append((word, COUNTER))

# 📢 Affichage explicite pour l’utilisateur (facultatif)
print("Nombre de voyelles trouvées dans chaque mot :")
for word, nb in results:
    print(f"- {word} : {nb} voyelle(s)")

print("\nRésultat final")
print(results)
