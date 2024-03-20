
#    ================================================================= Guess The Number ===========================================

import random


target = random.randint(1,100)


while True:
    userChoice = int(input("Guess the target :- "))
    if(userChoice == target):
        print("SUCESS : correct guess")
        break
    elif(userChoice < target):
        print("your number was small.. Think Bigger number ....")
    else:
        print("your number was Big.. Think Smaller number ....")
    
print("---------------Game Over ------------------------")