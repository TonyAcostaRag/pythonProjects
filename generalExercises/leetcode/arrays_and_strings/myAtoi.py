from tests import TestExecutor


def myAtoi(s: str) -> int:

    negative_flag = False
    result = 0
    current_digit = ''

    def round_big_number(big_number):
        if big_number > 2**31 - 1:
            return int(2**31 - 1)
        elif big_number < -2**31:
            return int(-2**31)
        else:
            return big_number

    for i in s:
        if i == ' ':
            if current_digit != '+' and current_digit != '-' and not current_digit.isdigit():
                continue
            else:
                if negative_flag:
                    result *= -1
                return round_big_number(result)
        if i.isalpha() or i == '.' or i == ',':
            if negative_flag:
                result *= -1
            return round_big_number(result)
        if i == '-' or i == '+':
            if current_digit != '+' and current_digit != '-' and not current_digit.isdigit():
                if i == '-':
                    negative_flag = True
                    current_digit = '-'
                if i == '+':
                    negative_flag = False
                    current_digit = '+'
                continue
            else:
                if negative_flag:
                    result *= -1
                return round_big_number(result)

        current_digit = i
        result = result * 10 + int(current_digit)

    if negative_flag:
        result *= -1

    return round_big_number(result)


if __name__ == '__main__':
    TestExecutor.execute_function([
        ["42"],
        [" -042"],
        ["1337c0d3"],
        ["0-1"],
        ["words and 987"],
        ["3333333333"],
        ["-3333333333"],
        ["3.14159"],
        ["+-12"],
        ["  -0012a42"],
        ["   +0 123"],
        ["   -1 123"],
        ["-5-"],
        ["  +  413"],
        [" ++1"],
        ["      -11919730356x"]
    ],
    [
        42,
        -42,
        1337,
        0,
        0,
        2147483647,
        -2147483648,
        3,
        0,
        -12,
        0,
        -1,
        -5,
        0,
        0,
        -2147483648
    ],
        myAtoi
    )
