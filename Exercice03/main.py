"""# Exercice 03 : Compter les voyelles dans des mots
# 📝 Cet exercice demande à l'utilisateur de compter le nombre de voyelles dans une liste de mots.
"""

# 📝 Liste de mots à analyser
mots = ["python", "programmation", "langage", "ordinateur", "apprentissage"]

# 🟡 Liste des voyelles à rechercher
VOYELLES = "aeiouy"

# 📊 Liste vide pour stocker les résultats sous forme de tuples (mot, nombre de voyelles)
resultats = []

# 🔄 Parcours de chaque mot de la liste
for mot in mots:
    COMPTEUR = 0  # Initialisation du compteur de voyelles à 0

    # 🔁 Parcours de chaque lettre du mot
    for lettre in mot:
        if lettre in VOYELLES:
            COMPTEUR += 1  # Incrémente si la lettre est une voyelle

    # ➕ Ajoute le mot et son nombre de voyelles dans la liste
    resultats.append((mot, COMPTEUR))

# 📢 Affichage explicite pour l’utilisateur (facultatif)
print("Nombre de voyelles trouvées dans chaque mot :")
for mot, nb in resultats:
    print(f"- {mot} : {nb} voyelle(s)")

print("/nRésultat final")
print(resultats)

# Façon élég.
# sum(1 for letter in word if letter.upper() in 'AEIOU')
