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
