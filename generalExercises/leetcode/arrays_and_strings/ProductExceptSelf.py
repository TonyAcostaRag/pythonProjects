from tests import TestExecutor


def product_except_self(nums: list[int]) -> list[int]:

    left = [0] * len(nums)
    for i in range(len(left)):
        if i == 0:
            left[i] = 1
        else:
            left[i] = left[i-1] * nums[i-1]

    right = [0] * len(nums)
    for i in range(len(right) - 1, -1, -1):
        if i == len(right) - 1:
            right[i] = 1
        else:
            right[i] = right[i+1] * nums[i+1]

    return [left[i] * right[i] for i in range(len(nums))]


if __name__ == '__main__':
    TestExecutor.execute_function([
        [[1, 2, 3, 4]],
        [[-1, 1, 0, -3, 3]]
    ], [
        [24, 12, 8, 6],
        [0, 0, 9, 0, 0]
    ],
        product_except_self
    )
