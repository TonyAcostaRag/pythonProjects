from tests import TestExecutor


def lengthOfLongestSubstring(s: str) -> int:
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1

    biggest_string = ''
    left = 0
    max_length = 1
    for i in range(len(s)):

        if max_length >= len(s[left:]):
            break

        if s[i] not in biggest_string:
            biggest_string += s[i]
        else:
            biggest_string += s[i]
            for _ in range(len(biggest_string[:-1])):
                if s[i] not in biggest_string[:-1]:
                    break
                biggest_string = biggest_string[1:]
                left += 1
                
        if len(biggest_string) > max_length:
            max_length = len(biggest_string)

    return max_length


TestExecutor.execute_function([
        ['abcabcbb'],
        ['bbbbb'],
        ['pwwkew'],
        [' '],
        ['au'],
        ['dvdf'],
        ['']
    ],
    [3, 1, 3, 1, 2, 3, 0],
    lengthOfLongestSubstring)
