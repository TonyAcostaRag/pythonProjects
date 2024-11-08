import collections

from tests import TestExecutor


def groupAnagrams(strs: list[str]) -> list[list[str]]:

    groups: collections.defaultdict[int, list[str]] = collections.defaultdict(list)
    for s in strs:
        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')] += 1
        groups[tuple(count)].append(s)

    return list(groups.values())


if __name__ == '__main__':
    TestExecutor.execute_function([
        [["eat", "tea", "tan", "ate", "nat", "bat"]],
        [[""]],
        [["a"]]
    ],
    [
        [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']],
        [[""]],
        [["a"]]
    ],
        groupAnagrams
    )
