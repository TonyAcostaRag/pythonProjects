from tests import TestExecutor


def arrayRankTransform(arr: list[int]) -> list[int]:
    arr_copy = sorted(arr)
    rank_dict = {}
    for i in range(len(arr_copy)):
        if i == 0:
            rank_dict[arr_copy[i]] = 1
            continue

        if arr_copy[i] == arr_copy[i-1]:
            rank_dict[arr_copy[i]] = rank_dict[arr_copy[i-1]]
        else:
            rank_dict[arr_copy[i]] = rank_dict[arr_copy[i-1]] + 1

    for i in range(len(arr)):
        arr[i] = rank_dict[arr[i]]

    return arr


if __name__ == '__main__':
    TestExecutor.execute_function([
        [[40,10,20,30]],
        [[100, 100, 100]],
        [[37, 12, 28, 9, 100, 56, 80, 5, 12]]
    ],
    [
        [4, 1, 2, 3],
        [1, 1, 1],
        [5, 3, 4, 2, 8, 6, 7, 1, 3]
     ],
        arrayRankTransform
    )
