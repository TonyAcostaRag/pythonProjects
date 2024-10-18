from tests import TestExecutor
import heapq


def smallest_range(nums: list[list[int]]) -> list[int]:

    pq = []
    max_val = float('-inf')
    range_start = 0
    range_end = float('inf')
    for i in range(len(nums)):
        heapq.heappush(pq, (nums[i][0], i, 0))  # Value, list_index, element_index.
        max_val = max(max_val, nums[i][0])

    while len(pq) == len(nums):

        min_val, row, col = heapq.heappop(pq)

        if max_val - min_val < range_end - range_start:
            range_end = max_val
            range_start = min_val

        if col + 1 < len(nums[row]):
            next_val = nums[row][col + 1]
            heapq.heappush(pq, (next_val, row, col + 1))
            max_val = max(max_val, next_val)

    return [range_start, range_end]


if __name__ == '__main__':
    TestExecutor.execute_function([
        [[[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]],
        [[[1, 2, 3], [1, 2, 3], [1, 2, 3]]],
        [[[0, 0, 1, 1, 2], [40, 50, 60], [45, 55, 65]]]
    ],
    [
        [20, 24],
        [1, 1],
        [2, 45]
    ],
        smallest_range
    )
