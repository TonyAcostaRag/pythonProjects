def are_anagrams(phrase_one, phrase_two):
    phrase_dict_one = {}
    phrase_dict_two = {}

    phrase_one_no_spaces = phrase_one.lower().replace(' ', '')
    phrase_two_no_spaces = phrase_two.lower().replace(' ', '')

    if len(phrase_one_no_spaces) != len(phrase_two_no_spaces):
        return False

    def store_in_dict(phrase, phrase_dict):

        for char in phrase:
            if char not in phrase_dict:
                phrase_dict[char] = 1
            else:
                phrase_dict[char] += 1

        return phrase_dict

    phrase_dict_one = store_in_dict(phrase_one_no_spaces, phrase_dict_one)  # ---> Be aware on recreated variables.
    phrase_dict_two = store_in_dict(phrase_two_no_spaces, phrase_dict_two)

    return phrase_dict_one == phrase_dict_two


print(are_anagrams('restful', 'fluster'))
print(are_anagrams('letra_uno', 'letra_dos'))
print(are_anagrams('my ideal time', 'Immediately'))
