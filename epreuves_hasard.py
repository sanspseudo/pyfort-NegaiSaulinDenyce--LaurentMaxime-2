'''
pyfort-NegaiSaulinDényce-LaurentMaxime-D2
Auteurs:
    Negai Saulin Dényce
    Laurent Maxime
Rôle:
    Permettre d'avoir 2 épreuves de hasard dans le jeu
'''


import random


'''
Rôle:
    Jouer à un jeu de bonneteau simple
Résultat:
    Le résultat retourné est un booléen permettant de savoir si l'utilisateur a trouvé le bon bonneteau ou pas. Si oui, il gagne une clé (dans un autre programme)
'''
def bonneteau():
    L = ['A', 'B', 'C'] #Liste des 3 bonneteaux
    val_bonneteau = random.choice(L)
    num_tentative = 2
    print("Bienvenue au jeu du bonneteau. La règle est de choisir un des trois bonneteaux et d'espérer tomber sur le bon. Vous avez deux essais pour gagner une clé")
    print("   ____      ____      ____")
    print("  /    \\    /    \\    /    \\")
    print(" /   A  \\  /   B  \\  /   C  \\")
    print(" \\______/  \\______/  \\______/")

    for _ in range(num_tentative):
        print(f"\nIl vous reste {num_tentative} tentatives")

        choix = input("Choisissez un bonneteau entre A, B et C : ").strip().upper() #Vérifier si l'input ne comporte pas d'espaces et qu'il se mette en majuscule s'il est en minuscule
        while choix not in L: #Boucle de sécurité
            print("\nEntrez une des 3 lettres")
            choix = input("Choisissez un bonneteau entre A, B et C : ").strip().upper()
            
        if choix == val_bonneteau:
            return(True)
        else:
            print("\nVous n'avez pas réussi cette tentative")
        
        num_tentative -= 1

    print(f"\nVous avez perdu. Le bon bonneteau était {val_bonneteau}")
    return(False)


'''
Rôle:
    Avoir 3 tentatives pour tomber sur un nombre 6 avec 2 dés, sachant que un "maître du jeu" joue aussi
Résultat:
    Le résultat retourné est un booléen permettant de savoir si l'utilisateur est tombé sur un 6. Si le nombre de tentatives est atteint ou que le maître du jeu a eu un 6 avant, le joueur a perdu
'''
def jeu_lance_des():
    num_tentative = 3

    print("Bienvenue au jeu des dés. La règle est de lancer les dés et espérer tomber sur un nombre 6")
    print("En face de vous, le maître du jeu joue après vous pour tenter de tomber sur un 6 également. Si vous gagnez, vous recevrez une clé. Sinon, vous perdez\n")
    
    print("    +-----+    +-----+")
    print("   /  o  /|   / o o /|")
    print("  +-----+ |  +-----+ |")
    print("  |  o  | |  | o o | |")
    print("  |     | +  |     | +")
    print("  | o o |/   | o o |/")
    print("  +-----+    +-----+")

    for _ in range(3):
        print("\nIl vous reste", num_tentative, "tentatives")
        input("Appuyez sur 'Entrée' pour lancer les dés ")

        #Tour du joueur
        resultat_de_1 = random.randint(1, 6)
        resultat_de_2 = random.randint(1, 6)
        joueur = (resultat_de_1, resultat_de_2)
        print(f"\nVoici le résultat des dés que vous avez lancer : {resultat_de_1}, {resultat_de_2}")

        if resultat_de_1 == 6 or resultat_de_2 == 6:
            print("\nVous avez remporté la partie et avez gagné la clé")
            return(True)
        
        #Tour du maître du jeu
        resultat_de_ia_1 = random.randint(1, 6)
        resultat_de_ia_2 = random.randint(1, 6)
        print(f"Le maître du jeu a lancé les dés et a obtenu : {resultat_de_ia_1}, {resultat_de_ia_2}")
        
        if resultat_de_ia_1 == 6 or resultat_de_ia_2 == 6:
            print("\nLe maître du jeu a remporté la partie")
            return(False)
        
        print("\nAucun joueur n'a eu de 6")
        num_tentative -= 1
    
    if num_tentative == 0: #Tentatives maximum atteintes
        print("Aucun joueur n'a obtenu un 6 après trois essais. C'est un match nul")
        return(False)


'''
Rôle:
    Choisir aléatoirement une des 2 fonctions du programme, les 2 épreuves du jeu
Résultat:
    Le résultat retourné est la fonction (l'épreuve) choisie pour l'utilisateur
'''
def epreuve_hasard():
    epreuves = [bonneteau, jeu_lance_des]
    epreuve = random.choice(epreuves)
    return(epreuve())