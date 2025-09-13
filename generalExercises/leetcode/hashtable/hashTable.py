from dataStructures.Linear.hashTable.HashSet import MyHashSet


def arrayHasDuplicates(array):

    my_hash_set = MyHashSet()
    for num in array:

        if my_hash_set.contains(num):
            return True
        my_hash_set.add(num)
    
    return False

if __name__ == '__main__':

    array_nums = [2, 3, 4, 5, 5]
    print('Does array has duplicates:', arrayHasDuplicates(array_nums))
