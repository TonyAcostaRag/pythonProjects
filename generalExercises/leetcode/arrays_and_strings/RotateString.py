from tests import TestExecutor


def rotate_string(s: str, goal: str) -> bool:
    double_s = s + s
    if goal in double_s and len(s) == len(goal):
        return True
    else:
        return False


if __name__ == '__main__':
    TestExecutor.execute_function([
        ["abcde", "cdeab"],
        ["abcde", "abced"]
    ], [
        True,
        False
    ],
        rotate_string
    )
