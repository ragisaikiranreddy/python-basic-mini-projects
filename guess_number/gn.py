import warnings
import random

# guess the number by taking feedback from computer
# x--> maxm number to be consider by computer
def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess!=random_number:
        guess = int(input(f"Guess the number between 1 and {x}: "))
        if guess<random_number:
            print("Sorry! its low, guess again")
        elif guess> random_number:
            print("Sorry! its high, guess again")
    print(f"congracts! you guessed the correct number its {random_number}")

guess(10)

