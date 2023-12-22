def ajouter_eleve(eleves, nom_eleve):
    """
    Ajoute un nouvel élève.

    Entrée:
    - eleves (dict): Un dictionnaire contenant les élèves et leurs notes.
    - nom_eleve (str): Le nom de l'élève à ajouter.

    Sortie:
    - str: Chaîne de confirmation.
    """
    if nom_eleve in eleves:
        return f"L'élève {nom_eleve} existe déjà."
    eleves[nom_eleve] = []
    return f"Élève {nom_eleve} ajouté avec succès."


def lister_eleves(eleves):
    """
    Liste les élèves.

    Entrée:
    - eleves (dict): Un dictionnaire contenant les élèves et leurs notes.

    Sortie:
    - str: Chaîne à afficher.
    """
    if not eleves:
        return "Aucun élève enregistré."
    return "\n".join([f"{i}. {eleve}" for i, eleve in enumerate(eleves, start=1)])


def supprimer_eleve(eleves, nom_eleve):
    """
    Supprime un élève.

    Entrée:
    - eleves (dict): Un dictionnaire contenant les élèves et leurs notes.
    - nom_eleve (str): Le nom de l'élève à supprimer.

    Sortie:
    - str: Chaîne de confirmation.
    """
    if nom_eleve in eleves:
        del eleves[nom_eleve]
        return f"Élève {nom_eleve} supprimé avec succès."
    return f"L'élève {nom_eleve} n'existe pas."


def ajouter_note_eleve(eleves, nom_eleve, matiere, valeur, coefficient):
    """
    Ajoute une note pour un élève.

    Entrée:
    - eleves (dict): Un dictionnaire contenant les élèves et leurs notes.
    - nom_eleve (str): Le nom de l'élève.
    - matiere (str): Le nom de la matière.
    - valeur (float): La valeur de la note.
    - coefficient (float): Le coefficient de la matière.

    Sortie:
    - str: Chaîne de confirmation.
    """
    if nom_eleve in eleves:
        ajouter_note(eleves[nom_eleve], matiere, valeur, coefficient)
        return f"Note ajoutée pour l'élève {nom_eleve} en {matiere} avec une valeur de {valeur} et un coefficient de {coefficient}."
    return f"L'élève {nom_eleve} n'existe pas."


def consulter_moyenne_eleve(eleves, nom_eleve, d_matieres):
    """
    Calcule et affiche la moyenne d'un élève.

    Entrée:
    - eleves (dict): Un dictionnaire contenant les élèves et leurs notes.
    - nom_eleve (str): Le nom de l'élève.
    - d_matieres (dict): Un dictionnaire contenant les matières et leurs coefficients.

    Sortie:
    - str: Chaîne à afficher.
    """
    if nom_eleve in eleves:
        moyennes_eleve = calcule_moyenne(eleves[nom_eleve], d_matieres)
        for matiere, valeur in moyennes_eleve.items():
            print(f"{matiere}: {valeur}")
    else:
        print(f"L'élève {nom_eleve} n'existe pas.")


def lister_matieres(matieres):
    """
    Liste les matières.

    Entrée : matieres, dictionnaire des matières

    Sortie : string, la chaîne à afficher.
    """
    result = []
    for matiere, coefficient in matieres.items():
        result.append(f"{matiere}: Coefficient {coefficient}")
    return result


def ajouter_matiere(matieres, nom_matiere, coefficient):
    """
    Ajoute une nouvelle matière.

    Entrée : matieres, tableau des matières
            nom_matiere, string
            coefficient, float

    Sortie : string, chaîne de confirmation
    """
    if nom_matiere in matieres:
        return f"Matière {nom_matiere} déjà présente"
    matieres[nom_matiere] = coefficient
    return f"Matière {nom_matiere} ajoutée avec un coefficient de {coefficient}"


