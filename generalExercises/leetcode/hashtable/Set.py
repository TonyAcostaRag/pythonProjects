
def containsDuplicate(nums: list[int]) -> bool:
        
    my_set = set()
    for num in nums:
        
        other_set = set()
        other_set.add(num)
        if other_set.issubset(my_set):
            return True
        
        my_set.add(num)
    return False

def find_pairs(arr1, arr2, target):

    print(
        '\narr1:', arr1,
        '\narr2:', arr2,
        '\ntarget:', target
    )
    
    set_arr1 = set(arr1)
    pairs = []

    print(
        '\nset_arr1:', set_arr1,
        '\npairs:', pairs
    )
    
    for i in range(len(arr2)):

        print('i:', i, '| target - arr2[i]:', target - arr2[i])
        
        if (target - arr2[i]) in set_arr1:
            pairs.append((arr2[i], target - arr2[i]))
            set_arr1.remove(target - arr2[i])

        print('pairs:', pairs)
            
    return pairs


if __name__ == '__main__':

    '''
    my_hashset = set()

    print('Adding 3')
    my_hashset.add(3)
    print('Adding 30')
    my_hashset.add(30)
    print('Adding 300')
    my_hashset.add(300)

    print('Removing 3')
    my_hashset.remove(3)
    # After removal, check if key is not present in the set.
    print('Checking if 3 is in hashset')
    if 3 not in my_hashset:
        print('3 is not present in the hashset.')

    print('Size of hashset is:', len(my_hashset))

    print('Iterate the hashset:')
    for x in my_hashset:
        print(x, end=' ')
    print()

    my_hashset.clear()
    print('Size of hashset is:', len(my_hashset))
    '''

    '''
    nums = [1,2,3,4]
    print(containsDuplicate(nums))
    '''

    
    # find_pairs
    expected_results = [
        [[(5, 2), (3, 4), (1, 6)], [(2, 5), (4, 3), (6, 1)]]
    ]
    test_inputs = [
        [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], 7]
    ]
    for i in range(len(test_inputs)):
        result = find_pairs(*test_inputs[i])
        if result == expected_results[i][0] or result == expected_results[i][1]:
            print('PASSED')
        else:
            print('FAILED', 'Actual:', result, 'Expected:', expected_results[i])
