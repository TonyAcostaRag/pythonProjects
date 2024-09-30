from tests import TestExecutor


def trap(height: list[int]) -> int:
    if len(height) == 0:
        return 0
    left_max = [0] * len(height)
    right_max = [0] * len(height)
    total_trapped_water = 0

    left_max[0] = height[0]
    for i in range(1, len(height)):
        left_max[i] = max(height[i], left_max[i-1])

    right_max[-1:] = height[-1:]
    for i in range(len(height)-2, -1, -1):
        right_max[i] = max(height[i], right_max[i+1])

    for i in range(1, len(height)-1):
        total_trapped_water += min(left_max[i], right_max[i]) - height[i]

    return total_trapped_water


if __name__ == '__main__':
    TestExecutor.execute_function([
        [[0,1,0,2,1,0,1,3,2,1,2,1]]
    ],
    [6],
        trap
    )
