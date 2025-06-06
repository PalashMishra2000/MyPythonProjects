import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
       word = random.choice(word)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letters of the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user has guessed
   
    lives = 6
    #getting user input
    while len(word_letters) > 0 and lives > 0:
        
        print('You have', lives, 'lives remaining. You have used these letters: ',''.join(used_letters))
        
        # W - R D
        
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word : ',''.join(word_list))
        
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives-=1    
                
        elif user_letter in word_letters:
            print('You have already chosen that letter!')
        else:
            print('Invalid letter!')
    

hangman()