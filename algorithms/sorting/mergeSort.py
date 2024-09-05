from tests import TestExecutor


def merge_sort(arr, left, right):

    if left < right:

        mid = (left + right) // 2

        merge_sort(arr,left, mid)
        merge_sort(arr, mid+1, right)
        merge(arr, left, mid, right)


def merge(arr, left, mid, right):
    i = left
    j = mid + 1
    k = left
    B = [0] * (right + 1)

    while i <= mid and j <= right:
        if arr[i] < arr[j]:
            B[k] = arr[i]
            i += 1
        else:
            B[k] = arr[j]
            j += 1
        k += 1

    while i <= mid:
        B[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        B[k] = arr[j]
        j += 1
        k += 1

    for i in range(left, right + 1):
        arr[i] = B[i]

    #print(arr)


if __name__ == '__main__':
    import random
    unsorted_100_list = [random.randint(1, 1000) for _ in range(100)]
    unsorted_1000_list = [random.randint(1, 1000) for _ in range(1000)]
    unsorted_10000_list = [random.randint(1, 1000) for _ in range(10000)]
    unsorted_100000_list = [random.randint(1, 1000) for _ in range(100000)]
    unsorted_200000_list = [random.randint(1, 1000) for _ in range(200000)]

    TestExecutor.execute_function(
        [
            [[3, 5, 8, 9, 6, 2], 0, 5],
            [unsorted_100_list, 0, 99],
            [unsorted_1000_list, 0, 999],
            [unsorted_10000_list, 0, 9999],
            [unsorted_200000_list, 0, 199999]
        ],
        merge_sort
    )
