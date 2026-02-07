#def ligne():
#    print("___|___|___")
#    print("___|___|___")
#    print("   |   |   ")
#ligne()


choixl1 = [" "," "," "]
choixl2 = [" "," "," "]
choixl3 = [" "," "," "]


def play():

    print(choixl1)
    print(choixl2)
    print(choixl3)

    j1=int(input("j1 ou joue tu(O) ? 1/2/3/4/5/6/7/8/9 : "))

    if j1 == 1:
        choixl1[0] = "O"
    elif j1 == 2:
        choixl1[1] = "O"
    elif j1 == 3:
        choixl1[2] = "O"

    if j1 == 4:
        choixl2[0] = "O"
    elif j1 == 5:
        choixl2[1] = "O"
    elif j1 == 6:
        choixl2[2] = "O"
    
    if j1 == 7:
        choixl3[0] = "O"
    elif j1 == 8:
        choixl3[1] = "O"
    elif j1 == 9:
        choixl3[2] = "O"

    j2=int(input("j2 ou veut tu jouer?(X) 1/2/3/4/5/6/7/8/9 : "))

    if j2 == 1:
        choixl1[0] = "X"
    elif j2 == 2:
        choixl1[1] = "X"
    elif j2 == 3:
        choixl1[2] = "X"

    if j2 == 4:
        choixl2[0] = "X"
    elif j2 == 5:
        choixl2[1] = "X"
    elif j2 == 6:
        choixl2[2] = "X"
    
    if j2 == 7:
        choixl3[0] = "X"
    elif j2 == 8:
        choixl3[1] = "X"
    elif j2 == 9:
        choixl3[2] = "X"
    



def morpion():
    compteur=0
    case=9
    while compteur < case:
        play()
        

morpion()

