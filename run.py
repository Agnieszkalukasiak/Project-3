import gspread
from google.oauth2.service_account import Credetials
import random
from words import word_list

def get_word():
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_completion ="_" * len (word)