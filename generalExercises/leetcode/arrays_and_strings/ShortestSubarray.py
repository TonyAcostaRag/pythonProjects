from tests import TestExecutor


def shortestSubarray(arr: list[int]) -> int:

    right = len(arr) - 1
    print('len(arr):', len(arr))
    while right > 0 and arr[right] >= arr[right - 1]:
        right -= 1
        print('right:', right)

    ans = right
    left = 0

    while left < right and (left == 0 or arr[left - 1] <= arr[left]):

        print(
            '\nright:', right,
            'left:', left,
            'arr[left]:', arr[left],
            'arr[right]:', arr[right],
            'ans:', ans,
            '\narr:', arr
        )

        while right < len(arr) and arr[left] > arr[right]:
            right += 1
            print(
                '\nInner while loop results:',
                'right:', right
            )

        ans = min(ans, right - left - 1)
        left += 1
        print(
            '\nOuter while loop results:',
            '\nans:', ans,
            'left:', left
        )

    return ans


if __name__ == '__main__':
    TestExecutor.execute_function([
        [[1, 2, 3, 10, 4, 2, 3, 5]],
        [[5, 4, 3, 2, 1]],
        [[1, 2, 3]]
    ],
    [
        3,
        4,
        0
    ],
        shortestSubarray
    )