def modifier_coefficient(matieres, nom_matiere, nouveau_coefficient):
    """
    Modifie coefficient d'une matière.

    Entrée : matieres, tableau des matières
            nom_matiere, string
            nouveau_coefficient, float

    Sortie : string, chaîne de confirmation
    """
    if nom_matiere in matieres:
        matieres[nom_matiere] = nouveau_coefficient
        return f"Coefficient de {nom_matiere} modifié avec succès. Nouveau coefficient : {nouveau_coefficient}"
    else:
        return f"Matière {nom_matiere} n'existe pas dans la liste."


def lister_notes(t_notes):
    """
    Liste les notes d'un élève

    Entrée : t_notes, tableau de notes

    Sortie : string, chaîne à afficher
    """
    result = []
    if t_notes:
        result.append("\nListe des notes pour l'élève:")
        for i, note in enumerate(t_notes, start=1):
            result.append(
                f"{i}. Matière: {note[1]}, Valeur: {note[0]}, Coefficient: {note[2]}"
            )
    else:
        result.append("L'élève n'a pas de notes enregistrées.")

    return result


def ajouter_note(t_notes, matiere, note, coefficient):
    """
    Ajoute une note au tableau des notes.

    Entrée : t_notes, tableau de notes
            matiere, string
            note, float
            coefficient, float

    Sortie : string, chaîne de confirmation

    TO DO : vérifier que la matière existe  dans d_matier, sinon l'ajouter
    """
    t_notes.append([note, matiere, coefficient])
    return f"Note ajoutée pour l'élève en {matiere} avec une valeur de {note} et un coefficient de {coefficient}."


def modifier_note(t_notes, matiere, choix, nouvelle_valeur, nouveau_coefficient):
    """
    Modifie une note au tableau des notes.

    Entrée : t_notes, tableau de notes
            matiere, string
            choix, int, l'indice de la note à modifier
            nouvelle_valeur, float
            nouveau_coefficient, float

    Sortie : string, chaîne de confirmation
    """

    notes_a_modifier = [i for i, note in enumerate(t_notes) if note[1] == matiere]

    if notes_a_modifier and 1 <= choix <= len(notes_a_modifier):
        index_a_modifier = notes_a_modifier[choix - 1]

        t_notes[index_a_modifier][0] = nouvelle_valeur
        t_notes[index_a_modifier][2] = nouveau_coefficient

        return f"Note pour l'élève en {matiere} modifiée avec succès. Nouvelle valeur : {nouvelle_valeur}, Nouveau coefficient : {nouveau_coefficient}"
    elif not notes_a_modifier:
        return f"L'élève n'a pas de note enregistrée pour la matière {matiere}."
    else:
        return "Numéro de note invalide."


def calcule_moyenne(t_notes, d_matieres):
    """
    Calcule les moyennes

    Entrée : t_notes, tableau
            d_matieres, dictionnaire des matières

    Sortie : dictionnaire contenant les différentes moyennes. Un item par matière et un item supplémentaire pour la moyenne générale
    """
    moyennes_matiere = {}
    total_coefficients = 0
    total_points = 0

    for note in t_notes:
        matiere = note[1]
        coefficient = note[2]
        valeur = note[0]

        if matiere not in moyennes_matiere:
            moyennes_matiere[matiere] = {"total_points": 0, "total_coefficients": 0}

        moyennes_matiere[matiere]["total_points"] += valeur * coefficient
        moyennes_matiere[matiere]["total_coefficients"] += coefficient
        total_points += valeur * coefficient
        total_coefficients += coefficient

    result = {}
    for matiere, valeurs in moyennes_matiere.items():
        moyenne = valeurs["total_points"] / valeurs["total_coefficients"]
        result[matiere] = moyenne

    # Calculer la moyenne générale en utilisant les coefficients du dictionnaire d_matieres
    if total_coefficients > 0:
        moyenne_generale = sum(
            result[matiere] * d_matieres.get(matiere, 1.0) for matiere in result
        ) / sum(d_matieres.get(matiere, 1.0) for matiere in result)
        result["Moyenne générale"] = moyenne_generale

    return result


