'''
Cesmag University
Developer: Diego Felipe Zarama Jojoa
'''
#Libraries
import os
from random import randint

#This function lets generate the players number and level.
def main():
    global players, P
    players = randint(2,5)
    print("Players generated: ", players)
    level = randint(1,3)
    if level == 1 :
        P = 20
    elif level == 2 :
        P = 30
    else :
        P = 50
    print("Level: ", level)
    print("Positions: ", P)

def game():
    status = True
    suma = 0
    i = 1
    while status :
        os.system("clear")
        print("Press any key to game with Player ", i)
        KEY = ()
        D1 = randint(1,6)
        D2 = randint(1,6)
        T = D1 + D2
        print("D1: ", D1)
        print("D2: ", D2)
        suma += T
        print(f"Jugador {i} - Tirada: {T} Suma: {suma}")
        i = i + 1
        if i == players+1 :
            i = 1
        if suma >= P :
            print("¡You Win!")
            break

        KEY = input("Press any key to continue next player... ")

        if D1 == 1 and D2 == 1 :
            suma == 10
            if suma == 10 :
                suma += T
            print("You have advanved 10 more...")
        if D1 == 6 and D2 == 6 :
            suma == 5
            if suma == 5 :
                suma += T
            print("You have advanved 5 more...")

#main
os.system("clear")
print("::: WELCOME TO NUMBERS RIDE :::")
KEY = input("Press any key to generate config data ......")
main()
KEY = input("Press any key to play ......")
game()
