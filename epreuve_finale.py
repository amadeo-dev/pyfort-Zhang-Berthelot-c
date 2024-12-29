import json
import random

def salle_De_Tresor():

    #variable

    jeu_tv, emission = {},{}
    annee, mot_code = "", ""
    essais = 0
    reponse_correct = False

    # integrer le fichier .json en une liste de dico

    with open("data/indicesSalle.json", "r") as fichier:
        jeu_tv = json.load(fichier)

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

    if reponse_correct == True :
        print("Vous avez gagné !")
    else :
        print("Vous avez perdu !")

salle_De_Tresor()
