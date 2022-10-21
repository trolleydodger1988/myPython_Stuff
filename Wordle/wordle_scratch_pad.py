from collections import Counter

secret_word = "graph"
my_counter = Counter(secret_word)
print(my_counter)

word=input("Enter a word: ")

for i in range(0, len(word)):
    s_letter_count = secret_word.count(str(word[i]))
    letter_count = 0
    
    while letter_count < s_letter_count:
        if (word[i] in secret_word and word[i] != secret_word[i]):
            print("\033[93m" + word[i], "\033[0m", end ="")
            letter_count +=1
            
        elif (word[i] == secret_word[i]):
            print("\033[32m" + word[i], "\033[0m", end ="")
            letter_count +=1
            
        elif (word[i] in secret_word and word[i] != secret_word[i]):
            print("\033[93m" + word[i], "\033[0m", end ="")
            letter_count +=1

        else:
            print("\033[0m" + (word[i]), "\033[0m", end ="")
            letter_count +=1
            