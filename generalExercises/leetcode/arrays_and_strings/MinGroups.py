from tests import TestExecutor


def min_group(intervals: list[list[int]]) -> int:

    range_start = intervals[0][0]
    range_end = intervals[0][1]
    for interval in intervals:
        range_start = min(range_start, interval[0])
        range_end = max(range_end, interval[1])

    point_to_count = [0] * (range_end + 2)
    for interval in intervals:
        point_to_count[interval[0]] += 1
        point_to_count[interval[1] + 1] -= 1

    concurrent_interval = 0
    max_concurrent_interval = 0
    for i in range(range_start, range_end + 1):
        concurrent_interval += point_to_count[i]
        max_concurrent_interval = max(max_concurrent_interval, concurrent_interval)

    return max_concurrent_interval


if __name__ == '__main__':
    TestExecutor.execute_function([
        [[[5,10],[6,8],[1,5],[2,3],[1,10]]],
        [[[1,3],[5,6],[8,10],[11,13]]]
    ],
    [
        3,
        1
    ],
        min_group
    )
