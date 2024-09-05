from tests import TestExecutor


def runner_up(arr):

    arr.sort()
    print(arr)

    top = arr[-1]
    runner_up = 0

    for i in range(len(arr) - 2, -1, -1):
        if arr[i] < top:
            runner_up = arr[i]
            break

    print(runner_up)


if __name__ == '__main__':
    import random

    unsorted_10_list = [random.randint(-100, 100) for _ in range(10)]
    unsorted_9_list = [random.randint(-100, 100) for _ in range(9)]
    unsorted_8_list = [random.randint(-100, 100) for _ in range(8)]
    unsorted_7_list = [random.randint(-100, 100) for _ in range(7)]
    unsorted_6_list = [random.randint(-100, 100) for _ in range(6)]
    unsorted_4_list = [random.randint(-100, 100) for _ in range(4)]
    unsorted_3_list = [random.randint(-100, 100) for _ in range(3)]
    unsorted_2_list = [random.randint(-100, 100) for _ in range(2)]

    TestExecutor.execute_function(
        [
            [[2, 3, 6, 6, 5]],
            [unsorted_10_list],
            [unsorted_9_list],
            [unsorted_8_list],
            [unsorted_7_list],
            [unsorted_6_list],
            [unsorted_4_list],
            [unsorted_3_list],
            [unsorted_2_list]
        ],
        runner_up
    )
