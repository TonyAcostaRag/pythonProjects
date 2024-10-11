from datetime import datetime


def execute_function(test_inputs, expected_values, function):

    failed_tc_dict = {}
    for i in range(len(test_inputs)):
        start_time = datetime.now()
        print(
            '\n  Actual result:', function(*test_inputs[i]),
            'Expected result:', expected_values[i],
            'Elapsed time:', datetime.now() - start_time,
            'Test input:', *test_inputs[i]
        )
        actual_result = function(*test_inputs[i])
        if actual_result == expected_values[i]:
            print('Test:', i+1, 'PASSED')
        else:
            print('Test:', i+1, 'FAILED')
            failed_tc_dict[(i+1)] = actual_result

    if len(failed_tc_dict) > 0:
        print('\n---> TEST SUITE FAILED\n---> Failing TCs:')
        for key, value in failed_tc_dict.items():
            print('Test case:', key, 'Result:', value)
    else:
        print('\n---> ALL TEST SUITE PASSED')
