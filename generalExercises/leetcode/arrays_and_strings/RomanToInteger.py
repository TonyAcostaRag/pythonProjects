from tests import TestExecutor


def romanToInt(roman: str) -> int:

    values_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900,
    }

    current_sum = 0
    i = 0
    while i < len(roman):

        if len(roman[i:]) >= 2 and roman[i:i+2] in values_dict:
            current_sum += values_dict[roman[i:i+2]]
            i += 2
        else:
            current_sum += values_dict[roman[i:i+1]]
            i += 1

    return current_sum


if __name__ == '__main__':
    TestExecutor.execute_function([
        ['III'],
        ['LVIII'],
        ['MCMXCIV'],
        ['CM']
    ],
    [
        3,
        58,
        1994,
        900
    ],
        romanToInt
    )
