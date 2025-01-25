import random


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


print(isPalindrome('Anita lava la tina'))
