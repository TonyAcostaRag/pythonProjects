from tests import TestExecutor


def merge_sort(arr, left, right):

    if left < right:
        middle = (left + right) // 2

        merge_sort(arr, left, middle)
        merge_sort(arr, middle + 1, right)
        merge(arr, left, middle, right)
    return arr


def merge(arr, left, middle, right):

    i = left
    j = middle + 1
    k = left
    arr_b = [0] * (right + 1)

    while i <= middle and j <= right:
        if arr[i] < arr[j]:
            arr_b[k] = arr[i]
            i += 1
        else:
            arr_b[k] = arr[j]
            j += 1
        k += 1
    while i <= middle:
        arr_b[k] = arr[i]
        i += 1
        k += 1
    while j <= right:
        arr_b[k] = arr[j]
        j += 1
        k += 1
    for i in range(left, right + 1):
        arr[i] = arr_b[i]


if __name__ == '__main__':
    import random
    unsorted_100_list = [random.randint(1, 1000) for _ in range(100)]
    unsorted_1000_list = [random.randint(1, 1000) for _ in range(1000)]
    unsorted_10000_list = [random.randint(1, 1000) for _ in range(10000)]
    unsorted_100000_list = [random.randint(1, 1000) for _ in range(100000)]
    unsorted_200000_list = [random.randint(1, 1000) for _ in range(200000)]
    unsorted_500000_list = [random.randint(1, 1000) for _ in range(500000)]
    unsorted_1000000_list = [random.randint(1, 1000) for _ in range(1000000)]

    TestExecutor.execute_function(
        [
            [[3, 5, 8, 9, 6, 2], 0, 5],  # Elapsed time: 0:00:00.000051
            [unsorted_100_list, 0, 99],  # Elapsed time: 0:00:00.000154
            [unsorted_1000_list, 0, 999],  # Elapsed time: 0:00:00.002975
            [unsorted_10000_list, 0, 9999]  # Elapsed time: 0:00:00.131831
        ],
        merge_sort
    )

    # [unsorted_200000_list, 0, 199999],  # Elapsed time: 0:00:43.767426
    # [unsorted_500000_list, 0, 499999],  # Elapsed time: 0:05:08.836090
    # [unsorted_1000000_list, 0, 999999]  # Elapsed time: 0:21:02.974867
