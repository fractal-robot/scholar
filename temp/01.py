def checkInput(entree: str):
    """
    entrée :
        entree (string) : la séquence ADN
    sortie : / (goto main si séquence ADN invalide)
    """

    for c in entree:
        if not (c == "A" or c == "T" or c == "G" or c == "C"):
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
    """

    valDict = {}

    for i in range(2, len(entree)):
        for j in range(0, len(entree), i):
            valeur = entree[j : j + i]
            if len(valeur) == i:
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
    entree = str(input("Veuillez entrer la séquence ADN: "))
    checkInput(entree)

    valDict = trouverSuites(entree)
    valeurMax = trouverMaxOccurences(valDict)

    print("La valeur maximale est atteinte en " + str(valeurMax) + " par : ")
    for key in valDict:
        if valDict[key] == valeurMax:
            print("- " + key)


main()
