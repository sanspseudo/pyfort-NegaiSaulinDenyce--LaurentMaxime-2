'''
pyfort-NegaiSaulinDényce-LaurentMaxime-D2
Auteurs:
    Negai Saulin Dényce
    Laurent Maxime
Rôle:
    Permettre de jouer à la bataille navale, la seule épreuve logique
'''


import random


'''
Rôle:
    Créer une grille de 5x5 vide
Résultat:
    Le résultat retourné est la liste 2D de la grille vide
'''
def grille_vide():
    L = [[" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "]]  
    return(L)


'''
Rôle:
    Afficher une jolie grille 5x5 pour aider l'utilisateur à voir le jeu
Paramètres:
    grille : Permet d'avoir la grille souhaitée
    message : Permet d'afficher un message, un titre à la grille
Résultat:
    Le résultat retourné est une représentation de la grille qui est affichée à l'utilisateur
'''
def affiche_grille(grille, message):
    print(message)
    print("  +---+---+---+---+---+")
    for ligne in grille:    #Dessiner une portion de grille en plusieurs fois suivant la grille souhaitée
        print("  | " + " | ".join(ligne) + " |")
        print("  +---+---+---+---+---+")


'''
Rôle:
    Demander une position sur la grille qui sera ensuite vérifiée dans une autre fonction
Résultat:
    Les résultats retournés sont la ligne et la colonne des coordonnées dans la grille
'''
def demande_position():
    while True: #Boucle de sécurité
        ligne = input("Entrez la ligne entre 1 et 5 : ")
        if ligne.isdigit(): #Vérifier que l'input est un nombre
            ligne = int(ligne) - 1
            if 0 <= ligne <= 4:
                break
            else:
                print("\nLa ligne doit être entre 1 et 5.")
        else:
            print("\nVeuillez entrer un nombre valide.")

    while True:
        colonne = input("Entrez la colonne entre 1 et 5 : ")
        if colonne.isdigit():
            colonne = int(colonne) - 1
            if 0 <= colonne <= 4:
                break
            else:
                print("\nLa colonne doit être entre 1 et 5.")
        else:
            print("\nVeuillez entrer un nombre valide.")

    return(ligne, colonne)


'''
Rôle:
    Placer 2 bateaux doubles aléatoirement dans la grille du joueur et du maître du jeu. Horizontalement ou verticalement
Paramètres:
    grille : La grille du jeu
    taille : La taille du bateau à placer
Résultat:
    Mettre des 'B' dans la grille, symbolisant les bateaux (2 par bateaux doubles), dans les emplacements vides. Les bateaux ne peuvent pas se chevaucher
'''
def placer_bateau(grille, taille):
    #Boucle pour chercher un emplacement de bateau vide
    while True:
        direction = random.choice([0, 1])   #Direction aléatoire du bateau choisie
        ligne, colonne = random.randint(0, 4), random.randint(0, 4)

        if direction == 0: #Direction horizontale
            if colonne + taille - 1 <= 4 and all(grille[ligne][colonne + i] == " " for i in range(taille)): #Vérifier que l'emplacement est vide
                for i in range(taille):
                    grille[ligne][colonne + i] = "B"
                break
        else:   #Direction verticale
            if ligne + taille - 1 <= 4 and all(grille[ligne + i][colonne] == " " for i in range(taille)):
                for i in range(taille):
                    grille[ligne + i][colonne] = "B"
                break


'''
Rôle:
    Initialiser la grille en plaçant les deux bateaux simples, et en rajoutant les deux bateaux doubles dans les places restantes
Résultat:
    Le résultat retourné est la grille avec tous les bateaux placés
'''
def init():
    print("\nPlacez vos bateaux simples (1 case) : ")
    #Initialiser une grille vide
    L = grille_vide()

    for i in range(2):
        print(f"\nPlacer le bateau simple #{i + 1} :")
        while True:
            ligne, colonne = demande_position() #Saisir les coordonnées des bateaux simples
            if L[ligne][colonne] == " ":
                L[ligne][colonne] = "B"
                break
            else:
                print("Cette position est déjà occupée. Choisissez une autre position.")

    print("\nLes deux bateaux doubles sont placés de manière aléatoire.")
    for i in range(2):
        placer_bateau(L, 2) #Placer les bateaux doubles

    return(L)


'''
Rôle:
    Retourner le numéro du joueur suivant pour ce jeu à deux joueurs, entre 0 et 1
Paramètre:
    Le numéro de joueur actuel
Résultat:
    Le résultat retourné est le numéro du joueur suivant
'''
def suiv(joueur):
    return (joueur + 1) % 2


