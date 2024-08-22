
#

my_list = ['Mary', 'had', 'a', 'little', 'lamb']



def other_list(my_lis):

    print(my_lis)
    my_lis_2 = my_list[:]
    print(my_lis_2)
    for i in range(len(my_lis_2)):
        my_lis_2.append(i)
    print("within func", my_lis_2)


other_list(my_list)

print(my_list)
