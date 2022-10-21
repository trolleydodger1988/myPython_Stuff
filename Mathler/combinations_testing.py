from itertools import *

o = ["+","-","*","/"]                                       # list all the operators as string
n = ["0","1","2","3","4","5","6","7","8","9"]               # list all the numbers as strings

mathler = int(input("Input the Mathler number: "))          # prompt user for the "Mathler" number

prod_nnonon = list(product(n,n,o,n,o,n, repeat=1))          # create a list of 

prod_nnnonn = list(product(n,n,n,o,n,n, repeat=1))

prod_nonnon = list(product(n,o,n,n,o,n, repeat=1))

prod_nononn = list(product(n,o,n,o,n,n, repeat=1))

my_list = []
new_list = []

def find_list(num_list):
    for i in range(len(num_list)):
        my_list = [num_list[i][0],num_list[i][1],num_list[i][2],num_list[i][3],num_list[i][4],num_list[i][5]]
        my_string = ''.join(my_list)
        try:
            answer = eval(my_string)
            if answer == mathler:
                new_list.append(num_list[i])
        except ZeroDivisionError: 
            pass
        except SyntaxError:
            pass
    return new_list

find_list(prod_nnonon)
find_list(prod_nnnonn)
find_list(prod_nonnon)
find_list(prod_nononn)
print(f"{new_list}")