# Projet EFREI TI101 - Programmation en Python / Jacky
# fichier qui représente l'épreuve finale

import json
import random

#fonction de l'épreuve finale et qui renvoie vrai si l'utilisateur trouve la réponse a l'énigme
#et faux si l'utilisateur ne trouve pas la réponse en utilisant tous ses essais.

def salle_De_Tresor():

    # on pose les variables

    jeu_tv, emission = {},{}
    annee, mot_code = "", ""
    essais = 0
    reponse_correct = False

    # integrer le fichier .json en une liste de dico

    with open("data/indicesSalle.json", "r") as fichier:
        jeu_tv = json.load(fichier)

#permet de choisir l'énigme de façon aléatoire

    fort_boyard = jeu_tv["Fort Boyard"]
    annees = list(fort_boyard.keys())
    annee = random.choice(annees)
    emissions = fort_boyard[annee]
    emission_nom = random.choice(list(emissions.keys()))
    emission = emissions[emission_nom]
    indice = emission["Indices"]
    mot_code = emission["MOT-CODE"]

    print("Les indices sont :",indice[0],indice[1],indice[2])

    j = 2 # il va etre utiliser pour les indices
    essais = 3

# permet a l'utilisateur de répondre et de voir s'il a bon, s'il trouve la bonne réponse,
# réponse_correct = True

    while essais > 0 :
        reponse_joueur = input("Saisir la réponse : ")
        mot_code_mini = mot_code.lower()
        reponse_joueur_mini = reponse_joueur.lower()
        if mot_code_mini == reponse_joueur_mini :
            reponse_correct = True
            break
        else :
            essais -= 1
            if essais > 0:
                j += 1
                print("Il vous reste", essais, "essais")
                print("Le prochain indice est", indice[j])
            else :
                print("La réponse était :", mot_code)

#affiche si il a gagné ou perdu

    if reponse_correct == True :
        print("Vous avez gagné !")
    else :
        print("Vous avez perdu !")

