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
    with open('data/indicesSalle.json', 'r', encoding='utf-8') as fichier:
        data = json.load(fichier)
    
    jeu_tv = data.get('Fort Boyard', {})

    #Extraire les émissions associées à l'année choisie aléatoirement
    annees = list(jeu_tv.keys())
    annee = random.choice(annees)

    emissions = list(jeu_tv[annee].keys())
    emission = random.choice(emissions)

    #Extraire les indices et le mot-code pour l'émission choisie
    details_emission = jeu_tv[annee].get(emission, {})
    indices = details_emission.get("Indices", [])
    mot_code = details_emission.get("MOT-CODE", "")

    essais = 3
    reponse_correcte = False

    print("Bienvenue à l'épreuve finale. Les règles sont simples. Vous devez trouver le mot-code. Biensûr, on vous donnera des indices, un avant chaque essais. Vous avez 3 essais")
    print("Trouvez le mot-clé, et finissez le jeu .. ")

    print("\nIndices :")
    print(f"Indice 1 : {indices[0]}")
    print("Indice 2 : ...")
    print("Indice 3 : ...")

    while essais > 0:
        reponse = input("\nEntrez le mot-code : ").strip()

        if reponse.lower() == mot_code.lower():
            reponse_correcte = True
            break
        else:
            essais -= 1
            if essais > 0:
                print(f"Raté. Ce n'est pas le bon mot-code. Il vous reste {essais} essai(s)")
                print(f"Un indice supplémentaire pour vous aider : {indices[3 - essais]}")
            else:
                print("Encore raté. Vous n'avez plus d'essais c'est dommage")
                print(f"Le mot-code correct était : {mot_code}")
    
    if reponse_correcte:
        print("\nFélicitations !! Vous avez réussi à trouver le mot-code tellement rapidement. Vous pouvez accéder à la salle au trésor")
        return(True)
    else:
        print("\nC'était la dernière épreuve et vous échoué malheureusement")
        return(False)
