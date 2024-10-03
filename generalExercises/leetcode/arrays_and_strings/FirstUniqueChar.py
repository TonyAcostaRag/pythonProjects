from tests import TestExecutor


def first_unique_char(s):
    char_dict = {}
    for i in range(len(s)):
        if s[i] not in char_dict:
            char_dict[s[i]] = 1
        else:
            char_dict[s[i]] += 1

    for i in range(len(s)):
        if char_dict[s[i]] == 1:
            return i

    return -1


if __name__ == '__main__':
    TestExecutor.execute_function([
        ["leetcode"],
        ["loveleetcode"],
        ["aabb"]
    ],
        [
            0,
            2,
            -1
        ],
        first_unique_char
    )
