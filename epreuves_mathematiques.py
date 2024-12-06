def epreuve_maths():
    pass

def factorielle(n):
    a = 1
    for i in range(1, n + 1):
        a *= i
        n = a
    return n

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
        print("Incorrect ! Vous avez raté l'épreuve de mathématiques.")
        return False

