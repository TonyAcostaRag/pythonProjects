from tests import TestExecutor


def binary_search(arr, key):
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = (left + right) // 2
        if arr[middle] == key:
            return middle
        elif arr[middle] > key:
            right = middle - 1
        elif arr[middle] < key:
            left = middle + 1
    return -1


TestExecutor.execute_function(
    [
        [[4, 11, 18, 30, 54], 4],
        [[4, 11, 18, 30, 54], 11],
        [[4, 11, 18, 30, 54], 18],
        [[4, 11, 18, 30, 54], 30],
        [[4, 11, 18, 30, 54], 54],
        [[4, 11, 18, 30, 54], 3]
    ],
    binary_search
)
