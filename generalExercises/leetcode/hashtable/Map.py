def first_non_repeating_char(s):
    
    if len(s) == 0 or s is None:
        return None
    
    dups = {}
    for i in range(len(s)):
        
        if s[i] not in dups:
            dups[s[i]] = 1
        else:
            dups[s[i]] += 1

    for char in s:
        if dups[char] == 1:
            return char
            
    return None

def group_anagrams(strings):
    
    coded_strings = {}
    for s in strings:

        char_freq = [0] * 26
        for char in s:
            char_freq[ord(char) - ord('a')] += 1

        if tuple(char_freq) not in coded_strings:
            coded_strings[tuple(char_freq)] = []
        coded_strings[tuple(char_freq)].append(s)

    return list(coded_strings.values())

def two_sum(nums, target):

    val_indexes = {}
    for i in range(len(nums)):

        if (target - nums[i]) not in val_indexes:
            val_indexes[nums[i]] = i
        else:
            return [val_indexes[target - nums[i]], i]
        
    return []


if __name__ == '__main__':

    '''
    # First non-duplicate
    expected_results = ['l', 'h', None]
    test_inputs = [['leetcode'], ['hello'], ['aabbcc']]
    for i in range(len(test_inputs)):
        result = first_non_repeating_char(*test_inputs[i])
        if result == expected_results[i]:
            print('PASSED')
        else:
            print('FAILED', 'Actual:', result, 'Expected:', expected_results[i])
    '''

    '''
    # Group anagrams
    expected_results = [
        [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']],
        [['abc', 'cba', 'bac'], ['foo'], ['bar']],
        [['listen', 'silent'], ['triangle', 'integral'], ['garden', 'ranged']],
        [['ad'], ['bc']]
    ]
    test_inputs = [
        [["eat", "tea", "tan", "ate", "nat", "bat"]],
        [["abc", "cba", "bac", "foo", "bar"]],
        [["listen", "silent", "triangle", "integral", "garden", "ranged"]],
        [["ad", "bc"]]
    ]
    for i in range(len(test_inputs)):
        result = group_anagrams(*test_inputs[i])
        if result == expected_results[i]:
            print('PASSED')
        else:
            print('FAILED', 'Actual:', result, 'Expected:', expected_results[i])
    '''


    # Two sum
    expected_results = [
        [1, 4],
        [1, 3],
        [0, 3],
        [1, 3],
        [],
        [2, 3],
        [0, 1],
        []
    ]
    test_inputs = [
        [[5, 1, 7, 2, 9, 3], 10],
        [[4, 2, 11, 7, 6, 3], 9],
        [[10, 15, 5, 2, 8, 1, 7], 12],
        [[1, 3, 5, 7, 9], 10],
        [[1, 2, 3, 4, 5], 10],
        [[1, 2, 3, 4, 5], 7],
        [[1, 2, 3, 4, 5], 3],
        [[], 0]
    ]
    for i in range(len(test_inputs)):
        result = two_sum(*test_inputs[i])
        if result == expected_results[i]:
            print('PASSED')
        else:
            print('FAILED', 'Actual:', result, 'Expected:', expected_results[i])

