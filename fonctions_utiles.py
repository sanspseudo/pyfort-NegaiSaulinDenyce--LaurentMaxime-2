'''
pyfort-NegaiSaulinDényce-LaurentMaxime-D2
Auteurs:
    Negai Saulin Dényce
    Laurent Maxime
Rôle:
    Permettre de cadrer le jeu et le rendre plus plaisant
'''


'''
Rôle:
    Accueillir les utilisateurs et expliquer les règles du jeu
Résultat:
    La fonction affiche 3 lignes de règles et de bienvenue
'''
def introduction():
    print("Bienvenue au jeu du Fort Boyard")
    print("Vous aurez différentesd épreuves  à accomplir, seul ou en équipe, pour gagner des clés et déverrouiller la salle du trésor")
    print("Votre objectif est de ramasser trois clés pour accéder à la salle du trésor et remporté le Grand Jeu")


'''
Rôle:
    Composer des équipes de 1 à 3 personne(s), vérifiant qu'il y ait obligatoirement un leader. Si à la fin des entrés du joueur il n'y a pas de leader, il doit recommencer à entrer les informations des joueurs
Résultat:
    Le résultat retourné est une liste de dictionnaires. Chaque dictionnaire comporte les informations d'un membre de l'équipe
'''
def composer_equipe():
    while True: #Boucle de sécurité
        nb_joueurs = input("\nCombien de joueurs vont participer au jeu ? (Maximum de 3 joueurs) : ").strip()
        if nb_joueurs.isdigit():    #Vérifier que l'input soit bien un nombre
            nb_joueurs = int(nb_joueurs)
            if 1 <= nb_joueurs <= 3:
                break
            else:
                print("Entrez un nombre entre 1 et 3")
        else:
            print("Entrez un nombre entre 1 et 3")

    equipe = []
    leader = False

    #Créer les dictionnaires de joueurs
    for _ in range(nb_joueurs):
        nom = input("Rentrez le nom de votre joueur : ").strip()
        while not nom or not nom.isalpha(): #Vérifier qu'il y ai au moins 1 caractère et que des lettres
            print("\nLe nom doit contenir uniquement des lettres et ne pas être vide.")
            nom = input("Rentrez le nom de votre joueur : ").strip()

        profession = input("Rentrez la profession de votre personnage : ").strip()
        while not profession or not profession.isalpha():
            print("\nLa profession doit contenir uniquement des lettres et ne pas être vide.")
            profession = input("Rentrez la profession de votre personnage : ").strip()

        leader_choix = None
        #Proposer à rendre le joueur leader si il n'y en a pas déjà un
        if not leader:
            while leader_choix not in ["oui", "non"]:
                leader_choix = input("Est-ce que ce personnage est le leader ? (Oui / Non) : ").strip().lower()
                if leader_choix == "oui":
                    leader = True
        else:
            leader_choix = "non"

        personnage = {"nom": nom, "profession": profession, "leader": leader_choix}
        equipe.append(personnage)

    #Recommencer la procédure si il n'y a pas de leader
    if not leader:
        print("\nVous n'avez pas désigner un joueur comme leader. Vous devez recommencer la saisie des personnages.\n")
        return(composer_equipe())

    return(equipe)


'''
Rôle:
    Proposer le menu des épreuves pour que l'utilisateur puisse choisir le type d'épreuve qu'il veut tenter
Résultat:
    Le résultat retourne le numéro de l'épreuve que l'utilisateur a choisi
'''
def menu_epreuves():
    print("\n\n\nMenu des épreuves du Fort Boyard")
    print("1. Epreuve de mathématiques\n")
    print("2. Epreuve de hasard\n")
    print("3. Epreuve de logique\n")
    print("4. Enigme du Père Fouras\n")

    #Boucle de sécurité
    while True:
        choix = input("Choix : ").strip()
        if choix.isdigit():
            choix = int(choix)
            if choix in [1, 2, 3, 4]:
                return(choix)
            else:
                print("Entrez un nombre entre 1 et 4")
        else:
            print("Entrez un nombre valide entre 1 et 4")


'''
Rôle:
    Laisser l'utilisateur se choisir comme joueur pendant la prochaine épreuve
Paramètre:
    La liste de dictionnaires de tous les joueurs dans l'équipe
Résultat:
    Afficher le dictionnaire du joueur selectionné
'''
def choisir_joueur(equipe):
    print("\n\n\nListe des joueurs disponibles :")

    #Donner le rôle 'membre' pour les joueurs n'étant pas leader
    for i in range (len(equipe)):
        joueur = equipe[i]
        if joueur["leader"] == "oui":
            role = "Leader"
        else:
            role = "Membre"
        print(f"{i + 1}. {joueur['nom']} ({joueur['profession']}) - {role}")
    
    #Boucle de sécurité
    while True:
        choix = input(f"Entrez le numéro du joueur : ").strip()
        if choix.isdigit():
            choix = int(choix)
            if 1 <= choix <= len(equipe):
                joueur_selectionne = equipe[choix - 1]
                print(f"Joueur sélectionné : {joueur_selectionne}")
                return joueur_selectionne
            else:
                print(f"Entrez un numéro valide")
        else:
            print("Entrez un numéro valide")

