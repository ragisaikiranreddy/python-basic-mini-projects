import warnings
import random

# computer guess the number by taking feedback from us
# x--> maxm number computer should guess within

def guess_comp(x):
    # number = int(input(f"fix a number to guess by comp: "))
    low  = 1
    high = x
    feedback = ''
    while feedback !='c':
        if low<high:
            guess = random.randint(low,high)
        elif low>high:
            print(f"low is: {low}, high is {high}. so, can't guess a number.\n your feedback was incorrect!")
            return
        else:
            print(f"low =high value is {low}")
            guess = low # can also be high
        feedback = input(f"I guess it as {guess}! Is it high(h), low(l) or i guessed it correctly(c) ??: ")
        if feedback=='l':
            print(f"so, comp {guess} as is low, let me guess again!")
            low = guess+1
        elif feedback=='h':
            print(f"so, comp {guess} as is high, let me guess again!")
            high = guess-1
    print(f"yay! comp guessed its correctly as {guess}")

guess_comp(100)



# def guess_comp():
#     number = int(input(f"fix a number to guess by comp: "))
#     guess = 0
#     low  = 1
#     high = 2*number
#     while guess!=number:
#         guess = random.randint(low,high)
#         print(f"I guess it maybe {guess}!")
#         if guess<number:
#             print(f"{guess} is low, guess again!")
#             low = guess+1
#         elif guess>number:
#             print(f"{guess} is high, guess again!")
#             high = guess-1
#     print(f"comp guessed its correctly as {guess}")



# guess_comp(input(f"fix a number to guess by computer: "))
