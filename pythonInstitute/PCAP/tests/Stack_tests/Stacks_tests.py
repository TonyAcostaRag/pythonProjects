
from Stacks.AddingStack import AddingStack
from tests.TestLogs.TestReports import TestResult

def test_sum_values(expectedSum):
    stack_object = AddingStack()
    testResult = TestResult()

    for i in range(5):
        stack_object.push(i)
    print("Sum of the stacked values:", stack_object.get_sum())
    testResult.testResult(expectedSum, stack_object.get_sum())
    print("End of test_sum_values")
    print("----" * 10)

def test_called_pushes(expected_Pushes):
    stack_object = AddingStack()
    testResult = TestResult()

    for i in range(expected_Pushes):
        stack_object.push(i)

    print("Total pushes:", stack_object.get_total_pushes())
    testResult.testResult(expected_Pushes, stack_object.get_total_pushes())
    print("End of test_called_pushes")
    print("----" * 10)

def test_called_pops(expected_Pops):
    stack_object = AddingStack()
    testResult = TestResult()

    for i in range(expected_Pops):
        stack_object.push(i)

    for i in range(expected_Pops):
        stack_object.pop()

    print("Total pops:", stack_object.get_total_pops())
    testResult.testResult(expected_Pops, stack_object.get_total_pops())
    print("End of test_called_pops")
    print("----" * 10)


if __name__ == "__main__":
    test_sum_values(10)
    test_called_pushes(100)
    test_called_pops(100)
