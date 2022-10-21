my_list = [("1","2","3", "+"), ("1","4","5", "-"), ("1","2","6", "/")]
new_list =[]
char = ["1","2", "/"]
for i in range(len(my_list)):
    for j in range(len(char)):
        if char[j] not in my_list[i]:
            new_list.append(my_list[i])
    
print(new_list)