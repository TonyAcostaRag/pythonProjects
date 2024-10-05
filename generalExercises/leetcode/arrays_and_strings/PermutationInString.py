from tests import TestExecutor


def checkInclusion(s1, s2):

        def matches(s1map, s2arr):
            for i in range(26):
                if s1map[i] != s2arr[i]:
                    return False
            return True

        if len(s1) > len(s2):
            return False

        s1arr = [0] * 26
        s2arr = [0] * 26
        for i in range(len(s1)):
            s1arr[ord(s1[i]) - ord('a')] += 1
            s2arr[ord(s2[i]) - ord('a')] += 1

        for i in range(len(s2) - len(s1)):
            if matches(s1arr, s2arr):
                return True

            s2arr[ord(s2[i + len(s1)]) - ord('a')] += 1
            s2arr[ord(s2[i]) - ord('a')] -= 1

        return matches(s1arr, s2arr)


if __name__ == '__main__':
    TestExecutor.execute_function([
        ["ab", "eidbaooo"],
        ["ab", "eidboaoo"],
        ["ab", "ab"],
        ["ab", "ba"],
        ["adc", "dcda"],
        ["ab", "eidbaooo"],
        ["ab", "a"]
    ],
    [
        True,
        False,
        True,
        True,
        True,
        True,
        False
    ],
        checkInclusion)
