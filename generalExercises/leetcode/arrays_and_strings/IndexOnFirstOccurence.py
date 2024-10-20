from tests import TestExecutor


def str_str(haystack: str, needle: str) -> int:

    i = 0
    while i < len(haystack):

        if haystack[i] == needle[0]:
            index = i
            if haystack[i:i + len(needle)] == needle:
                return index
            else:
                i += 1
        else:
            i += 1
    return -1


if __name__ == '__main__':
    TestExecutor.execute_function([
        ["sadbutsad", "sad"],
        ["leetcode", "leeto"],
        ["mississippi", "issip"]
    ],
    [
        0,
        -1,
        4
    ],
        str_str
    )
