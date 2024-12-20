import json
import random

#fonction qui permet de changer un fichier .json en une liste de dictionnaire
def charger_enigmes(fichier):
    enigmes = open(fichier,'r')
    liste_dico_enigmes = json.load(enigmes)
    enigmes.close
    return liste_dico_enigmes

#fonction qui fait faire une énigme a l'utilisateur et
# qui renvoie true si il trouve la bonne réponse et false s'il le trouve pas
def enigme_pere_fouras():

    #variable utilisé

    liste_dico_enigmes = []
    enigmes1 = {}
    essais = 3

    # début fonction

    liste_dico_enigmes = charger_enigmes("data/enigmesPF.json")
    enigmes1 = random.choice(liste_dico_enigmes)
    print(enigmes1["question"])
    while essais > 0 :
        reponse = input("Saisir la réponse : ")
        reponse_miniscule = reponse.lower()
        if reponse_miniscule == enigmes1["reponse"].lower():
            print("La réponse est correct, vous avez gagné une clé.")
            return True
        else :
            print("La réponse n'est pas correct.")
            essais -= 1

        if essais == 0 :
            print("Le joueur a échoué a résoudre l'énigme.")
            return False





