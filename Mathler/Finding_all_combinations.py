from itertools import *
from itertools import permutations
from itertools import accumulate
from itertools import combinations
from operator import add

q = ["+","-","*","/"]
r = ["0","1","2","3"]               # ["0","1","2","3"]
s = ["0","1","2","3"]              #[0,1,2,3]

t = [0,1,2,3,4,5,6,7,8,9]
u = [0,1,2,3,4,5,6,7,8,9]
v = [0,1,2,3,4,5,6,7,8,9]
w = [0,1,2,3,4,5,6,7,8,9]
x = [0,1,2,3,4,5,6,7,8,9]
y = [0,1,2,3,4,5,6,7,8,9]
z = [0,1,2,3,4,5,6,7,8,9]
n = [0,1,2,3,4,5,6,7,8,9]
prod_rs = list(product(r,q,s, repeat=2))
#print(len(prod_rs))
#print(prod_rs)
invalid = []

prod_rs[1]
my_list = [prod_rs[1][0],prod_rs[1][1],prod_rs[1][2],prod_rs[1][3],prod_rs[1][4],prod_rs[1][5]]
my_string = ''.join(my_list)
print(my_string)
answer = eval(my_string)
print(answer)
#"string[0]+string[1]+string[2]+string[3]+string[4]+
#string_1 = add,(string)
#string = eval(str(string_1))
#print(string)

'''
for i in range(len(prod_rs)):
    for sym in prod_rs[i][0]:
        if sym == '+':
            invalid.append(i)
        if sym == '-':
            invalid.append(i)
        if sym == '/':
            invalid.append(i)
        if sym == '*':
            invalid.append(i)

for i in range(len(prod_rs)):
    for sym in prod_rs[i][0]:
        for j in range(4):
            if sym == q[j]:
                invalid.append(i)

for i in invalid:
    prod_rs.pop(i)
    prod_rs.insert(i,"")

print(prod_rs)
#print(len(invalid))
#print(invalid)

if i in prod_rs != "":
    print(prod_rs[i])
'''

