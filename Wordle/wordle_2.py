"""Wordle Game - Taylor Harrison a.k.a HACKERMAN"""
import random
import linecache
from colorama import init, Fore, Back, Style
from Colors_Class import colors

init(autoreset=False)
guess_count = 0
guess_limit = 5
out_of_guesses = False
word = ""
abcs = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def roll_dice(num):
    return random.randint(1, num)  # function to generate random number


secret_word_long = linecache.getline(
    r"C:\Users\harritx9\OneDrive - Abbott\Documents\Python_3.10\Wordle\wordle_answers.txt",
    roll_dice(213),
)
secret_word = secret_word_long[:-1]


def letter_check(word):  # function to assign a color to each letter
    for i in range(0, len(word)):
        if word[i] in secret_word and word[i] != secret_word[i]:
            print("\033[93m" + word[i], "\033[0m", end="")
        elif word[i] == secret_word[i]:
            print("\033[32m" + word[i], "\033[0m", end="")
        else:
            print(Style.RESET_ALL + (word[i]), end=" ")


# Function to see if the word entered is a valid word
def word_lookup(word):
    file = open(
        r"C:\Users\harritx9\OneDrive - Abbott\Documents\Python_3.10\Wordle\wordle_words.txt",
        "r",
    )
    wordle_file = file.readlines()
    word_newline = word + "\n"
    if word_newline in wordle_file:
        return True
    else:
        return False


def remaining_letters(word):
    for i in range(0, len(word)):
        if word[i] in abcs:
            abcs.remove(word[i])


while word != str(secret_word) and not (out_of_guesses):
    word = input("\033[38;5;43m\nEnter a 5 letter word: \033[0;0" + Style.RESET_ALL)
    if not word_lookup(word):
        print(
            "\033[38;5;34mWord must be a valid 5 letter word. \033[0;0"
            + Style.RESET_ALL
        )
    else:
        guess_count += 1
        letter_check(word)  # perform the letter coloring
        remaining_letters(word)
        print(Style.RESET_ALL + "\nRemaining Letters: ")
        print("  ".join(abcs))
    if guess_count == guess_limit:
        out_of_guesses = True

if word == secret_word:
    print(f"\033[32m" "\nYou win!" "\033[0m")
elif out_of_guesses and word != secret_word:
    print(f"\033[91m" "\nYou are out of guesses, you lose!" "\033[0m")
    print(
        colors.bg.lightgrey, colors.fg.orange, "The word is: " + secret_word, "\033[0m"
    )
