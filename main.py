'''
pyfort-NegaiSaulinDényce-LaurentMaxime-D2
Auteurs:
    Negai Saulin Dényce
    Laurent Maxime
Rôle:
    Programme principal du jeu. Permettre de structurer le jeu
'''


import fonctions_utiles
import epreuves_mathematiques
import epreuves_hasard
import epreuves_logiques
import enigme_pere_fouras
import epreuve_finale


'''
Rôle:
    Rendu final du jeu
Résultat:
    Afficher du texte selon si l'équipe a gagné ou perdu le jeu
'''
def jeu():
    fonctions_utiles.introduction()
    equipe = fonctions_utiles.composer_equipe()
    cle = 0

    while cle < 3:
        choix_epreuve = fonctions_utiles.menu_epreuves()

        joueur = fonctions_utiles.choisir_joueur(equipe)

        if choix_epreuve == 1:
            print("\nVous avez selectionné le chiffre 1 : Epreuve de mathématiques\n\n")
            gagne = epreuves_mathematiques.epreuve_math()
        elif choix_epreuve == 2:
            print("\nVous avez selectionner le chiffre 2 : Epreuve de hasard\n\n")
            gagne = epreuves_hasard.epreuve_hasard()
        elif choix_epreuve == 3:
            print("\nVous avez selectionner le chiffre 3 : Epreuve de logique\n\n")
            gagne = epreuves_logiques.jeu_bataille_navale()
        elif choix_epreuve == 4:
            print("\nVous avez selectionner le chiffre 4 : Enigme du Père Fouras\n\n")
            gagne = enigme_pere_fouras.enigme_pere_fouras()
        
        if gagne is True:
            print(f"\n{joueur['nom']} a réussi l'épreuve {choix_epreuve}")
            cle += 1
            print(f"\nVous avez {cle}/3 clés")
        else:
            print(f"\n{joueur['nom']} a malheureusement echoué à l'epreuve {choix_epreuve}")
        
    print("\n\nBravo !! Votre équipe a collecté 3 clés. Vous pouvez participer à l'épreuve finale de notre émission\n\n")

    
    gagne = epreuve_finale.salle_De_Tresor()
    if gagne is True:
        print("\n\nVOUS AVEZ GAGNE LE JEU ET REMPORTEZ LE GRAND PRIX. VOUS AVEZ ETE EXCELLENT")
    else:
        print("\n\nVOUS AVEZ PERDU CETTE FOIS-CI MAIS VOUS POUVEZ RETENTER VOTRE CHANCE, VOUS ETIEZ SI PRES DU BUT")

     
jeu()
