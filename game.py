

import random
def game():
    secreate_number = random.randint(1, 100)
    attempt = 1
    while attempt <=7:
        x = int(input("enter the no"))
        if x > secreate_number:
            print("lower ")

        elif x<secreate_number:
            print("higher ")

        else:
            print("correct")
            break
        attempt = attempt + 1
    else:
        # this runs only if the while loop finished WITHOUT breaking (i.e. ran out of attempts)
        print(f"Out of attempts! The number was {secreate_number}.")


while True:
    game()
    again=input("play again(yes/no):")
    if again.lower== "yes":
        continue
    else:
        break





