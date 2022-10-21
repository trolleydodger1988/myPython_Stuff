from itertools import product

#o = ["+","-","*","/"]                                       # list all the operators as string
o = ["*","/"] 
n = ["0","1","2","3","4","5","6","7","8","9"]               # list all the numbers as strings

mathler = int(input("Input the Mathler number: "))          # prompt user for the "Mathler" number

prod_nnonon = list(product(n,n,o,n,o,n, repeat=1))          # create a list of all possible combinations of sequence "nnonon" and reapeat for other sequence combinations
prod_nnnonn = list(product(n,n,n,o,n,n, repeat=1))
prod_nonnon = list(product(n,o,n,n,o,n, repeat=1))
prod_nononn = list(product(n,o,n,o,n,n, repeat=1))
prod_nnonnn = list(product(n,n,o,n,n,n, repeat=1))
prod_nonnnn = list(product(n,o,n,n,n,n, repeat=1))
prod_nnnnon = list(product(n,n,n,n,o,n, repeat=1))

my_list = []
new_list = []

def find_list(num_list):
    for i in range(len(num_list)):    # run through each index in the list      
        my_list = [num_list[i][0],num_list[i][1],num_list[i][2],num_list[i][3],num_list[i][4],num_list[i][5]]   # create a list of strings for the ith index in the list
        my_string = ''.join(my_list)        # join the list of strings into a string
        try:
            answer = eval(my_string)        # evaluate the list of strings as an equation
            if answer == mathler:
                new_list.append(num_list[i])    # if the evaluation is equal to the Mathler number, then create a new list with the ith index in the num_list
        except ZeroDivisionError:               # ignore divide by zero error
            pass
        except SyntaxError:                     # ignore syntax errors like '8+04*7'
            pass
    return new_list                             # return the list of strings that satify the equation
# run the find_list function for each sequence nnonon, nnnonn, etc...
find_list(prod_nnonon)
find_list(prod_nnnonn)
find_list(prod_nonnon)
find_list(prod_nononn)
find_list(prod_nnonnn)
find_list(prod_nonnnn)
find_list(prod_nnnnon)
print(f"There are {len(new_list)} possible solutions: \n{new_list}")        # print that mother