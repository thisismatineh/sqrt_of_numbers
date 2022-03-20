#Matineh Mousavi
from decimal import *
# to get number between 10 & 100
print("Please enter a number between 10 and 100")
while True:
    x=int(input("x= "))
    if x > 10 and x < 100:
        break
    else:
        print("try again!")
# to get decimal number(in this situation, we use number "50" due to the question)
print("Decimal number")
dec=int(input("decimal = "))
# we use getcontext function with Decimal in decimal module to print 
# decimal numbers due to "dec"
getcontext().prec = dec
# to get sqrt of "x" we use multiply (**) instead of sqrt()
print("Answer: ",Decimal(x)**(Decimal(0.5)))