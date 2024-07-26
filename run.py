import gspread
from google.oauth2.service_account import Credentials
import random
from word import words_list

def random_word_selected():
    word = random.choice(word_list)
    return word.upper()

def game(word):
    guessed_word ="_" * len (word)
    guessed = False
    letters_guessed = []
    words_guessed = []
    tries = 6

    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(guessed_word)
    print ("/n")

    while not guessed and tries > 0:
        guess = input("Please guess a word or a letter")
        if len(guess) == 1 and guess.isalpha():
            if guess in letters_guessed:
                print ("You already guessed that letter", guess)
        elif guess not in word:
            print (f"{guess}is not in word")
            tries -=1
            letters_guessed.append(guess)

            words_list = list (guessed_word_state)
            indices = [i for i, letter is enumerate(word)if letter == guess] 
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
                            words_guessed.append(guess)
                            else:
                                guessed =True
                                guessed_word_state = word
                         else:
                            print("Not a valid guess")
                            print(display_hangman(tries)) 
                            print(guessed_word_state)
                            print("/n")
                        if guessed:
                            print("You win!")
                        else:
                            print ("You run out of tries. The word was" + word +.)

        def display_hangman(tries):
            stages = [#final state: head, torso, both arms, and both legs
            """

            ------
            |     |
            |     o
            |    \|/
            |     |
            |   // \\
            _
            """
            # head, torso, both arms, one leg
            
            """
             ------
            |     |
            |     o
            |    \|/
            |     |
            |   // 
            _

            """
            #head, torso, both arms
            """
              ------
            |     |
            |     o
            |    \|/
            |     |
            |   
            _
            """
            #head, torso, one arm
            """
              ------
            |     |
            |     o
            |    \|
            |     |
            |   
            _

            """
            #head, torso
            """
              ------
            |     |
            |     o
            |     |
            |     |
            |   
            _

            """
            #head

            """
            ------
            |     |
            |     o
            |     
            |     
            |   
            _

            """
            #initial state
            """
            ------
            |     |
            |     
            |     
            |     
            |   
            _
            ]
            return stages [tries]