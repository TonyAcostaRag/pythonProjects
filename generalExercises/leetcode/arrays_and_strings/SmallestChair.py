from tests import TestExecutor


def smallest_chair(times: list[int], target_friend: int) -> int:

    n = len(times)
    events = []
    for i in range(n):
        events.append([times[i][0], i])
        events.append([times[i][1], ~i])

    events.sort()

    available_chairs = list(range(n))
    occupied_charis = []

    return 1


if __name__ == '__main__':
    TestExecutor.execute_function([
        [[[1,4],[2,3],[4,6]], 1],
        [[[3,10],[1,5],[2,6]], 0]
    ],
    [
        1,
        2
    ],
        smallest_chair
    )
