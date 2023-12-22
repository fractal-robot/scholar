def checkInput(entree: str):
    """
    Entrée :
        entree (string) : la séquence ADN
    Sortie : / (goto main si séquence ADN invalide)
    """

    caracteresValides = set("ATGC")

    if not all(c in caracteresValides for c in entree):
        print("Entrée incorrecte.\n")
        main()


def trouverSousChainesRepetees(entree: str) -> list:
    """
    Entrée :
        entree (string) : la séquence ADN
    Sortie :
        Liste : les sous-chaînes répétées dans la séquence ADN
    """

    sousChainesRepetees = []

    for i in range(1, len(entree)):
        for j in range(0, len(entree) - i + 1):
            sousChaine = entree[j : j + i]
            if sousChaine in entree[j + i :]:
                sousChainesRepetees.append(sousChaine)

    return sousChainesRepetees


def trouverPlusLongueSousChaineRepetee(entree: str) -> str:
    """
    Entrée :
        entree (string) : la séquence ADN
    Sortie :
        string : la plus longue sous-chaîne répétée dans la séquence ADN
    """

    sousChainesRepetees = trouverSousChainesRepetees(entree)

    if not sousChainesRepetees:
        return "Aucune sous-chaîne répétée trouvée."

    return max(sousChainesRepetees, key=len)


def main():
    """
    - Obtenir séquence ADN via utilisateur
    - Vérifier input
    - Trouver la plus longue sous-chaîne répétée
    - Print la plus longue sous-chaîne répétée dans la séquence ADN
    """
    entree = str(input("Veuillez entrer la séquence ADN (A-T-G-C): "))
    checkInput(entree)

    plusLongueSousChaine = trouverPlusLongueSousChaineRepetee(entree)

    print("La plus longue sous-chaîne répétée est :", plusLongueSousChaine)


if __name__ == "__main__":
    main()


def test():
    val = trouverSousChainesRepetees("AAACCT")
