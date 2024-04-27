
sample_story = '''Once upon a time, there was a beginner programmer named Alice who was eager to learn Python. She tried to learn from books, but found it difficult to grasp the concepts. One day, she stumbled upon an online course.

Alice was thrilled. The course was taught by a well-known programmer who made the lessons interesting and easy to understand. The course covered everything a beginner programmer needed, and Alice was finally able to understand how to code in Python.'''


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
