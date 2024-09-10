from tests import TestExecutor


def binary_search_recursive(arr, key, left, right):

    if left > right:
        return -1
    else:
        middle = (left + right) // 2
        if arr[middle] == key:
            return middle
        elif arr[middle] > key:
            return binary_search_recursive(arr, key, left, middle - 1)
        elif arr[middle] < key:
            return binary_search_recursive(arr, key, middle + 1, right)


TestExecutor.execute_function(
    [
        [[4, 11, 18, 30, 54], 4, 0, 4],
        [[4, 11, 18, 30, 54], 11, 0, 4],
        [[4, 11, 18, 30, 54], 18, 0, 4],
        [[4, 11, 18, 30, 54], 30, 0, 4],
        [[4, 11, 18, 30, 54], 54, 0, 4],
        [[4, 11, 18, 30, 54], 3, 0, 4]
    ],
    binary_search_recursive
)
