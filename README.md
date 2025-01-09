Jeu du Fort Boyard

1. **Présentation générale**


**Contributeurs**
NEGAI SAULIN Dényce
LAURENT Maxime

**Description**
Ce projet est un jeu base sur le jeu télévisé "Fort Boyard". Plusieurs épreuves doivent être accomplis pour gagner des clés et accéder à la salle du trésor

**Fonctionnalités principales**
    - Création d'une équipe de 1 à 3 joueurs pour participer aux jeux

    - Participation à des épreuves variées :
        - Mathématiques
        - Hasard
        - Logique
        - Énigmes du Père Fouras

    - Gestion de clés qui peuvent être gagnes pour accéder à l'épreuve finale du jeu

    - Epreuve finale finalisant le jeu

**Technologies utilisées**
    - Langage : Python
    - Bibliothèques : random, json

**Installation**
    - Dépôt Git : 
        - Installer Git sur votre appareil

        - Ouvrir un terminal de commande et éxécuter la ligne ci dessous : 
        git clone https://github.com/sanspseudo/pyfort-NegaiSaulinDenyce-LaurentMaxime-D2.git

    - Avoir Python installé sur votre appareil

**Utilisation**
    - Lancer le fichier main.py, le programme principal, et suivre le fil du jeu
    - Gagner des clés et finir l'épreuve finale pour gagner 





2. **Documentation technique**


**Algorithme du jeu**

    - Introduction : Message de bienvenue et énonciation des règles

    - Composition de l'équipe : L'utilisateur crée une équipe de joueurs de 1 à 3 joueurs

    - Boucle des épreuves :
        - L'utilisateur choisit un type d'épreuve
        - Un joueur se désigne à participer

    - Epreuve jouée : Si victoire, le joueur repart avec une clé

    - Épreuve finale : Découverte du mot-code pour accéder à la salle du trésor


**Détails des fonctions implémentées**

    - introduction() : Afficher un message de bienvenue et énonce les règles

    - composer_equipe() : Permettre de créer une équipe de joueurs et de leur attribuer un rôle de leader ou non

    - menu_epreuves() : Afficher les différentes épreuves et lancer celle choisie par l'utilisateur

    - choisir_joueur(equipe) : Sélectionner un joueur de l'équipe

    - epreuves : Les différentes fonctions d'épreuves

    - salle_De_Tresor() : Jouer l'épreuve finale


**Gestion des entrées et erreurs:**
Validation des saisies utilisateur pour qu'il n'y ai aucune erreur lors des saisies





3. **JOURNAL DE BORD**

**Chronologie du projet**

*Pendant les cours de python* :
Travail en collaboration : Création du repo git. Création complète des épreuves mathématiques et de hasard

*22 au 27 décembre* :
NEGAI SAULIN Dényce : Création de la première version de la bataille navale en 3x3
LAURENT Maxime : Finition des énigmes du père Fouras

*28 décembre au 2 janvier* :
NEGAI SAULIN Dényce : Finalisation fonctions utiles
LAURENT Maxime :  Finalisation épreuve finale

*3 au 4 décembre* :
NEGAI SAULIN Dényce : Modification de la bataille navale en 5x5 avec rajout de génération aléatoire de bateaux doubles
LAURENT Maxime : Finalisation du main

*5 janvier* :
Travail en collaboration : Correction des bugs, validation finale du projet





4. **Tests et Validation**

Stratégies de tests :
    - Tester toutes les saisies utilisateur possibles pour voir si il y des problèmes 
        Exemple : Dans toutes les entrées, si l'on appuie sur espace sans rien écrire, le programme redemandera à l'utilisateur d'entrer une nouvelle saisie
