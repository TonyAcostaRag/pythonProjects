from tests import TestExecutor


def maxArea(height: list[int]) -> int:

    left = 0
    right = len(height) - 1
    max_Area = 0
    while left < right:
        area = (right - left) * min(height[left], height[right])
        max_Area = max(max_Area, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_Area


if __name__ == '__main__':
    TestExecutor.execute_function([
        [[1,8,6,2,5,4,8,3,7]],
        [[1,1]]
    ],
    [
        49,
        1
    ],
        maxArea
    )
