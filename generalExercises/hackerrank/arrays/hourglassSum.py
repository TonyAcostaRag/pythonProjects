def hourglassSum(arr):
    # 1. Define the 16th existing hourglass within the array.
    hourglass_sum_list = []

    x = 2
    y = 2
    while y < 6:

        while x < 6:
            h1 = arr[y - 2][x - 2]
            h2 = arr[y - 2][x - 1]
            h3 = arr[y - 2][x]
            b = arr[y - 1][x - 1]
            f1 = arr[y][x - 2]
            f2 = arr[y][x - 1]
            f3 = arr[y][x]

            hourglass_sum_list.append(h1 + h2 + h3 + b + f1 + f2 + f3)
            x += 1

        y += 1
        x = 2

    for i in range(0, len(hourglass_sum_list)):

        if i % 4 == 0 and i != 0:
            print()
        print(hourglass_sum_list[i], end=' ')

    return max(hourglass_sum_list)


hourglassSum(
    [
        [1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 2, 4, 4, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 1, 2, 4, 0]
    ]
)
