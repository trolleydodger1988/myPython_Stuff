secret_word = ("level")
word=print(input("Enter a word: "))

for i in range(0, len(word)):
    if (word[i] in secret_word and word[i] != secret_word[i]):
        print("\033[93m" + word[i], "\033[0m", end ="")
    elif word[i] == secret_word[i]:
        print("\033[32m" + word[i], "\033[0m", end ="")
    else:
        print("\033[0m" + (word[i]), "\033[0m", end =" ")