from tests import TestExecutor


def intToRoman(num):
    symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    roman = ''
    i = 0
    while i < len(values) and num > 0:
        while num >= values[i]:
            num -= values[i]
            roman += symbols[i]
        i += 1
    return roman


if __name__ == '__main__':
    TestExecutor.execute_function([
        [3749],
        [58],
        [1994]
    ],
    [
        "MMMDCCXLIX",
        "LVIII",
        "MCMXCIV"
    ],
        intToRoman
    )
