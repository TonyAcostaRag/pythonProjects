from tests import TestExecutor


def three_sum_closest(nums: list[int], target: int) -> int:

    diff = float('inf')
    nums.sort()
    for i in range(len(nums) - 2):

        left = i + 1
        right = len(nums) - 1
        while left < right:

            sum = nums[i] + nums[left] + nums[right]
            if abs(target - sum) < diff:
                diff = target - sum
            if sum < target:
                left += 1
            else:
                right -= 1

        if diff == 0:
            break

    return target - diff


if __name__ == '__main__':
    TestExecutor.execute_function([
        [[-1,2,1,-4], 1],
        [[0,0,0], 1]
    ],
    [
        2,
        0
    ],
        three_sum_closest
    )
