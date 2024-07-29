
import random
from words import words_list
from colorama import init, Fore

def random_word_selected():
    word = random.choice(words_list)
    return word.upper()

def game(word):
    guessed_word ="_" * len(word)
    guessed = False
    letters_guessed = []
    words_guessed = []
    tries = 6

    print(Fore.RED + "Let's play!")
    print(hangman(tries))
    print(guessed_word)
    print ("\n")

    while not guessed and tries > 0:
        guess = input("Guess a word or a letter:").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in letters_guessed:
                    print(Fore.RED + "You already guessed that letter", guess)
            elif guess not in word:
                print(Fore.RED + guess, "is not in word")        
                tries -= 1
                letters_guessed.append(guess)
            else: 
                print(Fore.GREEN + "You did it!", guess, " is in the word")
                letters_guessed.append(guess)
                letter_list = list(guessed_word)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    letter_list[index] = guess
                guessed_word = "".join(letter_list)
            if "_" not in words_guessed:
                guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in words_guessed:
                print(Fore.RED + "You already guessed the word", guess)
            elif guess.lower() != word.lower():
                print(Fore.RED + guess, "is not in the word")
                tries -= 1
                words_guessed.append(guess)
            else: 
                guessed = True
                guessed_word = word
        else:
            print("Not a valid guess")
        print(hangman(tries)) 
        print(guessed_word)
        print("\n")
    if guessed:
        print("You win!")
    else:
        print ("You run out of tries. The word was" + word +".")

def hangman(tries):
    stages = [
        #final state: head, torso, both arms, and both legs
            """
            ------
            |     |
            |     o
            |    \|/
            |     |
            |    / \
            _
            """,
            #head, torso, both arms, one leg   
            """ 
             ------
            |     |
            |     o
            |    \|/
            |     |
            |    / 
            _
            """,
            #head, torso, both arms
            """
              ------
            |     |
            |     o
            |    \|/
            |     |
            |   
            _
            """,
            #head, torso, one arm
            """
              ------
            |     |
            |     o
            |    \|
            |     |
            |   
            _
            """,
            #head, torso
            """
              ------
            |     |
            |     o
            |     |
            |     |
            |   
            _
            """,
            #head
            """
            ------
            |     |
            |     o
            |     
            |     
            |   
            _
            """,
            #initial state
            """
             ------
            |     |
            |     
            |     
            |     
            |   
            _
            """
    ]
    return stages[tries]

def main():
        word = random_word_selected()
        game(word)
        while input ("Want to play again? (Y/N)").upper()== "Y":
            main()
               
if __name__ == "__main__":
    inti(autoreset=True)
    main()