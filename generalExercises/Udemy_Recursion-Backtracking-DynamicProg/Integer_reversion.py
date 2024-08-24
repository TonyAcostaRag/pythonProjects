from tests import TestExecutor


def reverse_integer(int_num):

    inverted = 0
    while int_num > 0:
        remainder = int_num % 10
        int_num = int_num // 10
        inverted = inverted * 10 + remainder

    return inverted


TestExecutor.execute_function(
    [1234, 3434, 123456789, 987654321123456789],
    reverse_integer)
