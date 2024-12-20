import json
import random

def salle_De_Tresor():

    #variable

    jeu_tv, emission = {},{}
    annee, mot_code = "", ""
    essais = 0
    reponse_correct = False

    # integrer le fichier .json en une liste de dico

    fichier = open("data/indicesSalle.json","r")
    jeu_tv = json.load(fichier)
    fichier.close()

    annee = random.choice(jeu_tv["annee"])
    emission = random.choice(annee["emission"])
    indice = emission["indice"]
    mot_code = emission["mot_code"]

    print(indice[0],indice[1],indice[2])

    j = 2 # il va etre utiliser pour les indices
    essais = 3

    while essais > 0 :
        reponse_joueur = input("Saisir la réponse : ")
        if mot_code == reponse_joueur:
            reponse_correct = True
            break
        else :
            if essais > 0:
                essais -= 1
                j += 1
                print(indice[j])
            else :
                print(mot_code)

    if reponse_correct == True :
        print("Vous avez gagné !")
    else :
        print("Vous avez perdu !")

salle_De_Tresor()
