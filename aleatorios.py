#Developer: Diego Zarama
#Números aleatorios

#Libraries###################################
import os
from random import randint, uniform, random

#function####################################

#this function generates integer numbers
def Z():
    AnsZ = randint(0,100)
    return AnsZ


N = Z():
i = 1
while i <= N :
    print(i)
    i = i+1
if N <= 0:
    print("The number is: ", N)
#Main######################################
os.system("clear")
print("The integer random number is: ", Z())

