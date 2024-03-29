from random import randint

answer = str(input("Please enter YES to roll or anything else to end the program: "))
while answer.upper() == "YES":
    dice_roll = randint(1, 6)
    print(dice_roll)
    answer = str(input("Please enter YES to roll or anything else to end the program: "))

    

