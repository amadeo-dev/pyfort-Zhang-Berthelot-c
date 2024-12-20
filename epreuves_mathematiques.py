x
from math import *
import random

# fonction pour choisir l'épreuve de façon aléatoire,
# elle renvoie le nom de la fonction a appeler

def epreuves_mathematiques():
    epreuves = [epreuve_maths_factorielle,epreuve_maths_premier,epreuve_roulette_mathematique]
    epreuve = random.choice(epreuves)
    return epreuve()

# debut épreuve maths factorielle

# fonction pour trouver la factorielle de n

def factorielle(n):
    a = 1
    for i in range(1, n + 1):
        a *= i
        n = a
    return n

# fonction de l'epreuve factorielle de mathematique qui
# renvoie vrai ou faux si l'utilisateur arrive a trouvé la factorielle de n

def epreuve_maths_factorielle():
    c = 0
    import random
    n = random.randint(1,10)
    c = factorielle(n)
    d = int(input(f"Épreuve de Mathématiques: Calculer la factorielle de {n} : "))
    if c == d:
        print("Votre réponse :", d)
        print("Correct ! Vous gagnez une clé.")
        return True
    else :
        print("Votre réponse est :", d)
        print("Incorrect ! Vous avez raté l'épreuve.")
        return False

# fin épreuve maths factorielle

# debut epreuve premier

#foncion pour verifié si un nombre est premier

def est_premier(n):
    for i in range(2, int(sqrt(n)+1)):
        if n % i == 0 :
            return False
    return True

#fonction pour trouver le nombre premier le plus proche et au dessus de n

def premier_plus_proche(n):
    i = n+1
    a = False
    while a == False :
        a = est_premier(i)
        if a == True:
            return i
        else:
            i = i + 1

# fonction de l'épreuve mathématiques premier qui renvoie faux

def epreuve_maths_premier():
    import random
    n = random.randint(10,20)
    a = int(input(f"Épreuve de Mathématiques: Trouver le nombre premier le plus proche de {n} : "))
    b = premier_plus_proche(n)
    if a == b :
        print("Votre réponse :", a)
        print("Correct ! Vous gagnez une clé.")
        return True
    else :
        print("Votre réponse est :", a)
        print("Incorrect ! Vous avez raté l'épreuve !")
        return False

# fin epreuve maths premier

# début epreuve roulette mathématique,
# la fonction choisit une opération mathématiques et 5 chiffres aléatoirement et
# demande a l'utilisateur de calculer l'opération des 5 chiffres.

def epreuve_roulette_mathematique():
    import random
    operation = random.randint(1,3)
    a = random.randint(1,20)
    b = random.randint(1,20)
    c = random.randint(1,20)
    d = random.randint(1,20)
    e = random.randint(1,20)

    if operation == 1:
        op = "addition"
        reponse = a+b+c+d+e
    elif operation == 2:
        op = "soustraction"
        reponse = a-b-c-d-e
    elif operation == 3:
        op = "multiplication"
        reponse = a*b*c*d*e
    print("Nombres sur la roulette : [",a,",",b,",",c,",",d,",",e,"]")
    reponse_joueur = int(input(f"Calculez le résultat en combinant ces nombres avec une {op} :"))
    print("Votre réponse est : ",reponse_joueur)
    if reponse_joueur == reponse:
        print("Bonne réponse ! Vous avez gagné une clé. ")
        return True
    else :
        print("Mauvaise réponse ! Vous avez perdu l'épreuve.")
        return False

#fin epreuve roulette mathématique

print(epreuves_mathematiques())