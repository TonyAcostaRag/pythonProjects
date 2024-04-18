"""
# By using yield, fun() becomes a generator object.
def fun(n):
    for i in range(n):
        yield i


for i in fun(5):
    print(i)
"""

"""
try:
    raise Exception(1, 2, 3)
except Exception as e:
    print(e)
    print(e.args)
    print(len(e.args))
"""

"""
import math


def halve_string(input_string):
    fisrt_half = ''
    second_half = ''

    for i in range(0, len(input_string)):

        if (i+1) <= math.ceil(len(input_string) / 2):
            fisrt_half += input_string[i]
        else:
            second_half += input_string[i]

    return (fisrt_half, second_half)


def halve_strings(string_list):
    tuple_list = []

    for element in string_list:
        #tuple_list.append(su.halve_string(element))
        tuple_list.append(halve_string(element))

    return tuple_list


if __name__ == '__main__':
    print(halve_string('Mark'))
    print(halve_string('Antonio'))
    print(halve_string('Lydia'))
    print(halve_strings(['Mark', 'Lydia']))
"""

"""
string_value = 'four sacrifice darkness. I\'m tester'


import logging as log


sample_story = '''Once upon a time, there was a beginner programmer named Alice who was eager to learn Python. She tried to learn from books, but found it difficult to grasp the concepts. One day, she stumbled upon an online course.

Alice was thrilled. The course was taught by a well-known programmer who made the lessons interesting and easy to understand. The course covered everything a beginner programmer needed, and Alice was finally able to understand how to code in Python.'''


#sample_story = "Once I\'m awaken, I\'ll sacrifice your soul to the ruler of darkness."


def get_longest_word(string):
    # Split the words within the string.
    splited_string = string.split()
    print(splited_string, end='\n\n')

    # Filling the dictionary with all the words.
    words_dictionary = {}
    print('Printing the dictionary right after the creation:', words_dictionary)

    for i in splited_string:

        if i not in words_dictionary:
            words_dictionary[i] = len(i)

    print('Printing the dictionary after being filled:', words_dictionary)

    # Check for the maximum lenght of the words in the string.
    biggest_word = ''
    biggest_value = 0
    for keys, values in words_dictionary.items():

        if words_dictionary[keys] > biggest_value:
            biggest_value = words_dictionary[keys]
            biggest_word = keys

    print('Biggest word:', biggest_word)
    print('Biggest value:', biggest_value)

    return biggest_word

print(get_longest_word(sample_story))

"""

my_list = [10, 20, 20, 30, 20, 40]

new_list = [i for i in my_list if i != 20]

print(new_list)
