import os


def count_occurrences(file, word):

    word_delimiters = [' ', ',', '.', '\n']

    try:
        stream = open(file)
        tempword = ''
        counter = 0

        character = stream.read(1)
        while character != '':

            while character not in word_delimiters:
                tempword += character
                character = stream.read(1)

            if tempword.lower() == word.lower():
                counter += 1

            tempword = ''
            character = stream.read(1)
    except Exception as e:
        print('An error ocurred', e)
    finally:
        stream.close()

    return counter


file = os.path.realpath(__file__)
file = os.path.dirname(file)
file = file.replace('PythonExercises', 'file.txt')

test_words = ['is', 'animal', 'ANIMAL', 'domestic', 'a', 'wild']

print('Occurences of ', test_words[0], ':', count_occurrences(file, test_words[0], ))
print('Occurences of ', test_words[1], ':', count_occurrences(file, test_words[1], ))
print('Occurences of ', test_words[2], ':', count_occurrences(file, test_words[2], ))
print('Occurences of ', test_words[3], ':', count_occurrences(file, test_words[3], ))
print('Occurences of ', test_words[4], ':', count_occurrences(file, test_words[4], ))
print('Occurences of ', test_words[5], ':', count_occurrences(file, test_words[5], ))
