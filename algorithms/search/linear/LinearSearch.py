from tests import TestExecutor


def linear_search(arr, key):

    for i in range(0, len(arr)):
        if arr[i] == key:
            return i

    return -1


TestExecutor.execute_function(
    [
        [[84, 21, 47, 96, 15], 96],
        [[84, 21, 47, 96, 15], 100]
    ],
    linear_search
)
