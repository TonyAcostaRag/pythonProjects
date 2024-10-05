from tests import TestExecutor


def largestUniqueNumber(nums: list[int]) -> int:
    nums_list = [0] * 2001
    for i in range(len(nums)):
        nums_list[nums[i]] += 1

    for i in range(len(nums_list) - 1, -1, -1):
        if nums_list[i] == 1:
            return i

    return -1


if __name__ == '__main__':
    TestExecutor.execute_function([
        [[5, 7, 3, 9, 4, 9, 8, 3, 1]],
        [[9,9,8,8]]
    ],
    [
        8,
        -1
    ],
        largestUniqueNumber
    )
