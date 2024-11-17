from tests import TestExecutor


def compareVersion(version_1: str, version_2: str) -> int:

    def get_next_chunk(version, str_len, char_point):

        if char_point > str_len - 1:
            return 0, char_point

        point_end = char_point
        while point_end < str_len and version[point_end] != '.':
            point_end += 1

        i = int(version[char_point: point_end]) if point_end != str_len - 1 else int(version[char_point: str_len])

        char_point = point_end + 1
        return i, char_point

    pointer_1 = pointer_2 = 0
    n1, n2 = len(version_1), len(version_2)
    while pointer_1 < n1 or pointer_2 < n2:

        chunk_1, pointer_1 = get_next_chunk(version_1, n1, pointer_1)
        chunk_2, pointer_2 = get_next_chunk(version_2, n2, pointer_2)

        if chunk_1 != chunk_2:
            return -1 if chunk_1 < chunk_2 else 1

    return 0


if __name__ == '__main__':
    TestExecutor.execute_function([
        ["1.2", "1.10"],
        ["1.01", "1.001"],
        ["1.0", "1.0.0.0"],
        ["1.08", "1.0"]
    ],
    [
        -1,
        0,
        0,
        1
    ],
        compareVersion
    )
