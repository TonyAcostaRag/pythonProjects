from tests import TestExecutor


def rotate(matrix: list[list[int]]) -> None:
    n = len(matrix)
    for i in range(n // 2 + n % 2):
        for j in range(n // 2):

            temp = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
            matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = matrix[i][j]
            matrix[i][j] = temp
    return matrix


if __name__ == '__main__':
    TestExecutor.execute_function([
        [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]],
        [[[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]],
        [[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]],
        [[
            [1, 2, 3, 4, 5, 6, 7],
            [8, 9, 10, 11, 12, 13, 14],
            [15, 16, 17, 18, 19, 20, 21],
            [22, 23, 24, 25, 26, 27, 28],
            [29, 30, 31, 32, 33, 34, 35],
            [36, 37, 38, 39, 40, 41, 42],
            [43, 44, 45, 46, 47, 48, 49],
        ]]
    ],
    [
        [[7, 4, 1], [8, 5, 2], [9, 6, 3]],
        [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]],
        [[21, 16, 11, 6, 1], [22, 17, 12, 7, 2], [23, 18, 13, 8, 3], [24, 19, 14, 9, 4], [25, 20, 15, 10, 5]],
        [[43, 36, 29, 22, 15, 8, 1],
         [44, 37, 30, 23, 16, 9, 2],
         [45, 38, 31, 24, 17, 10, 3],
         [46, 39, 32, 25, 18, 11, 4],
         [47, 40, 33, 26, 19, 12, 5],
         [48, 41, 34, 27, 20, 13, 6],
         [49, 42, 35, 28, 21, 14, 7]]
    ],
        rotate
    )