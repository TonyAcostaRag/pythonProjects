import os
import errno
from sys import stderr


def frequency_histogram():
    #filename = input("Enter the name of the file: ")
    filename = 'text.txt'
    #filename = 'text_test.txt'
    letter_histogram = {}

    try:
        file = open(filename, 'r', encoding="UTF-8")

        ch = file.read(1)
        while ch != '':
            if ch.lower() in letter_histogram:
                letter_histogram[ch.lower()] += 1
            else:
                letter_histogram[ch.lower()] = 1
            ch = file.read(1)

        file.close()

    except IOError as ioE:
        print("There is an IO Error:")

    for i in letter_histogram:
        print(i, "->", letter_histogram[i])


def frequency_histogram_sorted():
    filename = 'text.txt'
    letter_histogram = {}

    try:
        file = open(filename, 'r', encoding="UTF-8")

        ch = file.read(1)
        while ch != '':
            if ch.lower() in letter_histogram:
                letter_histogram[ch.lower()] += 1
            else:
                letter_histogram[ch.lower()] = 1
            ch = file.read(1)

        file.close()

    except IOError as ioE:
        print("There is an IO Error:")

    letter_histogram_sorted = dict(sorted(letter_histogram.items(), key=lambda x: x[1], reverse=True))

    hist_filename = ''

    for i in filename:
        if i != '.':
            hist_filename += i
        else:
            break

    try:
        file = open(hist_filename + '.hist', 'w', encoding="UTF-8")

        for key, value in letter_histogram_sorted.items():
            file.write(key + " -> " + str(value) + "\n")

        file.close()
    except IOError as ioE:
        print("There is IO Error")

    print("Sorted dictionary")
    for i in letter_histogram_sorted:
        print(i, "->", letter_histogram_sorted[i])


#frequency_histogram()
frequency_histogram_sorted()
