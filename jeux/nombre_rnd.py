import random

a = random.randint(1, 101)
compteur=1

while compteur<9:
    reponse = int(input("choisi un nombre entre 1 et 100?...."))

    if reponse == a :
        print("VICTOIRE")
        break
    elif reponse > a :
        print("trop haut")
    else :
        print("trop bas")

    compteur = compteur+1
 


print("tu a tenter", reponse, "la bonne reponse était", a)



# question = "choisi un nombre entre 1 et 10?....

# reponse = int(input(question))


# if reponse == a :
#     print("VICTOIRE")
# elif reponse > a :
#     print("trop haut")
# else :
#     print("trop_bas")
