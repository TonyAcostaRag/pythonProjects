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
    
