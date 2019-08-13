'''
this script let you apply basic math operations as:
add, mult, divide, sustract
'''


#libraries####################################
import os
##############################################

#function#####################################
def calc(x, y, z):
    if z == 1 :
    Ans = x + y
    elif z == 2 :
    Ans = x - y
    elif z == 3 :
    Ans = x * y
    else :
    Ans = x / y 
    return Ans   

#Main#########################################
ni = int(input("First number: "))
n2 = int(input("Second number: "))
print(":::MENU:::)
print("[1]. Add")
print("[2]. Subs")
print("[3]. Mult")
print("[4]. Div")
opt = int(input("press an option: "))
print("The answer is: ",calc(n1,n2,opt)

