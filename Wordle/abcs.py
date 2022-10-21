abcs = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
word = str("bigasswordlkjg")
for i in range(len(word)):
    if word[i] in abcs:
        abcs.remove(word[i])

print(abcs)