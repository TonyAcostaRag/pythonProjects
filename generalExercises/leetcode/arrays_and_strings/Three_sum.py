from tests import TestExecutor


def three_sum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    triplets = []
    for i in range(len(nums) - 2):

        left = i + 1
        right = len(nums) - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]

            if sum == 0:
                if [nums[i], nums[left], nums[right]] not in triplets:
                    triplets.append([nums[i], nums[left], nums[right]])
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
            elif sum > 0:
                right -= 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            else:
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
    return triplets


if __name__ == '__main__':
    TestExecutor.execute_function([
        [[-1, 0, 1, 2, -1, -4]],
        [[0,1,1]],
        [[0,0,0]]
    ],
    [
        [[-1, -1, 2], [-1, 0, 1]],
        [],
        [[0, 0, 0]]
    ],
        three_sum
    )
