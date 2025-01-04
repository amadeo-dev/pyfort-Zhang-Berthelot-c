# Projet EFREI TI101 - Programmation en Python
# Fort Boyard Simulator  / Amadéo
# Fichier qui représente les épreuves logiques

import random
import time

def suiv(joueur):
    if joueur == 0:
        return 1
    if joueur == 1:
        return 0

def grille_vide():
    return [[" " for i in range(3)] for i in range(3)]  #création d'une grille 3x3 en utilisant boucle for


def affiche_grille(grille, message):
    print(message)
    for ligne in grille:
        print("| " + " | ".join(ligne) + " |")  # on utilise la méthode join pour séparer par des '|' les cases
    print("-" * 15)


def demande_position():
    while True:
        position = input("Entrez la position (ligne,colonne) entre 1 et 3 (ex: 1,2) : ")
        if "," in position:
            ligne, colonne = position.split(',') # utilisation de la méthode split pour séparer le tuple position là où il y a une virgule
            ligne, colonne = int(ligne), int(colonne)
            if 1 <= ligne <= 3 and 1 <= colonne <= 3:
                return ligne - 1, colonne - 1
        print("Position invalide !")


def init():
    grille = grille_vide()

    print("Bateau 1")
    bateau1 = demande_position()
    grille[bateau1[0]][bateau1[1]] = 'B'

    while True:
        print("Bateau 2")
        bateau2 = demande_position()
        if bateau2 == bateau1:
            print("Position déjà occupée, veuillez choisir une autre position.")
        else:
            grille[bateau2[0]][bateau2[1]] = 'B'
            break

    affiche_grille(grille, "Découvrez votre grille de jeu avec vos bateaux :")

def tour(joueur, grille_tirs_joueur, grille_adversaire):
    if joueur == 0:
        print("C'est à votre tour de faire feu !:")
        affiche_grille(grille_tirs_joueur, "Rappel de l'historique des tirs que vous avez effectués :")
        tirl, tirc = demande_position()
        if grille_adversaire[tirl][tirc] == 'B':
            grille_tirs_joueur[tirl][tirc] = 'x'
            print("Touché coulé !")
        elif grille_adversaire[tirl][tirc] == ' ':
            grille_tirs_joueur[tirl][tirc] = '.'
            print("Dans l'eau...")

    if joueur == 1:
        print("\nC'est le tour du maître du jeu :")
        tirl, tirc = random.randint(0,2), random.randint(0,2)
        print('Le maître du jeu tire en position', tirl+1, ',', tirc+1)
        if grille_adversaire[tirl][tirc] == 'B':
            grille_tirs_joueur[tirl][tirc] = 'x'
            print("Touché coulé !")
            time.sleep(1)
        elif grille_adversaire[tirl][tirc] == ' ':
            grille_tirs_joueur[tirl][tirc] = '.'
            print("Dans l'eau...")

def gagne(grille_tirs_joueur):
    wincompte = 0
    wincompte = 0
    for ligne in grille_tirs_joueur:
        for case in ligne:
            if case == 'x':
                wincompte += 1
    if wincompte == 2:
        return True
    if wincompte < 2:
        return False

def jeu_bataille_navale():
    print("Chaque joueur doit placer 2 bateaux sur une grille de 3x3.")
    init()
    grille_moi, grille_maitre = grille_vide(), grille_vide()
    grille_tirs_moi, grille_tirs_maitre = grille_vide(), grille_vide()

    while True:
        bateau1 = (random.randint(0, 2), random.randint(0, 2))
        bateau2 = (random.randint(0, 2), random.randint(0, 2))
        if bateau1 != bateau2:
            break
    grille_maitre[bateau1[0]][bateau1[1]] = 'B'
    grille_maitre[bateau2[0]][bateau2[1]] = 'B'

    joueur = 0
    while True:
        if joueur == 0:
            tour(joueur,grille_tirs_moi, grille_maitre)
        elif joueur == 1:
            tour(joueur,grille_tirs_maitre, grille_moi)
        time.sleep(1)
        if gagne(grille_tirs_moi) == True:
            print("Le joueur a gagné !")
            return True

        joueur = suiv(joueur)