def menu_gestion_matieres(matieres):
    """
    Gère le menu pour la gestion des matières.

    Entrée:
    - matieres (dict): Un dictionnaire contenant les matières et leurs coefficients.

    Affiche un menu avec des options pour la gestion des matières, puis appelle les fonctions appropriées en fonction du choix de l'utilisateur.
    """
    while True:
        print("\nOptions pour la gestion des matières:")
        print("1. Lister les matières et leurs coefficients")
        print("2. Ajouter une matière")
        print("3. Modifier le coefficient d'une matière")
        print("4. Quitter")

        choix = input("Choisissez une option (1-4): ")

        if choix == "1":
            lister_matieres(matieres)
        elif choix == "2":
            nom_matiere = input("Entrez le nom de la matière: ")
            coefficient = float(input("Entrez le coefficient de la matière: "))
            print(ajouter_matiere(matieres, nom_matiere, coefficient))
        elif choix == "3":
            nom_matiere = input(
                "Entrez le nom de la matière dont vous voulez modifier le coefficient: "
            )
            nouveau_coefficient = float(input("Entrez le nouveau coefficient: "))
            print(modifier_coefficient(matieres, nom_matiere, nouveau_coefficient))
        elif choix == "4":
            print("Retour au menu principal.")
            break
        else:
            print("Option invalide. Veuillez choisir une option entre 1 et 4.")


def menu_gestion_notes(n, d_matieres, nom_eleve):
    """
    Gère le menu pour la gestion des notes de l'élève.

    Entrée:
    - n (list): Une liste des notes de l'élève.
    - d_matieres (dict): Un dictionnaire contenant les matières et leurs coefficients.

    Affiche un menu avec des options pour la gestion des notes de l'élève, puis appelle les fonctions appropriées en fonction du choix de l'utilisateur.
    """
    while True:
        print("\nOptions pour la gestion des notes:")
        print("1. Lister les notes de l'élève")
        print("2. Ajouter une note pour l'élève")
        print("3. Modifier une note de l'élève")
        print("4. Consulter les moyennes")
        print("5. Quitter")

        choix = input("Choisissez une option (1-5): ")

        if choix == "1":
            lister_notes(n)
        elif choix == "2":
            matiere = input("Entrez le nom de la matière: ")
            valeur = float(input("Entrez la valeur de la note: "))
            coefficient = float(input("Entrez le coefficient de la matière: "))
            print(ajouter_note(n, matiere, valeur, coefficient))
        elif choix == "3":
            matiere = input(
                "Entrez le nom de la matière dont vous voulez modifier la note: "
            )
            choix_note = int(input("Entrez le numéro de la note à modifier: "))
            print(modifier_note(n, matiere, choix_note))
        elif choix == "4":
            moyennes = calcule_moyenne(n, d_matieres)
            for matiere, valeur in moyennes.items():
                print(f"{matiere}: {valeur}")
        elif choix == "5":
            print("Retour au menu principal.")
            break
        else:
            print("Option invalide. Veuillez choisir une option entre 1 et 5.")


# Nouvelle fonction pour gérer les élèves
def menu_gestion_eleves(eleves):
    """
    Gère le menu pour la gestion des élèves.

    Entrée:
    - eleves (dict): Un dictionnaire contenant les élèves et leurs notes.

    Affiche un menu avec des options pour la gestion des élèves, puis appelle les fonctions appropriées en fonction du choix de l'utilisateur.
    """
    while True:
        print("\nOptions pour la gestion des élèves:")
        print("1. Ajouter un élève")
        print("2. Lister les élèves")
        print("3. Supprimer un élève")
        print("4. Retour au menu principal")

        choix = input("Choisissez une option (1-4): ")

        if choix == "1":
            nom_eleve = input("Entrez le nom de l'élève: ")
            print(ajouter_eleve(eleves, nom_eleve))
        elif choix == "2":
            print(lister_eleves(eleves))
        elif choix == "3":
            nom_eleve = input("Entrez le nom de l'élève à supprimer: ")
            print(supprimer_eleve(eleves, nom_eleve))
        elif choix == "4":
            print("Retour au menu principal.")
            break
        else:
            print("Option invalide. Veuillez choisir une option entre 1 et 4.")


