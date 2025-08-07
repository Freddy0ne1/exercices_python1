"""# Exercice 02 : Notes des étudiants
# 📝 Cet exercice demande à l'utilisateur d'entrer le nom d'un étudiant
# et affiche ses notes ainsi que sa moyenne."""

# 📘 Dictionnaire contenant les notes de chaque étudiant par matière
students = {
    "Alice": {"Mathématiques": 90, "Français": 80, "Histoire": 95},
    "Bob": {"Mathématiques": 75, "Français": 85, "Histoire": 70},
    "Charlie": {"Mathématiques": 88, "Français": 92, "Histoire": 78},
}

# 🧾 Demande à l'utilisateur d'entrer le nom d'un étudiant
name = input("Entrez le nom de l'étudiant : ").capitalize()

# 🔍 Vérifie si l'étudiant existe dans le dictionnaire
if name in students:
    print(f"\nNotes de {name} :")

    # 📚 On parcourt chaque matière et note
    for subject, grade in students[name].items():
        print(f"- {subject} : {grade}")

    # 📊 Calcul de la moyenne
    grades = students[name].values()  # On récupère toutes les notes de l'étudiant
    total_grades = sum(grades)  # On fait la somme des notes
    total_subjects = len(grades)  # On compte combien il y a de matières

    average = (
        total_grades / total_subjects
    )  # On divise la somme par le nombre de matières

    print(
        f"\nMoyenne de {name} : {average:.2f}\n"
    )  # Affiche la moyenne avec 2 décimales

else:
    # ❌ Si l'étudiant n'existe pas, on affiche un message d'erreur
    print(f"\nAucun étudiant trouvé avec le nom {name}.\n")
