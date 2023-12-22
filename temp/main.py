def estSequenceValide(sequenceADN: str, test: bool=False) -> bool:
    """
    Verifie que la sequenceADN rentree par l'utilisateur est une sequence adn valide

    Entrée :
        sequenceADN (string): la séquence ADN
        test (booleen): vrai si la fonction est utilisee pour un unit test, permet de ne pas afficher les messages d'erreurs sur l'ecran
    Sortie :
        booleen: vrai si la sequence est valide, faux sinon 
    """

    if len(sequenceADN) < 1:
        if not test:
            print("Entrée incorrecte, la sequence doit faire au minimum 1 caractere")
        return False

    caracteresValides = set("ATGC")

    if not all(c in caracteresValides for c in sequenceADN):
        if not test:
            print("Entrée incorrecte, la sequence ne doit contenir que A-T-G-C.\n")
        return False
    
    return True


def trouverSousChainesRepetees(sequenceADN: str) -> list:
    """
    Cherche toutes les chaines de caracteres qui se repetent dans la sequence ADN et les renvoit dans une liste

    Entrée :
        sequenceADN (string): la séquence ADN
    Sortie :
        Tableau (array): les sous-chaînes répétées dans la séquence ADN
    """

    sousChainesRepetees = []

    for i in range(1, len(sequenceADN)):
        for j in range(0, len(sequenceADN) - i + 1):
            sousChaine = sequenceADN[j:j+i]
            if sousChaine in sequenceADN[j+i:]:
                sousChainesRepetees.append(sousChaine)

    return sousChainesRepetees


def trouverPlusLongueSousChaineRepetee(sequenceADN: str) -> str:
    """ 
    Cherche la chaine de caracteres la plus longue parmis toutes celles qui se repetent dans la sequence ADN

    Entrée :
        sequenceADN (string): la séquence ADN
    Sortie :
        string: la plus longue sous-chaîne répétée dans la séquence ADN
    """

    sousChainesRepetees = trouverSousChainesRepetees(sequenceADN)

    if not sousChainesRepetees:
        return "Aucunes sous-chaînes répétées trouvées."

    return max(sousChainesRepetees, key=len)


def main():
    """
    Fonction principale du programme

    Demande la sequence ADN a l'utilisateur et la stocke, verifie qu'elle est bien valide puis affiche la plus longue sequence repete
    """
    entree = str(input("Veuillez entrer la séquence ADN (A-T-G-C): "))
    
    if not estSequenceValide(entree):
        main() # Si la sequence n'est pas valide on relance le programme
        return


    plusLongueSousChaine = trouverPlusLongueSousChaineRepetee(entree)

    print("La plus longue sous-chaîne répétée est :", plusLongueSousChaine)


def tests_unitaires():
    """
    Fonction de test du programne, renverra une erreur si ce dernier ne fonctionne pas correctement
    """
    
    assert estSequenceValide("", True) == False
    assert estSequenceValide("ASDD", True) == False
    assert estSequenceValide("AATTGGAATTGGCGCCTTA") == True

    assert trouverSousChainesRepetees("AATTGGAATTGGCGCCTTA") == ['A', 'A', 'T', 'T', 'G', 'G', 'A', 'A', 'T', 'T', 'G', 'G', 'C', 'C', 'T', 'AA', 'AT', 'TT', 'TG', 'GG', 'TT', 'GC', 'AAT', 'ATT', 'TTG', 'TGG', 'AATT', 'ATTG', 'TTGG', 'AATTG', 'ATTGG', 'AATTGG']
    assert trouverSousChainesRepetees("ATGC") == []

    assert trouverPlusLongueSousChaineRepetee("AAAAAAAAAAAAAAAA") == "AAAAAAAA"
    assert trouverPlusLongueSousChaineRepetee("AATTGGAATTGGCGCCTTA") == "AATTGG"
    assert trouverPlusLongueSousChaineRepetee("ATGC") == "Aucunes sous-chaînes répétées trouvées."


if __name__ == "__main__":
    tests_unitaires()
    main()
