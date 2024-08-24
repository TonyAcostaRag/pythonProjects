from datetime import datetime


def execute_function(test_input, function):
    for i in test_input:
        start_time = datetime.now()
        print(function(i))
        print('Elapsed time:', datetime.now() - start_time)
        print()
