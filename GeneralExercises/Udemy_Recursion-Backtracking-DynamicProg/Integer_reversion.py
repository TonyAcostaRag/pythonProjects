from datetime import datetime


def reverse_integer(int_num):

    # 1. Convert the integer to string.
    string_num = str(int_num)

    # 2. convert the string in a List
    num_list = [char for char in string_num]

    # 3. swap the first number with the last one in a loop
    # 4. Continue while first num is less than last
    # 5. join all the items of the list into an string
    # 6. convert string into an integer.

    first_num = 0
    last_num = len(num_list)-1
    while first_num < last_num:
        temp_var = num_list[first_num]
        num_list[first_num] = num_list[last_num]
        num_list[last_num] = temp_var
        first_num += 1
        last_num -= 1

    string_num = ''
    for char in num_list:
        string_num += char

    return int(string_num)


def execute_function(test_input):
    for i in test_input:
        start_time = datetime.now()
        print(reverse_integer(i))
        print('Elapsed time:', datetime.now() - start_time)


execute_function(['1234', '3434', '123456789', '987654321123456789'])
