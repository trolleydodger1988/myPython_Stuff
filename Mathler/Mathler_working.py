#this file sucks, use The_Ultimate_Mathler_Solution_Finder instead

from itertools import *
from itertools import permutations
from itertools import accumulate
from itertools import combinations
from operator import add
import random 

def roll_dice(num):
    return random.randint(0, num) #function to generate random number

q = ["+","-","*","/"]
r = ["0","1","2","3","4","5","6","7","8","9"]               # ["0","1","2","3"]
s = ["0","1","2","3","4","5","6","7","8","9"]              #[0,1,2,3]

prod_rqs = list(product(r,q,s, repeat=2))

mathler = int(input("Input the Mathler number: "))
my_list = []
new_list = []
for i in range(len(prod_rqs)):
    my_list = [prod_rqs[i][0],prod_rqs[i][1],prod_rqs[i][2],prod_rqs[i][3],prod_rqs[i][4],prod_rqs[i][5]]
    my_string = ''.join(my_list)
    try:
        answer = eval(my_string)
        if answer == mathler:
            new_list.append(prod_rqs[i])
    except ZeroDivisionError: 
        pass
    except SyntaxError:
        #new_list.remove(prod_rs[i])
        pass

for i in range(len(prod_rqs)):
    my_list = [prod_rqs[i][0],prod_rqs[i][1],prod_rqs[i][2],prod_rqs[i][3],prod_rqs[i][4],prod_rqs[i][5]]
    my_string = ''.join(my_list)
    try:
        answer = eval(my_string)
        if answer == mathler:
            new_list.append(prod_rqs[i])
    except ZeroDivisionError: 
        pass
    except SyntaxError:
        #new_list.remove(prod_rs[i])
        pass


if len(new_list) >= 1:
    print(new_list)
else:
    print('Nothing was found')

answer = False
no_answer = True
not_answer = True
counter = 0

while not answer:

    random_list = [r[roll_dice(9)], r[roll_dice(9)], q[roll_dice(3)], r[roll_dice(9)], q[roll_dice(3)], r[roll_dice(9)]]
    random_string = ''.join(random_list)
    try:
        answer_2 = eval(random_string)
        if answer_2 == mathler:
            print(random_string)
            counter +=1
            if counter > 49:
                answer = True
    except ZeroDivisionError: 
        pass
    except SyntaxError:
        pass

counter = 0
while no_answer:
    random_list = [r[roll_dice(9)], q[roll_dice(3)], r[roll_dice(9)], q[roll_dice(3)], r[roll_dice(9)], r[roll_dice(9)]]
    random_string = ''.join(random_list)
    try:
        answer_2 = eval(random_string)
        if answer_2 == mathler:
            print(random_string)
            counter +=1
            if counter > 49:
                no_answer = False
    except ZeroDivisionError: 
        pass
    except SyntaxError:
        pass

counter = 0
while not_answer:
    random_list = [r[roll_dice(9)], r[roll_dice(9)], r[roll_dice(9)], q[roll_dice(3)], r[roll_dice(9)], r[roll_dice(9)]]
    random_string = ''.join(random_list)
    try:
        answer_2 = eval(random_string)
        if answer_2 == mathler:
            print(random_string)
            counter +=1
            if counter > 49:
                not_answer = False
    except ZeroDivisionError: 
        pass
    except SyntaxError:
        pass