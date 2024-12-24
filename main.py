from enigme_pere_fouras import *
from epreuves_logiques import *
from epreuve_finale import *
from epreuves_hasard import *
from epreuves_mathematiques import epreuves_mathematiques
from fonctions_utiles import *

cles = 0

def jeu():
    introduction()
    ekip = composer_equipe()
    while cles < 3:
        epreuve_choisi = menu_epreuves()
        choisir_joueur(ekip)
        if epreuve_choisi == '1':
            epreuves_mathematiques()
        if epreuve_choisi == '2':
            epreuves_logiques()
        if epreuve_choisi == '3':
            epreuves_hasard()
        if epreuve_choisi == '4':
            enigme_pere_fouras()


if __name__ == "__main__":
    jeu()
