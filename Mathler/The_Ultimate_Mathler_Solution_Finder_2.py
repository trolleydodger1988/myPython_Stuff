from itertools import product

# list all the operators as string
o = ["+", "-", "*", "/"]
# list all the numbers as strings
n = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

# prompt user for the "Mathler" number
mathler: int = int(input("Input the Mathler number: "))
print("Calculating - this might take a while...")

# create a list of all possible combinations of sequence "nnonon" and reapeat for other sequence combinations ᕦ(ò_óˇ)ᕤ
prod_nnonon = list(product(n, n, o, n, o, n, repeat=1))
prod_nnnonn = list(product(n, n, n, o, n, n, repeat=1))
prod_nonnon = list(product(n, o, n, n, o, n, repeat=1))
prod_nononn = list(product(n, o, n, o, n, n, repeat=1))
prod_nnonnn = list(product(n, n, o, n, n, n, repeat=1))
prod_nonnnn = list(product(n, o, n, n, n, n, repeat=1))
prod_nnnnon = list(product(n, n, n, n, o, n, repeat=1))

my_list = []
new_list = []
new_list_1 = []


def find_list(num_list):
    for i in range(len(num_list)):  # run through each index in the list
        # create a list of strings for the ith index in the list
        my_list = [
            num_list[i][0],
            num_list[i][1],
            num_list[i][2],
            num_list[i][3],
            num_list[i][4],
            num_list[i][5],
        ]
        # join the list of strings into a string
        my_string = "".join(my_list)
        try:
            # evaluate the list of strings as an equation
            answer = eval(my_string)
        except ZeroDivisionError:  # ignore divide by zero error
            pass
        except SyntaxError:  # ignore syntax errors like '8+04*7'
            pass
        if answer == mathler:
            # if the evaluation is equal to the Mathler number, then create a new list with the ith index in the num_list
            new_list.append(num_list[i])
    # return the list of strings that satify the equation
    return new_list


def known_position(char, position, num_list):
    new_list_1 = []
    for i in range(len(num_list)):  # run through each index in the list
        # if any of the lists has the char at the specified position, add to this new list
        if num_list[i][position] == char:
            new_list_1.append(num_list[i])  #
    return new_list_1  #


# Function that removes list items if any of those characters are not contained with the num_list
def does_not_contain(char, num_list):
    new_list_2 = []
    for i in range(len(num_list)):
        if char not in num_list[i]:
            new_list_2.append(num_list[i])
    return new_list_2


# Function that removes list items if any of those characters are contained with the num_list
def does_contain(char, num_list):
    new_list_3 = []
    for i in range(len(num_list)):
        if char in num_list[i]:
            new_list_3.append(num_list[i])
    return new_list_3


# run the find_list function for each sequence nnonon, nnnonn, etc...
find_list(prod_nnonon)
find_list(prod_nnnonn)
print("(￣o￣) . z Z")
find_list(prod_nonnon)
find_list(prod_nononn)
print("(￣O￣) . z Z")
find_list(prod_nnonnn)
find_list(prod_nonnnn)
print("(￣o￣) . z Z")
find_list(prod_nnnnon)

# print that mother
# print(f"There are {len(new_list)} possible solutions: \n{new_list}")

# num_list_1 = known_position("6", 0, new_list)       # use this function to speciy what chars and what index to return from the master list

redu_list = []
redu_set = set()
char_list = ["0", "1", "3", "6", "7", "8", "9", "+", "*"]


# new_red_list = does_not_contain("7", does_contain("/",does_contain("4",new_list)))
# print(new_red_list)
# print(f"There are {len(new_red_list)} possible solutions: \n{new_red_list}")
# new_list_13 = does_contain("/", does_contain("8", does_contain("+", new_list)))

# new_list_131 = does_not_contain("4", does_not_contain("1", does_not_contain("9", new_list_13)))
# print(new_list_131)