'''
Rôle:
    Vérifier si le joueur a touché tous les bateaux adverses en parcourant la grille
Paramètre:
    La grille de tir du joueur actuel
Résultat:
    Le résultat retourné est un booléen. Permet de vérifier si les 6 bateaux du joueur adverse ont coulés
'''
def gagne(grille_tirs_joueur):
    n = 0

    #Parcourir la grille pour chercher des 'X', soit les coordonnées des bateaux touchés
    for i in range(5):
        for j in range(5):
            if grille_tirs_joueur[i][j] == "X":
                n += 1
            if n == 6:
                return(True)
    return(False)


'''
Rôle:
    Suivre le tour du joueur actuel en tirant une fois dans une position donnée par l'utilisateur ou aléatoire pour le maître du jeu
Paramètres:
    joueur : Le numéro du joueur actuel
    grille_tirs_joueur : La grille de tir du joueur actuel, composé de ' ', 'X' ou '.'
    grille_adversaire : La grille du joueur adverse, composé de ' ' ou 'B'
    touches_mj : Le nombre de fois où le maître du jeu a touché l'utilisateur
Résultat:
    Les grilles et les nombres de touches sont modifiées
'''
def tour(joueur, grille_tirs_joueur, grille_adversaire, touches_mj):
    if joueur == 0: #Le maître du jeu tire aléatoirement dans la grille
        ligne = random.randint(0, 4)
        colonne = random.randint(0, 4)
        print(f"\n\nLe maître du jeu tire en position {ligne + 1}, {colonne + 1}")
    else:
        print("\nVotre tour : ")
        while True: #Vérifier que la place dans la grille est vide
            ligne, colonne = demande_position()
            if grille_tirs_joueur[ligne][colonne] == " ":
                break
            else:
                print("\nVous avez déjà tiré à cette position. Choisissez une autre.")

    #Vérifier si l'endroit touché est un bateau ou de l'eau
    if grille_adversaire[ligne][colonne] == "B":
        print("Tir réussi")
        grille_tirs_joueur[ligne][colonne] = "X"
        grille_adversaire[ligne][colonne] = " "
        #Incrémente les touches du maître du jeu si il a touché un bateau de l'utilisateur
        if joueur == 0:
            touches_mj[0] += 1
            print(f"Le maître du jeu a touché {touches_mj} bateau(x)")
    else:
        print("Tir manqué")
        grille_tirs_joueur[ligne][colonne] = "."

    #Afficher la grille si c'est au tour de l'utilisateur
    if joueur != 0:
        affiche_grille(grille_tirs_joueur, f"\nGrille mise à jour pour le joueur {joueur} : ")


'''
Rôle:
    Exécuter le jeu de la bataille navale. Chaque joueur place ces bateaux et se tirent dessus jusqu'à que l'un des joueurs n'ai plus de bateaux
Résultat:
    Le résultat retourné est un booléen. Permettant de savoir si l'utilisateur (joueur 1) a gagné ou perdu 
'''
def jeu_bataille_navale():
    print("Bienvenue au jeu de la bataille navale")
    print("Vous devre placer 4 bateaux (2 taille simple, 2 taille double). Votre objectif est de trouver les bateaux du maître du jeu avant qu'il trouve les vôtres\n")


    print("  +---+---+---+---+---+")
    print("  |   |   |   |   |   |")
    print("  +---+---+---+---+---+")
    print("  |   |   |   |   |   |")
    print("  +---+---+---+---+---+")
    print("  |   |   |   |   |   |")
    print("  +---+---+---+---+---+")
    print("  |   |   |   |   |   |")
    print("  +---+---+---+---+---+")
    print("  |   |   |   |   |   |")
    print("  +---+---+---+---+---+")


    #Initialiser les grilles
    grille_joueur = init()
    affiche_grille(grille_joueur, "\n\nVotre grille : ")

    grille_mj = grille_vide()
    #Placement des bateaux simples puis doubles du maître du jeu
    for _ in range(2):
        while True:
            ligne, colonne = random.randint(0, 4), random.randint(0, 4)
            if grille_mj[ligne][colonne] == " ":
                grille_mj[ligne][colonne] = "B"
                break
    for _ in range(2):
        placer_bateau(grille_mj, 2)
    
    #Initialiser les grilles de tir
    grille_tirs_joueur = grille_vide()
    grille_tirs_mj = grille_vide()

    touches_mj = [0]
    joueur = 1

    #Boucle principale du jeu
    while True:
        if joueur == 0: #Tour du maître du jeu
            tour(joueur, grille_tirs_mj, grille_joueur, touches_mj)
        else:   #Tour de l'utilisateur
            tour(joueur, grille_tirs_joueur, grille_mj, touches_mj)

        if gagne(grille_tirs_joueur):
            return(True)
        elif gagne(grille_tirs_mj):
            return(False)

        #Changer de tour
        joueur = suiv(joueur)