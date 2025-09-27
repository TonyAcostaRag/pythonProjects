
def containsDuplicate(nums: list[int]) -> bool:
        
    my_set = set()
    for num in nums:
        
        other_set = set()
        other_set.add(num)
        if other_set.issubset(my_set):
            return True
        
        my_set.add(num)
    return False


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

    nums = [1,2,3,4]
    print(containsDuplicate(nums))
