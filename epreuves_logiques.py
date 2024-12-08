
def suiv(joueur):
    if joueur == 0:
        return 1
    if joueur == 1:
        return 0


def grille_vide():
    return [[" " for i in range(3)] for i in range(3)]


def affiche_grille(grille, message):
    print(message)
    for ligne in grille:
        print("|" + "|".join(ligne) + "|")
    print("-" * 10)


def demande_position():
    position = input("Entrez la position (ligne,colonne) entre 1 et 3 (ex: 1,2) :")
    ligne, colonne = map(int, position.split(','))
    if 0 < ligne <= 3 and 0 <= colonne <= 3:
        return ligne-1, colonne-1
    else:
        print("Position invalide")


def init():
    grille = grille_vide()

    print("Bateau 1")
    bateau1 = demande_position()
    grille[bateau1[0]][bateau1[1]] = 'B'

    print("Bateau 2")
    bateau2 = demande_position() #faut pas que le deuxième bateau soit sur la même position que le premier
    grille[bateau2[0]][bateau2[1]] = 'B'

    affiche_grille(grille, "Découvrez votre grille de jeu avec vos bateaux :")

def tour(joueur, grille_tirs_joueur, grille_adversaire):

    affiche_grille(grille_jouer, "C'est à votre tour de faire feu !:")

def gagne(grille_tirs_joueur):
    pass

def jeu_bataille_navale():
    print("Chaque joueur doit placer 2 bateaux sur une grille de 3x3.")
    init()

