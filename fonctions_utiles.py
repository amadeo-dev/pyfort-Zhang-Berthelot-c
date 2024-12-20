def introuduction():
    print("Bienvenue")
    print("Accomplir des épreuves pour gagner des clés et déverrouiller la salle du trésor.")
    print("L'objectif est de ramasser trois clés pour accéder à la salle du trésor.")

def composer_equipe():
    nbr_joueurs = 4
    while nbr_joueurs > 3:
        nbr_joueurs = int(input("Combien voulez vous inscrire de joueurs (max 3):"))
        if nbr_joueurs > 3:
            print("Erreur")

print(composer_equipe())

