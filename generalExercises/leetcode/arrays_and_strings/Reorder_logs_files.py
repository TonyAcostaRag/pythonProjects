from tests import TestExecutor


def reorderLogFiles(logs: list[str]) -> list[str]:

    def get_key(log):
        _id, content = log.split(" ", maxsplit=1)
        return (0, content, _id) if content[0].isalpha() else (1, None)

    return sorted(logs, key=get_key)


TestExecutor.execute_function(
    [
        [["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]],
        [["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]]
    ],
    [
        ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"],
        ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
    ],
    reorderLogFiles
)
