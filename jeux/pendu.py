import random

mot = ["yo", "moi", "voiture","janvier","rigoler","chintok","renoi","bouche"]
choix = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m","n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

pendu = (random.choice(mot))
# pendu = "moi"


mot_cache = ["_"] * len(pendu)
essai = len(pendu) + 6
rater = [] *essai

while essai > 0 :
    print("")
    print("le mot est", mot_cache)
    print("le nombre d'esseai restan est de", essai)
    print("lettre deja tester :", rater)
    tente = (input("tentative :")).lower()

    if tente in choix:
        print("lettre tenter ==",tente)
        print("")

    elif tente not in choix:
        print("1 seul lettre a taper")
        print("")
        continue

    if tente in pendu :
        ind = pendu.index(tente) #trouver l'index de tente dans pendu

        # mot_cache.replace(ind, tente)
        #remplacer "mot_cache" de la place de l'index par tente

        mot_cache[ind]=tente

    if tente not in pendu :
        rater.append(tente)
    essai = essai -1

    


