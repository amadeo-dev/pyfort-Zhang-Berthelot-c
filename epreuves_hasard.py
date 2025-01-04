# Projet EFREI TI101 - Programmation en Python
# Fort Boyard Simulator  / Amadéo
# Fichier qui represente les épreuves d'hasard

import random

def epreuves_hasard():
    """fontion choisissant au hasard parmi les jeux proposés dans la section des épreuves de hasard"""
    epreuves = [bonneteau, jeu_lance_des]
    epreuve = random.choice(epreuves)
    return epreuve()

#fonction qui du jeu bonneauteau et renvoie True s'il a reussi le jeu et False s'il a raté
def bonneteau():
    print(
        "Bienvenue au jeu du bonneteau ! Devinez sous quel bonneteau (A, B ou C) se cache la clé. Vous avez deux essais, bonne chance !")
    li = ('A','B','C')
    tentative = 2
    while tentative > 0:    # Boucle qui se repete 2 fois (nbr tentatives)
        bonnet = random.choice(li)
        print("Il vous reste", tentative, "essais")
        test = input("Choisir un bonneteau :").upper()   # demande et met en majuscule
        if test in li:                                   # vérifie si joueur a trouvé
            if test == bonnet:
                print("La clé a été trouvée sous le bonneteau")
                return True
            else:
                print("Le joueur n'a pas réussi la tentative")
        else:
            print("Choix Invalide")
        tentative -= 1
    print("Le joueur a perdu, la clé se trouvait sous le bonneteau", bonnet)
    return False

#fonction qui représente le jeu de lancé de dé et renvoie true s'il gagne et false s'il perd

def jeu_lance_des():
    essais = 3
    while essais > 0:
        print("Il vous reste", essais, "essais")
        input("Appuyez sur Entrée pour lancer les dés...")
        de1 = (random.randint(1, 6), random.randint(1, 6) )  
        print(f"Vous avez obtenu : {de1[0]} et {de1[1]}.")
        for i in de1:
            if i == 6:
                print("Le joueur a remporté la partie et la clé")
                return True

        de2 = (random.randint(1, 6), random.randint(1, 6))
        print(f"Le maître du jeu a obtenu : {de2[0]} et {de2[1]}.")
        for i in de2:
            if i == 6:
                print("le maître du jeu a remporté la partie")
                return False
        print("On passe au prochain essai")
        essais -=1
    print("Personne n'a emporté la partie")
    return False

