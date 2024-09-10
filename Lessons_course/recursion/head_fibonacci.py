from tests import TestExecutor


def fibonacci_number(n):

    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci_number(n - 1) + fibonacci_number(n - 2)


TestExecutor.execute_function(
    [
        [10],
        [9],
        [8],
        [7],
        [6],
        [5],
        [4],
        [3],
        [2],
        [1],
        [0]
    ],
    fibonacci_number
)
