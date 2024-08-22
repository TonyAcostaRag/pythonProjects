my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

dup_values = True

i = 0
while dup_values:
    
    if i < (len(my_list) - 1):
        if my_list[i] in my_list[(i+1):]:
            del my_list[i]
            i = 0
            continue
            
        i += 1
        
    if i == (len(my_list) - 1):
        dup_values = False

print("The list with unique elements only:")
print(my_list)
