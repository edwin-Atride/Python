
import random

choix = ["ciseaux", "pierre", "feuille"]

pierre = 1
ciseaux = 2
feuille = 3

# compteur=1
# while compteur<4:
#     ordinateur = (random.randint(1, 3))
#     choix = ["ciseaux", "pierre", "feuille"]

#     while True:
#         utilisateur = input("Choisissez entre ciseaux, pierre ou feuille : ").lower()
#      if utilisateur in choix:
#         print("Vous avez choisi"  ,  utilisateur)
#         break  
#     else:
#         print("Pierre, feuille ou ciseaux c'est pas compliquer?.")


#     if ordinateur == 2:
#         print("L'ordinateur a choisi : ciseaux")
#     elif ordinateur == 1:
#         print("L'ordinateur a choisi : pierre")
#     else:
#         print("L'ordinateur a choisi : feuille")


#     if ordinateur == 2 and utilisateur == "ciseaux":
#         print("bien jouer mais egaliter il faut recommencer")
#     elif ordinateur == 2 and utilisateur == "pierre":
#         print("Bien jouer c'est GAGNER")
#         break
#     elif ordinateur == 2 and utilisateur == "feuille":
#         print("Dommage c'est la defaite")

#     if ordinateur == 3 and utilisateur == "feuille":
#         print("bien jouer mais egaliter il faut recommencer")
#     elif ordinateur == 3 and utilisateur == "ciseaux":
#         print("Bien jouer c'est GAGNER")
#         break
#     elif ordinateur == 3 and utilisateur == "pierre":
#         print("Dommage c'est la defaite")

#     if ordinateur == 1 and utilisateur == "pierre":
#         print("bien jouer mais egaliter il faut recommencer")
#     elif ordinateur == 1 and utilisateur == "feuille":
#         print("Bien jouer c'est GAGNER")
#         break
#     elif ordinateur == 1 and utilisateur == "ciseaux":
#         print("Dommage c'est la defaite")
# compteur=compteur+1
    



ordinateur = (random.randint(1, 3))

while True:
    utilisateur = input("Choisissez entre ciseaux, pierre ou feuille : ").lower()
    if utilisateur in choix:
        print("Vous avez choisi"  ,  utilisateur)
        break  
    else:
        print("Pierre, feuille ou ciseaux c'est pas compliquer?.")


if ordinateur == 2:
    print("L'ordinateur a choisi : ciseaux")
elif ordinateur == 1:
    print("L'ordinateur a choisi : pierre")
else:
    print("L'ordinateur a choisi : feuille")


if ordinateur == 2 and utilisateur == "ciseaux":
    print("bien jouer mais egaliter il faut recommencer")
elif ordinateur == 2 and utilisateur == "pierre":
    print("Bien jouer c'est GAGNER")
elif ordinateur == 2 and utilisateur == "feuille":
    print("Dommage c'est la defaite")

if ordinateur == 3 and utilisateur == "feuille":
    print("bien jouer mais egaliter il faut recommencer")
elif ordinateur == 3 and utilisateur == "ciseaux":
    print("Bien jouer c'est GAGNER")
elif ordinateur == 3 and utilisateur == "pierre":
    print("Dommage c'est la defaite")

if ordinateur == 1 and utilisateur == "pierre":
    print("bien jouer mais egaliter il faut recommencer")
elif ordinateur == 1 and utilisateur == "feuille":
    print("Bien jouer c'est GAGNER")
elif ordinateur == 1 and utilisateur == "ciseaux":
    print("Dommage c'est la defaite")








