from tests import TestExecutor

def minimumBribes(q):

    total_bribes = 0
    i = 0
    while i < len(q):

        if q[i] > (i+1):
            person_bribes = q[i] - (i+1)
            if person_bribes > 2:
                print('Too chaotic')
                return
            total_bribes += person_bribes

        i += 1

    print(total_bribes)


TestExecutor.execute_function(
    [
        [[2, 1, 5, 3, 4]],
        [[2, 5, 1, 3, 4]],
        [[5, 1, 2, 3, 7, 8, 6, 4]],
        [[1, 2, 5, 3, 7, 8, 6, 4]],
        [[1, 2, 5, 3, 4, 7, 8, 6]],
        [[3, 1, 2, 4, 5]],
        [[3, 2, 1, 4, 5]],
        [[1, 2, 3, 5, 7, 4, 6, 8]],
    ],
    minimumBribes
)
