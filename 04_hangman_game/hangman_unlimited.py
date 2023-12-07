import random
import string
from words import words

def get_valid_word(words):
    word = random.choice(words)
    while '_' in word or ' ' in word or '-' in word:
        word = random.choice(words)
    return word.upper()

# keep track which letters we guessed
#which letters we correctly guessed
#what is valid letter and what is invalid letter


# hangman with unlimited lifes
def hangman():
  
    word = get_valid_word(words)  
    # print(word)
    word_letters = set(word)       # set of all letters of the word chosen
    alphabet = set(string.ascii_uppercase)  # set of all 26 capital letters
    used_letters =set()
 
    while len(word_letters) >0:

        # used letters
        # ' '.join(used_letters) --> [A J N]
        print('Used letters: ',' '.join(used_letters))

        #current state of word
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('current word: ',' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        
        elif user_letter in used_letters:
            print("you have already guessed this letter. guess again!")
        else:
            print("invalid input. guess again")
        print('-------------------------')
    
    # final_word = [letter if letter in used_letters else '_' for letter in word]
    # print('guessed correctly! ',' '.join(final_word))
    print('congracts! you guessed correctly!. It is: ',word)

    print('*--------------------------------------*')

hangman()



