from datetime import datetime


def execute_function(test_inputs, expected_values, function):

    failed_tc_list = []
    for i in range(len(test_inputs)):
        start_time = datetime.now()
        print('Function return:', function(*test_inputs[i]))
        print('Elapsed time:', datetime.now() - start_time)
        if function(*test_inputs[i]) == expected_values[i]:
            print('Test:', i+1, 'PASSED')
        else:
            print('Test:', i+1, 'FAILED')
            failed_tc_list.append(i+1)

    if len(failed_tc_list) > 0:
        print('\n---> TEST SUITE FAILED\n---> Failing TCs:')
        for i in failed_tc_list:
            print(i)

