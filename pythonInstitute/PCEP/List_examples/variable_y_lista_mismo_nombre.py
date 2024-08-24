

my_list = ['Mary', 'had', 'a', 'little', 'lamb']


def my_list(my_lis):
    del my_lis[3]
    my_lis[3] = 'ram'
    print("within the function", my_lis)


my_list(my_list)

print(my_list)

