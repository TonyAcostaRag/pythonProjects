from tests import TestExecutor
import heapq


def longestDiverseString(a: int, b: int, c: int) -> str:
    pq = []
    happy_string = ''
    if a > 0:
        heapq.heappush(pq, (-a, 'a'))
    if b > 0:
        heapq.heappush(pq, (-b, 'b'))
    if c > 0:
        heapq.heappush(pq, (-c, 'c'))

    while pq:
        count, letter = heapq.heappop(pq)
        count = -count
        if (
            len(happy_string) >= 2
            and happy_string[-1] == letter
            and happy_string[-2] == letter
        ):
            if not pq:
                break
            next_frequent_count, next_frequent_letter = heapq.heappop(pq)
            happy_string += next_frequent_letter
            if next_frequent_count + 1 < 0:
                heapq.heappush(pq, (next_frequent_count + 1, next_frequent_letter))
            heapq.heappush(pq, (-count, letter))
        else:
            happy_string += letter
            count -= 1
            if count > 0:
                heapq.heappush(pq, (-count, letter))

    return happy_string


if __name__ == '__main__':
    TestExecutor.execute_function([
        [1, 1, 7],
        [7, 1, 0],
        [2, 2, 1]
    ],
    [
        'ccaccbcc',
        'aabaa',
        'ababc'
    ],
        longestDiverseString
    )
