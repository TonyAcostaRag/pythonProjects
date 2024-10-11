from tests import TestExecutor


def maxWidthRamp(nums: list[int]) -> int:

    n = len(nums)
    rightMax = [0] * n
    rightMax[n - 1] = nums[n - 1]
    for i in range(n - 2, -1, -1):
        rightMax[i] = max(rightMax[i + 1], nums[i])
        #print('Index: ', i, 'rightMax', rightMax)
    '''print(
        '\nLength of nums: ', n,
        '\nnums: ', nums,
        '\nrightMax: ', rightMax,
    )'''
    left = 0
    right = 0
    maxWidth = 0

    while right < n:
        '''print(
            '\nnums: ', nums,
            '\nrightMax: ', rightMax,
            '\nleft: ', left,
            '\nright:', right,
            '\nmaxWidth:', maxWidth
        )
        print('\nnums[left] > rightMax[right]')
        print(nums[left], ' > ', rightMax[right])'''
        while nums[left] > rightMax[right]:
            left += 1
        maxWidth = max(maxWidth, right - left)
        right += 1

    return maxWidth


if __name__ == '__main__':
    TestExecutor.execute_function([
        [[6,0,8,2,1,5]],
        [[9,8,1,0,1,9,4,0,4,1]],
        [[9,8,7,6,5,4,3,2,1,0]],
        [[9,8,1,0,1,8,4,0,4,1]]
    ],
    [
        4,
        7,
        0,
        7
    ],
        maxWidthRamp
    )
