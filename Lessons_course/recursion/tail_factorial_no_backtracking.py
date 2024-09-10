from tests import TestExecutor


def factorial(n, accumulator=1):

    if n == 0:
        return accumulator

    return factorial(n-1, n*accumulator)


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
    factorial
)
