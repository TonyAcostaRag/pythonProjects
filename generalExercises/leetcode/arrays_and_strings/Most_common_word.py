from tests import TestExecutor


def mostCommonWord(paragraph, banned):
    # 1. Store the different words in a dictionary.
    word_dictionary = {}
    word_list = paragraph.lower().replace(',', ' ').replace('.', ' ').split()
    puntuation_marks = ['!', '"', '\'', '?', '´', ';', ':', '_', '-']

    for word in word_list:
        if word[-1:] in puntuation_marks:
            word = word[:-1]
        if word not in banned:
            if word not in word_dictionary:
                word_dictionary[word] = 1
            else:
                word_dictionary[word] += 1

    # Print the most common word.
    max_word_occurence = 0
    most_common_word = ''
    for key, value in word_dictionary.items():
        if value > max_word_occurence:
            most_common_word = key
            max_word_occurence = value

    return most_common_word


TestExecutor.execute_function([
    ["Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]],
    ["a.", []],
    ["a, a, a, a, b,b,b,c, c", ["a"]],
    ["..Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]]
],
    ["ball", "a", "b", "ball"],
    mostCommonWord)
