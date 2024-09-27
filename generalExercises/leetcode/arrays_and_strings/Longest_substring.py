from tests import TestExecutor


def lengthOfLongestSubstring(s: str) -> int:
    biggest_string = ''
    current_string = ''
    for i in range(len(s)):
        if len(current_string) == 0:
            current_string += s[i]
            biggest_string = current_string
            continue

        if s[i] not in current_string:
            current_string += s[i]
            if len(current_string) > len(biggest_string):
                biggest_string = current_string
        else:
            current_string += s[i]
            while s[i] in current_string[:-1] and len(current_string) > 1:
                current_string = current_string[1:]

    return len(biggest_string)



TestExecutor.execute_function([
        ['abcabcbb'],
        ['bbbbb'],
        ['pwwkew'],
        [' '],
        ['au'],
        ['dvdf']
    ],[3, 1, 3, 1, 2, 3],
    lengthOfLongestSubstring)
