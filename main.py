from enigme_pere_fouras import *
from epreuves_logiques import *
from epreuve_finale import *
from epreuves_hasard import *
from epreuves_mathematiques import epreuves_mathematiques
from fonctions_utiles import *


def jeu():
    introduction()
    ekip = composer_equipe()
    cles = 0


    while cles < 3:
        epreuve_choisi = menu_epreuves()
        choisir_joueur(ekip)
        if epreuve_choisi == 1:
            epreuve_choisi = epreuves_mathematiques()
        if epreuve_choisi == 2:
            epreuve_choisi = jeu_bataille_navale()
        if epreuve_choisi == 3:
            epreuve_choisi = epreuves_hasard()
        if epreuve_choisi == 4:
            epreuve_choisi = enigme_pere_fouras()

        elif epreuve_choisi == True:
            cles += 1

    final = salle_De_Tresor()
    if final == True:
        "L'équipe remporte"
    else:
        "L'équipe perd"

jeu()