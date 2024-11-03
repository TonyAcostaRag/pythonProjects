from tests import TestExecutor


def isCurcularSentence(sentence: str) -> bool:
    if sentence == '' or sentence == ' ':
        return False
    word_list = sentence.split(' ')
    if len(word_list) == 1:
        return True if word_list[0][0] == word_list[0][-1] else False
    else:
        if word_list[0][0] == word_list[-1][-1]:
            for i in range(0, len(word_list) - 1):
                if word_list[i][-1] != word_list[i + 1][0]:
                    return False
            return True
        else:
            return False


if __name__ == '__main__':
    TestExecutor.execute_function([
        ["leetcode exercises sound delightful"],
        ["eetcode"],
        ["Leetcode is cool"],
        ["leetcode"]
    ],
    [
        True,
        True,
        False,
        False
    ],
        isCurcularSentence
    )
