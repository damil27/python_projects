import random


def rollingdice():
    while True:
        choice = input("ROll a dice (yes/no): ")
        if choice.lower() == "yes":
            die1 = random.randint(1, 6)
            die2 = random.randint(1, 6)
            print(f"Die 1: {die1}, Die 2: {die2}")
        elif choice.lower() == "no":
            print("Thanl you")
            break
        else:
            print("Invalid input, please enter 'yes' or 'no'")


rollingdice()
