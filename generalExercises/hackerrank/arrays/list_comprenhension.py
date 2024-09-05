from tests import TestExecutor


def coordinates(x, y, z, n):

    valid_coordinates = list(filter(lambda x: sum(x) != n,
                                    [[i, j, k] for k in range(0, z + 1) for j in range(0, y + 1) for i in range(0, x + 1)]))

    valid_coordinates.sort()

    print(valid_coordinates)


TestExecutor.execute_function(
    [
        [2, 2, 2, 2],
        [1, 1, 1, 2]],
    coordinates)
