from tests import TestExecutor


def canArrange(arr, k):

    remainder_Count = {}
    for i in range(len(arr)):
        if arr[i] % k not in remainder_Count:
            remainder_Count[arr[i] % k] = 1
        else:
            remainder_Count[arr[i] % k] += 1

    for i in range(len(arr)):
        if arr[i] % k == 0:
            if remainder_Count[0] % 2 != 0:
                return False
        else:
            if (k - arr[i] % k) in remainder_Count:
                if remainder_Count[arr[i] % k] != remainder_Count[k - (arr[i] % k)]:
                    return False
            else:
                return False

    return True


if __name__ == '__main__':
    TestExecutor.execute_function([
        [[1,2,3,4,5,10,6,7,8,9], 5],
        [[1,2,3,4,5,6], 7],
        [[1,2,3,4,5,6], 10]
    ],
        [True, True, False],
        canArrange)
