import random
import math


def get_random_number():
    number = random.randint(1, 100)
    print(number)

def get_ordinal_from_char(char):
    ordinal = ord(char)
    return ordinal

def get_max_from_iterable(dict):
    max_number = max(dict)
    return max_number

def isPalindrome(text):

    text = text.replace(' ', '')
    left = 0
    right = len(text) - 1
    i = 0
    while i < len(text) // 2:

        if text[left].lower() != text[right].lower():
            return False

        i += 1
        left += 1
        right -= 1

    return True

def memory_object_analyzer(object):

    print('Object type:', type(object))

    object_1 = object
    object_2 = object_1

    print('Object 1 value:', object_1)
    print('Object 2 value:', object_2)

    print('Object 1 memory address:', id(object_1))
    print('Object 2 memory address:', id(object_2))

    if isinstance(object, str):
        object_2 = 'Other string'
    elif isinstance(object, int):
        object_2 = 2
    elif isinstance(object, dict):
        object_2[1] = 'uno'

    print('Object 1 value:', object_1)
    print('Object 2 value:', object_2)

    print('Object 1 memory address:', id(object_1))
    print('Object 2 memory address:', id(object_2))

def for_analyzer():

    for i in range(len([ i for i in range(10) ])):
        i += 1
        print(i)

def Boolean_Analyzer():

    zero = 0
    one = 1
    five = 5

    if five:
        print(five)
    
    if one:
        print(one)

    if zero:
        print(zero)

    xor = one ^ five
    print('or exclusive of 1 ^ 5', xor)

    xor = five ^ one
    print('or exclusive of 5 ^ 1', xor)

    xor = 4 ^ 3
    print('or exclusive of 4 ^ 3', xor)

def xor_analyzer() -> int:
        
    nums = [1,1,0,0]
    a = 0
    for i in nums:
        a ^= i
        print(a)
    return a

def string_analyzer(input_s):

    if input_s:
        print(input_s)
    else:
        print(bool(input_s))

    if input_s is None:
        print('String is None')
    else:
        print('String is just empty not None')

def array_analyzer():

    empty_array = []
    print('Empty array bool:', bool(empty_array))

    one_item_array = [1]
    print('One item array bool:', bool(one_item_array))

    char_array = ['t', 'o', 'n', 'y']
    print(''.join(char_array))
    
def math_operations_analyzer():
    
    result = 4 / 5
    print(result)
    result = int(result)
    print('--> Final result:', result)

    result = 20 / 5
    print(result)
    result = int(result)
    print('--> Final result:', result)

def list_comprehension():
    board = [[(i+1, j+1) for i in range(5)] for j in range(3)]

    for row in board:
        
        for cell in row:
            print(cell, end = ' ')
        print()
    
    print()
    print('Indexing the matrix:')
    print()
        
    n = 3
    m = 5
    for j in range(n):
        for i in range(m):
            print(board[j][i], end = ' ')
        print()

def defining_list_comprehension(rows, columns):

    matrix = [[ (column, row) for column in range(columns) ] for row in range(rows)]

    for row in range(rows):
        for column in range(columns):

            print(matrix[row][column], end = ' ')
        print()
    
def ceiling(dividend, divider):

    total = math.ceil(dividend/divider)
    return total

def list_operations_analyzer():

    empty_array = [1, 2, 4]

def set_analyzer():
    
    sandwiches_set_one = set([0,1,1])
    students_set_one = set([0,1,1])

    print(sandwiches_set_one)
    print(students_set_one)

    set_difference_one = sandwiches_set_one.difference(students_set_one)
    print(
            'Difference of the sets one:', set_difference_one,
            '\nLength of the difference one:', len(set_difference_one)
        )
    

    sandwiches_set_two = set([0,1,1])
    students_set_two = set([1,1,1])

    print(sandwiches_set_two, len(sandwiches_set_two))
    print(students_set_two, len(students_set_two))

    set_difference_two = sandwiches_set_two.difference(students_set_two)
    print(
            'Difference of the sets two:', set_difference_two,
            '\nLength of the difference two:', len(set_difference_two)
        )


if __name__ == '__main__':

    set_analyzer()
