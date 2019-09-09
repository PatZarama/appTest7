'''
This is a fibonacci serie, showing the first 20 caracters
Developer: Diego Felipe Zarama Jojoa
'''
#Library
import os

#fibonacci  serie
def fi_seq(n):
    a = 0
    b = 1

    if n == 1:
        print(a)
    elif n == 2:
        print(a,b)
    else:
        print("•",a,b, end = "\n")
        for i in range (n-2):
            c = a + b
            a = b
            b = c
            print("•",b, end = "\n")

os.system("clear")
fi_seq(20)
