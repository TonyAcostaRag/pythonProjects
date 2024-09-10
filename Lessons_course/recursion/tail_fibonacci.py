from tests import TestExecutor


def tail_fibonaci(n, a=0, b=1):
    if n == 0:
        return a
    if n == 1:
        return b

    return tail_fibonaci(n-1, b, a+b)


TestExecutor.execute_function(
    [
        [6],
        [5],
        [4],
        [3],
        [2],
        [1]
    ],
    tail_fibonaci
)
