from tests import TestExecutor


def two_sum(numbers: list[int], target: int) -> list[int]:
    left = 0
    right = len(numbers) - 1
    while left < right:
        sum = numbers[left] + numbers[right]

        if sum == target:
            return [left + 1, right + 1]
        elif sum > target:
            right -= 1
        else:
            left += 1

    return [-1, -1]


if __name__ == '__main__':
    TestExecutor.execute_function([
        [[2,7,11,15], 9],
        [[2,3,4], 6],
        [[-1,0], -1],
        [[2, 3, 5], 6]
    ],
    [
        [1, 2],
        [1, 3],
        [1, 2],
        [-1, -1]
    ],
        two_sum
    )
