def rotLeft(a, d):

    rotated_array = a[d:]
    rotated_array += a[:d]

    print(a)
    print(rotated_array)

    return rotated_array


result = rotLeft(
    [1, 2, 3, 4, 5], 4
)
