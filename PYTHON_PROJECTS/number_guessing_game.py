import random

number = random.randint(1,10)

chance = 0 
max_chance = 5

while chance <= max_chance:
    chance +=1
    try:
        gusse = int(input("enter your number :"))

    except ValueError:
        print("please enter a valid number ")

    if gusse > number :
        print("try lower number....")

    elif gusse < number:
        print("Try bigger number...")

    elif gusse == number :
        print("you won...")
        print(f"you win the game in {chance} try")
        break

    if chance == max_chance and gusse != number:
        print(f"game over\n you have used all moves\n the correct number is {number}")
