from tests import TestExecutor


def two_sum(array, target) -> list[int]:

    traversed_values = {}
    result_list = []
    for i in range(len(array)):
        if len(traversed_values) == 0:
            traversed_values[array[i]] = i
            continue

        if (target - array[i]) in traversed_values.keys():
            result_list.append(i)
            result_list.append(traversed_values.get(target - array[i]))
            return result_list
        else:
            traversed_values[array[i]] = i


TestExecutor.execute_function([
    [[2, 7, 11, 15], 9],
    [[3, 2, 4], 6],
    [[3, 5, 1, 4, -8], 5],
    [[3, 4, 9, 6, 4], 8],
    [[4, -2, 5, 0, 6, 3, 2, 7], 1]
], two_sum)
