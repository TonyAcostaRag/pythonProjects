from tests import TestExecutor


def recursion(n):

    if n == 0:
        return 1

    return n * recursion(n-1)


TestExecutor.execute_function(
    [
        [0],
        [1],
        [2],
        [3],
        [4],
        [5],
        [6],
        [7],
        [8],
        [9],
        [10]
    ],
    recursion
)