def menu_consulter_moyennes(eleves, d_matieres):
    """
    Gère le menu pour la consultation des moyennes d'un élève.

    Entrée:
    - eleves (dict): Un dictionnaire contenant les élèves et leurs notes.
    - d_matieres (dict): Un dictionnaire contenant les matières et leurs coefficients.

    Affiche un menu avec des options pour la consultation des moyennes d'un élève, puis appelle les fonctions appropriées en fonction du choix de l'utilisateur.
    """
    while True:
        nom_eleve = input(
            "Entrez le nom de l'élève dont vous voulez consulter les moyennes (ou 'q' pour quitter): "
        )
        if nom_eleve.lower() == "q":
            break
        consulter_moyenne_eleve(eleves, nom_eleve, d_matieres)


def programme():
    # Exemple d'utilisation des fonctions de menu
    d_matieres = {}
    t_notes = []

    while True:
        print("\nOptions disponibles:")
        print("1. Gestion des matières")
        print("2. Saisir une note")
        print("3. Consultation des moyennes")
        print("4. Quitter")

        choix_principal = input("Choisissez une option (1-4): ")

        if choix_principal == "1":
            menu_gestion_matieres(d_matieres)
        elif choix_principal == "2":
            menu_gestion_notes(t_notes, d_matieres)
        elif choix_principal == "3":
            consulter_moyenne(t_notes)
        elif choix_principal == "4":
            print("Au revoir!")
            break
        else:
            print("Option invalide. Veuillez choisir une option entre 1 et 4.")


# -----------------------------------------------------------------------------


def test_ajouter_matiere():
    matieres = {}
    ajouter_matiere(matieres, "Math", 3.0)
    assert "Math" in matieres
    assert matieres["Math"] == 3.0


def test_modifier_coefficient():
    matieres = {"Math": 7}
    modifier_coefficient(matieres, "Math", 120)
    assert matieres["Math"] == 120


def test_ajouter_eleve():
    eleves = {}
    assert ajouter_eleve(eleves, "pol") == "Élève pol ajouté avec succès."
    assert ajouter_eleve(eleves, "pol") == "L'élève pol existe déjà."


def test_lister_eleves():
    eleves = {"pol": []}
    assert lister_eleves(eleves) == "1. pol"
    assert lister_eleves({}) == "Aucun élève enregistré."


def test_supprimer_eleve():
    eleves = {"pol": []}

    supprimer_eleve(eleves, "pol")
    assert eleves.__len__() == 0

    assert supprimer_eleve(eleves, "milan") == "L'élève milan n'existe pas."


def test_ajouter_note_eleve():
    eleves = {"pol": []}
    assert ajouter_note_eleve(eleves, "pol", "Math", 90.0, 1.0) == (
        "Note ajoutée pour l'élève pol en Math avec une valeur de 90.0 et un coefficient de 1.0."
    )
    assert (
        ajouter_note_eleve(eleves, "milan", "Math", 80.0, 1.0)
        == "L'élève milan n'existe pas."
    )


def test_modifier_note():
    n = []
    ajouter_note(n, "Math", 1.0, 3.0)
    modifier_note(n, "Math", 1, 8.0, 0.9)
    assert n[0] == [8.0, "Math", 0.9]


def test_calcule_moyenne():
    # Python assure conservation des égalités parfaites après promotion des float
    t_notes = [[90.0, "Math", 1.0], [80.0, "Math", 1.0]]
    d_matieres = {"Math": 1.0}
    assert calcule_moyenne(t_notes, d_matieres) == {
        "Math": 85.0,
        "Moyenne générale": 85.0,
    }


test_ajouter_matiere()
test_modifier_coefficient()
test_ajouter_eleve()
test_lister_eleves()
test_supprimer_eleve()
test_ajouter_note_eleve()
test_modifier_note()
test_calcule_moyenne()
print("tests passed\n")

# Aurait été préférable d'utiliser la lib unittest, mais je ne suis pas très familier a la gestion de l'OP en python

programme()
