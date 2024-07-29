#Guessing game

import random
target= random.randint(1,100)
while True:
    a=input("Guess The Number or Enter (X) To Quit : ")
    if(a=="x"):
        break
    a=int(a)
    if(a==target):
        print("Congrts You Have Guessed Number")
        break
    elif(a<target):
        print("Enter Bigger Number ")
    else:
        print("Enter Smaller Number ")
print("#### Game Over ####")
