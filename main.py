# Projet EFREI TI101 - Programmation en Python
# Fort Boyard Simulator  / Amadéo
# Fichier qui represente le fichier principal dans lequel l'utilisateur va jouer

from enigme_pere_fouras import *
from epreuves_logiques import *
from epreuve_finale import *
from epreuves_hasard import *
from epreuves_mathematiques import *
from fonctions_utiles import *


def jeu():
    introduction()
    ekip = composer_equipe()    #présentation et création des équipes
    cles = 0                    # initialisation du nombre de clés à 0

    while cles < 3:             # On répète tant que l'équipe n'a pas trois clés
        epreuve_choisi = menu_epreuves()
        joueur_choisi = choisir_joueur(ekip)

        if epreuve_choisi == 1:
            epreuve_choisi = epreuves_mathematiques()
        if epreuve_choisi == 2:
            epreuve_choisi = jeu_bataille_navale()
        if epreuve_choisi == 3:
            epreuve_choisi = epreuves_hasard()
        if epreuve_choisi == 4:
            epreuve_choisi = enigme_pere_fouras()

        elif epreuve_choisi == True:
            joueur_choisi['cles_gagnees'] += 1
            cles += 1

    print("L'épreuve de la Salle au trésor commence !")
    final = salle_De_Tresor()  # une fois les 3 clés obtenues -> salle tresor
    if final == True:
        "L'équipe remporte"
    else:
        "L'équipe perd"

jeu()