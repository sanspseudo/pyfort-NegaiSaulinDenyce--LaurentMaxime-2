'''
pyfort-NegaiSaulinDényce-LaurentMaxime-D2
Auteurs:
    Negai Saulin Dényce
    Laurent Maxime
Rôle:
    Permettre d'avoir 4 épreuves de mathématiques dans le jeu
'''

import random


'''
Rôle:
    Calculer la factorielle d'un nombre n
Paramètres:
    n vient de manière aléatoire de la fonction epreuve_math_factorielle(). Permet de simplifier en séparant l'épreuve et la méthode de calcul
Résultat:
    Le résultat retourne la factorielle d'un nombre n
'''
def factorielle(n):
    resultat = 1
    if n > 0:
        for i in range(1,n+1):  #Boucle qui multiplie chaque nombre de 1 à n
            resultat *= i
    return(resultat)


'''
Rôle:
    En proposant un calcul de factorielle, permet de tenter une réponse à la question
Résultat:
    Le résultat obtenu est un booléen permettant de savoir si la réponse donnée par l'utilisateur est la bonne réponse. Si c'est faux, la réponse est affichée
'''
def epreuve_math_factorielle():
    n = random.randint(1, 10)
    print("Calculez la factorielle de", n)

    while True: #Boucle de sécurité
        proposition = input("Saisissez votre proposition : ")
        if proposition.isdigit():
            proposition = int(proposition)
            break
        else:
            print("\nEntrez un nombre entier")
    
    if proposition == factorielle(n):   #Vérifier si l'utilisateur a une bonne réponse
        return(True)
    else:
        print(f"\nVous avez raté. La réponse était {factorielle(n)}")
        return(False)


'''
Rôle:
    Trouver un nombre x dans une équation du premier degré
Résultat:
    Les résultats retournés sont les variables de l'équation et une liste contenant les valeurs de x en incluant plusieurs types de réponses selon la pensée de chaque joueur
'''
def resoudre_equation_lineaire():
    L = []
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    
    #Rajouter à la liste L, les réponses possibles de l'utilisateur
    if a == b:
        L.append("-1")
        L.append(f"-{b}/{a}")
    elif a == 1:
        L.append(f"-{b}")
        L.append(f"-{b}/{a}")
    else:
        L.append(f"-{b}/{a}")
    
    return(a, b, L)


'''
Rôle:
    En proposant de trouver une valeur de x dans une équation du premier degré, permet de tenter une réponse à la question
Résultat:
    Le résultat obtenu est un booléen permettant de savoir si la réponse donnée par l'utilisateur est la bonne réponse. Si c'est faux, la réponse est affichée
'''
def epreuve_math_equation():
    a, b, L = resoudre_equation_lineaire()
    print(f"Résolvez l'équation {a}x + {b} = 0")

    while True: #Boucle de sécurité
        proposition = input("Saisissez votre proposition sous forme fractionnelle de type (X/Y), x = ").replace(" ", "")

        if not proposition: #Vérifier si l'input est vide
            print("\nVous devez mettre au moins 1 caractère dans l'input")
            continue

        if proposition in L:    #Vérifier si la réponse de l'utilisateur est présente dans la liste de réponses possibles
            return(True)
            break
        else:
            if a == b:
                print(f"\nVous avez raté. La réponse était {L[0]} ou {L[1]}")
            elif a == 1:
                print(f"\nVous avez raté. La réponse était {L[0]} ou {L[1]}")
            else:
                print(f"\nVous avez raté. La réponse est {L[0]}")
            return(False)


'''
Rôle:
    Vérifier si un nombre n est premier
Paramètre:
    n vient de manière aléatoire de la fonction epreuve_math_premier(). Permet de simplifier en séparant l'épreuve et la méthode de calcul
Résultat:
    Le résultat retourné est un booléen pour vérifier que n est premier ou pas
'''
def est_premier(n):
    if n <= 1:
        return(False)
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return(False)
    return(True)


'''
Rôle:
    Trouver l'entier supérieur ou égal à n qui soit premier
Paramètre:
    n vient de manière aléatoire de la fonction epreuve_math_premier(). Permet de simplifier en séparant l'épreuve et la méthode de calcul
Résultat:
    Le resultat retourné est le l'entier supérieur ou égal à n qui soit premier
'''
def premier_le_plus_proche(n):
    while not est_premier(n): #Tant que le n étudié n'est pas premier, la boucle continue
        n += 1
    return(n)


'''
Rôle:
    En proposant de trouver le nombre premier supérieur ou égal le plus proche à n, permet de tenter une réponse à la question
Résultat:
    Le résultat obtenu est un booléen permettant de savoir si la réponse donnée par l'utilisateur est la bonne réponse. Si c'est faux, la réponse est affichée
'''
def epreuve_math_premier():
    n = random.randint(10, 20)
    n1 = premier_le_plus_proche(n)
    print("Trouvez le nombre premier supérieur ou égal le plus proche à", n)

    while True: #Boucle de sécurité
        proposition = input("Saisissez votre proposition : ")
        if proposition.isdigit(): #Vérifier si l'input est un entier
            proposition = int(proposition)
            break
        else:
            print("\nEntrez un nombre valide")
    
    if proposition == n1: #Vérifier l'entrée de l'utilisateur
        return(True)
    else:
        print(f"\nVous avez raté. La réponse était {n1}")
        return(False)
    

'''
Rôle:
    L'utilisateur doit trouver la réponse au problème qui est un calcul entre 5 entiers générés aléatoirement
Résultat:
    Le résultat obtenu est un booléen permettant de savoir si la réponse donnée par l'utilisateur est la bonne réponse. Si c'est faux, la réponse est affichée
'''
def epreuve_roulette_mathematique():
    #Génération aléatoire des 5 entiers
    n1 = random.randint(1, 20)
    n2 = random.randint(1, 20)
    n3 = random.randint(1, 20)
    n4 = random.randint(1, 20)
    n5 = random.randint(1, 20)

    choix_operation = random.randint(1, 3)
    #Calculer les résultats selon la fonction mathématique choisie aléatoirement
    if choix_operation == 1:
        operation = "addition"
        resultat = n1 + n2 + n3 + n4 + n5
    elif choix_operation == 2:
        operation = "soustraction"
        resultat = n1 - n2 - n3 - n4 - n5
    else:
        operation = "multiplication"
        resultat = n1 * n2 * n3 * n4 * n5

    print("Nombres sur la roulette : [", n1, ",", n2, ",", n3, ",", n4, ",", n5, "]")
    print("Calculez le résultat en combinant ces nombres avec une", operation)
    
    while True: #Boucle de sécurité
        proposition_input = input("Votre réponse : ")
        proposition = proposition_input.strip("-")  #Vérifier si lorsque le résultat est négatif, que l'input est bien un entier
        if proposition.isdigit():
            proposition = int(proposition_input)
            break
        else:
            print("\nEntrez un nombre valide")

    if proposition == resultat:
        return(True)
    else:
        print(f"\nVous avez raté. La réponse était {resultat}")
        return(False)


'''
Rôle:
    Choisir aléatoirement une des 4 fonctions principales du programme, les 4 épreuves du jeu
Résultat:
    Le résultat retourné est la fonction (l'épreuve) choisie pour l'utilisateur
'''
def epreuve_math():
    epreuves = [epreuve_math_factorielle, epreuve_math_equation, epreuve_math_premier, epreuve_roulette_mathematique]
    epreuve = random.choice(epreuves)
    return(epreuve())