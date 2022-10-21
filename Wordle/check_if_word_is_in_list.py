import linecache
file = open(r"C:\Users\harritx9\OneDrive - Abbott\Documents\Python_3.10\Wordle\wordle_words.txt", "r")
print(file.readable())
secret_word_long = linecache.getline(r"C:\Users\harritx9\OneDrive - Abbott\Documents\Python_3.10\Wordle\wordle_answers.txt", roll_dice(210))
secret_word = secret_word_long[:-1]
wordle_file = file.readlines()
word = str("dozen\n")
#print(wordle_file)
if word in wordle_file:
    print("It's there")