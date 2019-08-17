#This is an exercise of random numbers
#Developer: Diego Zarama



#libraries####################################
import os
from random import randint, uniform, random
##############################################


#function#####################################

#this function generates integer numbers
def Z():
    AnsZ = randint(0,6)
    return AnsZ

i = 0
while i <= 6:
    print(Z())
    i = i + 1


###########################################