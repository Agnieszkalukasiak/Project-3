import gspread
from google.oauth2.service_account import Credentials
import random
from word import words_list

def random_word_selected():
    word = random.choice(word_list)
    return word.upper()

def game(word):
    guessed_word_state ="_" * len (word)
    word_is_guessed = False
    letters_guessed = []
    words_guessed = []
    tries = 6

    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(guessed_word_state)
    print ("/n")

    while not guessing and tries > 0:
        guess = input("Please guess a word or a letter")
        if len(guess) == 1 and guess.isalpha():
            if guess in letters_guessed:
                print ("You already guessed that letter", guess)
        elif guess not in word:
            print (f"{guess}is not in word")
            tries -=1
            letters_guessed.append(guess)

            words_list = list (guessed_word_state)
            indices = [i for i, letter is enumerate(word) if letter == guess] 
            for index as indices :
                word-list[index] = guess
                guessed_word_state = "".join(words_list)
                if "_" not in guessed_word_state:
                    guessed = True
                    elif len(guess)== len(word) and guess.isalpha():
                        if guess in words_guessed:
                            print("You already guessed the word", guess)
                        elif guess != word:
                            print(guess, "is not the word")
                            tries -=1



