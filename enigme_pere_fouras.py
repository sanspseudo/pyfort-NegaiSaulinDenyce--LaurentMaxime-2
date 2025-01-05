'''
pyfort-NegaiSaulinDényce-LaurentMaxime-D2
Auteurs:
    Negai Saulin Dényce
    Laurent Maxime
Rôle:
    Permettre de tenter de trouver la fameuse énigme du père Fouras
'''


import json
import random


'''
Rôle:
    Charger les énigmes en ouvrant le fichier JSON
Paramètre:
    Le chemin du fichier JSON avec les énigmes
Résultat:
    Le résultat retourné est une liste d'énigmes
'''
def charger_enigmes(fichier):
    with open(fichier, "r", encoding="utf-8") as file:
        enigmes = json.load(file)
    return(enigmes)


'''
Rôle:
    Permettre d'enlever le espaces inutiles et mettre les majuscules en minuscules
Paramètre:
    Le texte à 'normaliser'
Résultat:
    Le résultat retourné est le texte de départ sans espaces, et avec des majuscules rendues minuscules
'''
def normaliser_texte(texte):
    return(texte.strip().lower())


'''
Rôle:
    Charger les énigmes du fichier JSON dédié et demander à l'utilisateur d'y répondre avec un nombre de 3 essais
Résultat:
    Le résultat retourné est un booléen dépendant de si le joueur a réussi l'énigme ou pas sous 3 tentatives
'''
def enigme_pere_fouras():
    chemin_fichier = "data/enigmesPF.json"
    liste_enigmes = charger_enigmes(chemin_fichier)

    enigme_choisie = random.choice(liste_enigmes) #Choisir une énigme aléatoirement dans la liste
    nombre_essais = 3

    print("Bienvenue dans l'épreuve du Père Fouras ! Vous devez résoudre l'énigme pour tenter de gagner une clé")
    print("\nVoici votre énigme :")
    print(enigme_choisie["question"])

    #Boucle qui s'arrete lorsque le nombre de tentatives est nul
    while nombre_essais > 0:
        reponse_joueur = input("Votre réponse : ")

        #Vérifier qu'une réponse soit écrite
        if not reponse_joueur:
            print("\nEntrez une réponse")
            continue
        
        reponse_joueur = normaliser_texte(reponse_joueur)
        reponse_attendue = normaliser_texte(enigme_choisie["reponse"])
        
        if reponse_joueur == reponse_attendue:
            return(True)
        else:
            nombre_essais -= 1
            if nombre_essais > 0:
                print(f"\nCe n'est pas la bonne réponse. Il vous reste {nombre_essais} tentative(s)")
            else:
                print(f"\nDommage ! C'était pourtant si simple. La réponse était : {enigme_choisie['reponse']}")
                return(False)