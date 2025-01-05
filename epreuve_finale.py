'''
pyfort-NegaiSaulinDényce-LaurentMaxime-D2
Auteurs:
    Negai Saulin Dényce
    Laurent Maxime
Rôle:
    Permettre à l'utilisateur de participer à l'épreuve finale du jeu
'''


import json
import random


'''
Rôle:
    L'utilisateur doit trouver un mot-code pour accéder à la salle au trésor à l'aide d'indices. Il a le droit à 3 essais
Résultat:
    Le résultat retourné est un booléen permettant de savoir si l'utilisateur a réussi ou pas à trouver le mot-code
'''
def salle_De_Tresor():
    with open('indicesSalle.json', 'r', encoding='utf-8') as fichier:
        data = json.load(fichier)
    
    jeu_tv = data.get('jeu_tv', {})

    #Extraire les émissions associées à l'année choisie aléatoirement
    annees = list(jeu_tv.keys())
    annee = random.choice(annees)

    emissions = jeu_tv.get(annee, {})
    if not emissions:
        print(f"Aucune émission n 'existe pour l'année {annee}")
        return

    emission = random.choice(list(emissions.keys()))
    indices = emissions[emission].get('indices', [])
    mot_code = emissions[emission].get('mot_code', "")

    if len(indices) < 3:
        print(f"Moins de 3 indices sont disponibles pour l'émission {emission}")
        return

    print("Indices disponibles :")
    for i in range(3):
        print(f"Indice {i + 1}: {indices[i]}")

    essais = 3
    reponse_correcte = False

    while essais > 0:
        reponse = input("Entrez le mot-code : ").strip()

        #Vérifier que l'input ne soit pas vide
        if not reponse:
            print("Entrez un mot-code")
            continue
        
        if reponse.lower() == mot_code.lower():
            return(True)
        else:
            essais -= 1
            if essais > 0:
                print(f"Le mot-code saisi n'est pas bon. Il vous reste plus que {essais} essais")
                if essais <= len(indices) - 3:
                    print(f"Voici un indice supplémentaire : {indices[3 - essais]}")
            else:
                print("Le mot-code est faux. Vous n'avez plus d'essais")

    return(False)

