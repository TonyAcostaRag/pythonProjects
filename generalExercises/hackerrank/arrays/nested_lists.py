from tests import TestExecutor


def second_lowest(student_list):

    student_list.sort()
    print(student_list)

    lowest_score = student_list[0][1]
    for i in range(0, len(student_list)):
        if student_list[i][1] < lowest_score:
            lowest_score = student_list[i][1]

    print(lowest_score)

    second_lowest = []
    for i in range(0, len(student_list)):

        if student_list[i][1] == lowest_score:
            continue
        elif student_list[i][1] > lowest_score:
            if len(second_lowest) != 0:
                if student_list[i][1] < second_lowest[0][1]:
                    second_lowest.clear()
                    second_lowest.append(student_list[i])
                elif student_list[i][1] == second_lowest[0][1]:
                    second_lowest.append(student_list[i])
            else:
                second_lowest.append(student_list[i])

    for i in second_lowest:
        print(i[0])


TestExecutor.execute_function(
    [
        [[['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]],
        [[['Rachel', -50], ['Mawer', -50], ['Sheen', -50], ['Shaheen', 51]]],
    ],
    second_lowest
)
