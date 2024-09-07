from tests import TestExecutor


def countSwaps(a):
    swaps = 0
    for i in range(0, len(a)):

        for j in range(0, len(a) - 1):

            if a[j] > a[j + 1]:
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp
                swaps += 1

    print('Array is sorted in', swaps, 'swaps.')
    print('First Element:', a[0])
    print('Last Element:', a[-1])


TestExecutor.execute_function(
    [
        [[1, 2, 3]],
        [[3, 2, 1]],
        [[4, 2, 3, 1]],
    ],
    countSwaps
)
