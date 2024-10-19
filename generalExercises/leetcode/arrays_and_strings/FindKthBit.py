from tests import TestExecutor


def findKthBit(n: int, k: int) -> str:

    binary_string = '0'

    def invert(s):
        inverted_s = ''
        for char in s:
            if char == '0':
                inverted_s += '1'
            else:
                inverted_s += '0'

        return inverted_s

    for i in range(1, n):
        binary_string = binary_string + '1' + invert(binary_string)[::-1]

    for bit in range(len(binary_string)):
        if bit + 1 == k:
            return binary_string[bit]


if __name__ == '__main__':
    TestExecutor.execute_function([
        [3, 1],
        [4, 11]
    ],
    [
        '0',
        '1'
    ],
        findKthBit
    )
