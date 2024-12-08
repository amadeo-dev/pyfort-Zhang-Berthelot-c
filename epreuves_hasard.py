import random

def epreuves_hasard():
    epreuves = [bonneteau, jeu_lance_des]
    epreuve = random.choice(epreuves)
    return epreuve()


def bonneteau():
    print(
        "Bienvenue au jeu du bonneteau ! Devinez sous quel bonneteau (A, B ou C) se cache la clé. Vous avez deux essais, bonne chance !")
    li = ('A','B','C')
    tentative = 2
    while tentative > 0:
        bonnet = random.choice(li)
        print("Il vous reste", tentative, "essais")
        test = input("Choisir un bonneteau :").upper()
        if test in li:
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

print(epreuves_hasard())