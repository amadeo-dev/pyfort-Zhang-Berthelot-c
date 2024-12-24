def introuduction():
    print("Bienvenue")
    print("Accomplir des épreuves pour gagner des clés et déverrouiller la salle du trésor.")
    print("L'objectif est de ramasser trois clés pour accéder à la salle du trésor.")

def composer_equipe():
    nbr_joueurs = 4
    li_joueurs = []

    while nbr_joueurs > 3:
        nbr_joueurs = int(input("Combien voulez vous inscrire de joueurs (max 3):"))
        if nbr_joueurs > 3:
            print("Erreur")

    for i in range(nbr_joueurs):
        new_joueur = { 'nom' :input("Nom du joueur : "),
                       'profession' : input('Sa profession : '),
                       'leader' : input('leader ? (o/n)'),
                       'cles_gagnees': 0 }
        li_joueurs.append(new_joueur)

    isleader = False
    for i in range(len(li_joueurs)):
        if li_joueurs[i]['leader'] == 'o':
            isleader = True
    if isleader == False:
        li_joueurs[1]['leader'] = 'o'

    return li_joueurs

def menu_epreuves():
    print("1. Épreuve de Mathématiques\n2. Épreuve de Logique\n3. Épreuve du hasard\n4. Énigme du Père Fouras")
    return int(input("Choix: "))

def choisir_joueur(equipe):
    for i in range(1,len(equipe)+1):
        if equipe[i]['leader'] == 'o':
            lead = 'Leader'
        else:
            lead = 'Membre'

        print("{}. {} ({}) - {}".format(i,equipe[i]['nom'],equipe[i]['profession'],lead))


equipe = composer_equipe()
print(choisir_joueur(equipe))
