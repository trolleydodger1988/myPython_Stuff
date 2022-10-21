import math
from itertools import *
from itertools import permutations
from itertools import accumulate
from functools import reduce

#num = int(input("Enter a number: "))
factor_list = []
def factors(num):
    for i in range(1,num):
        if num % i == 0:
            factor_list.append(i)
    return factor_list


num_list = [0,1,2,3,4,5,6,7,8,9]
sym_list = ['-','+','/','*']


a = [1,2,3,4,5,6,7,8,9,0,'-','+','/','*']
perm = permutations(a,3)
print(type(perm))
perm_list = list(perm)
print(type(perm_list))
y = len(perm_list)
print(y)
#x = int(input("Enter the index you wish to access: "))
symb_count = []
for i in range(y):              # make a list of the idexies where it starts or ends with a symbol
    if perm_list[i][0] == '*':
        symb_count.append(i)
    if perm_list[i][-1] == '*':
        symb_count.append(i)
    if perm_list[i][0] == '+':
        symb_count.append(i)
    if perm_list[i][-1] == '+':
        symb_count.append(i)
    if perm_list[i][0] == '/':
        symb_count.append(i)
    if perm_list[i][-1] == '/':
        symb_count.append(i)
    if perm_list[i][0] == '-':
        symb_count.append(i)
    if perm_list[i][-1] == '-':
        symb_count.append(i)

#perm_list.pop(x)
#print(list(symb_count))

for x in symb_count:                # remove the index from perm_list where there are symbols in the first or last
    perm_list.pop(x)
    perm_list.insert(x, '')

perm_list_no_blank = []                 # list of the permutations but without any blanks
for x in range (len(perm_list)):
    if perm_list[x] != '':                          # if theres no blank, add to this new list perm_list_no_blank
        perm_list_no_blank.append(perm_list[x])


#print(perm_list_no_blank)

answ = list(str(perm_list_no_blank[-1]))
print(answ)
answ_str = ''.join(answ)
print(answ_str)
answ_str_2 = ''.join(answ_str)
answ_str_2.replace(',', '').replace(')', '').replace('(', '').replace("'", '')
num_str = (str)
for i in range(3):
    num_str = num_str+answ_str_2[i]
print(num_str)