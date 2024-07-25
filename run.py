import gspread
from google.oauth2.service_account import Credetials
import random
from words import word_list

def random_word_selected():
    word = random.choice(word_list)
    return word.upper()

def game(word):
    guessed_word_state ="_" * len (word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    