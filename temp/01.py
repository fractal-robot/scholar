def checkInput(entree: str):
    """
    entrée :
        entree (string) : la séquence ADN
    sortie : / (goto main si séquence ADN invalide)
    """

    caracteresValides = set("ATGC")

    if not all(c in caracteresValides for c in entree):
        print("Entrée incorrecte.\n")
        main()


def trouverSuites(entree: str) -> dict:
    """
    entrée :
        entree (string) : la séquence ADN
    sortie :
        dictionnaire :
            clé : suite de caractères
            valeur : nombre d'occurence

    précondition :
        callback main si entrée trop courte
    """

    valDict = {}

    tailleMinSequence = 2

    if len(entree) < tailleMinSequence:
        print("La séquence ADN est trop courte.")
        main()

    for i in range(tailleMinSequence, len(entree)):
        for j in range(0, len(entree) - i + 1):
            valeur = entree[j : j + i]
            if valeur in valDict:
                valDict[valeur] += 1
            else:
                valDict[valeur] = 1

    return valDict


def trouverMaxOccurences(valDict: dict) -> int:
    """
    entrée :
        valDict (dictionnaire) : les différentes suites de nombres et leurs occurences
    sortie :
        int : la suite avec le plus d'occurences dans la séquence ADN
    """

    valeurMax = 0

    for key in valDict:
        if valDict[key] > valeurMax:
            valeurMax = valDict[key]

    return valeurMax


def main():
    """
    - obtenir séquence ADN via utilisateur
    - vérifier input
    - trouver les différentes suites
    - trouver l'occurence maximale
    - print la (ou les si plusieurs de même taille) plus longue suite(s) dans la séquence adn
    """
    entree = str(input("Veuillez entrer la séquence ADN (A-T-G-C): "))
    checkInput(entree)

    valDict = trouverSuites(entree)
    valeurMax = trouverMaxOccurences(valDict)

    print(
        "La valeur maximale est atteinte avec " + str(valeurMax) + " occurences par : "
    )
    for key in valDict:
        if valDict[key] == valeurMax:
            print("- " + key)


if __name__ == "__main__":
    main()
