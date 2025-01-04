# Projet EFREI TI101 - Programmation en Python
# Fort Boyard Simulator  / Amadéo
# Fichier qui représente les fonctions utiles tel que :
# la composition de l'équipe, le menu des épreuves...

#fonction qui introduit le début du jeu en renvoyant l'explication du jeu

def introduction():
    print("Bienvenue")
    print("Accomplir des épreuves pour gagner des clés et déverrouiller la salle du trésor.")
    print("L'objectif est de ramasser trois clés pour accéder à la salle du trésor.")

#fonction qui permet de composer les équipes et renvoie les informations des joueurs en une liste

def composer_equipe():
    nbr_joueurs = 4
    li_joueurs = []

    while nbr_joueurs > 3:
        nbr_joueurs = int(input("Combien voulez vous inscrire de joueurs (max 3) : "))
        if nbr_joueurs > 3 or nbr_joueurs <= 0:
            print("Erreur")

    for i in range(nbr_joueurs):
        new_joueur = { 'nom' :input("Nom du joueur : "),
                       'profession' : input('Sa profession : '),
                       'leader' : input('leader ? (o/n)'),
                       'cles_gagnees': 0 }
        li_joueurs.append(new_joueur)

    isleader = 0
    for i in range(len(li_joueurs)):
        if li_joueurs[i]['leader'] == 'o':
            isleader += 1
    if isleader == 0:
        li_joueurs[0]['leader'] = 'o'
    elif isleader > 1:
        for i in range(len(li_joueurs)):
            li_joueurs[i]['leader'] = 'n'
            li_joueurs[0]['leader'] = 'o'
    return li_joueurs

#fonction qui permet de demander a l'utilisateur de choisir l'epreuve et renvoie donc l'épreuve choisi

def menu_epreuves():
    print("\n1. Épreuve de Mathématiques\n2. Épreuve de Logique\n3. Épreuve du hasard\n4. Énigme du Père Fouras")
    choix = int(input("Choix: "))
    return choix

#fonction qui permet de choisir le joueur qui va jouer et renvoie donc la personne qui joue

def choisir_joueur(equipe):
    print('\n')
    for i in range(len(equipe)):
        if equipe[i]['leader'] == 'o':
            lead = 'Leader'
        else:
            lead = 'Membre'
        print("{}. {} ({}) - {}".format(i+1,equipe[i]['nom'],equipe[i]['profession'],lead))
    choix = int(input("Choix: "))
    return equipe[choix-1]

