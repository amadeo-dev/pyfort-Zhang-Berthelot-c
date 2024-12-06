from math import *
import random
def epreuve_maths():
    pass

# début épreuve maths factorielle :

def factorielle(n):
    a = 1
    for i in range(1, n + 1):
        a *= i
        n = a
    return n
def epreuve_maths_factorielle():
    c = 0
    n = random.randint(1,10)
    c = factorielle(n)
    d = int(input(f"Épreuve de Mathématiques: Calculer la factorielle de {n} : "))
    if c == d:
        print("Votre réponse :", d)
        print("Correct ! Vous gagnez une clé.")
        return True
    else :
        print("Votre réponse est :", d)
        print("Incorrect ! Vous avez raté l'épreuve de mathématiques.")
        return False

# fin épreuve maths factorielle

# début épreuve des nombres premiers ( moyenne ):

def est_premier(n):
    for i in range(2 , int(sqrt(n))+1):
            if n % i == 0 :
                return False
    return True

def premier_plus_proche(n):
    i = n+1
    a = False
    while a == False :
        a = est_premier(i)
        if a == True :
            return i
        else :
            i = i + 1

def epreuve_math_premier():
    n = random.randint(10,20)
    a = int(input("Épreuve de Mathématiques: Trouver le nombre premier le plus proche


jgkiufyiyi