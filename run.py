import gspread
from google.oauth2.service_account import Credetials
import random
from words import word_list

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

while not guessed and tries > 0 :
    guess = input("please guess a word or a letter:").upper()