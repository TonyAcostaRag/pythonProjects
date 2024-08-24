from tests import TestExecutor


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


TestExecutor.execute_function(
    ['anita lava la tina', 'no_palindrome', 'radar', 'madam'],
    is_palindrome)

