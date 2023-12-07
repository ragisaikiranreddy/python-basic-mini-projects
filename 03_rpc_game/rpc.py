import random

def game():
    # user = input("choose 'r' for rock, 'p' for paper and 's' for scissors: \n")
    user ='r'
    computer = random.choice(['r','p','s'])
    print(user,computer)

    if user == computer:
        print("It's a tie game!")
        game()
    

    # r>s or s>p or p>r
    if is_win(user,computer):
        return 'you wins!'
    
    return "you lost!"
        

def is_win(player,opponent):
    if (player=='r' and opponent =='s' ) or \
       (player=='s' and opponent =='p' ) or \
       (player=='p' and opponent =='r' ):
        return True

print(game())