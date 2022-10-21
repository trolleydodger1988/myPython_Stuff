import random
import linecache
def roll_dice(num):
    return random.randint(1, num)
wordle_words = open("wordle_words.txt", "r")
secret_word = linecache.getline(r"C:\Users\harritx9\OneDrive - Abbott\Documents\Python_3.10\Wordle\wordle_words.txt", roll_dice(12972))
print(secret_word)