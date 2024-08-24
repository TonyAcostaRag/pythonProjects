def is_palindrome(phrase):

    phrase_no_spaces = phrase.lower().replace(' ', '')
    first_letter = 0
    last_letter = len(phrase_no_spaces)-1

    while first_letter < last_letter:
        if phrase_no_spaces[first_letter] != phrase_no_spaces[last_letter]:
            return False
        first_letter += 1
        last_letter -= 1

    return True


print(is_palindrome('anita lava la tina'))
print(is_palindrome('no_palindrome'))
print(is_palindrome('radar'))
print(is_palindrome('madam'))
