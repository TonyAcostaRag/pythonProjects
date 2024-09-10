from tests import TestExecutor


def factorial(n, accumulator):

    if n == 0:
        return accumulator

    return factorial(n-1, n*accumulator)


TestExecutor.execute_function(
    [
        [0, 1],
        [1, 1],
        [2, 1],
        [3, 1],
        [4, 1],
        [5, 1],
        [6, 1],
        [7, 1],
        [8, 1],
        [9, 1],
        [10, 1]
    ],
    factorial
)
