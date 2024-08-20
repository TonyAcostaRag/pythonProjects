
from Queues.AddingQueue import *
from tests.TestLogs.TestReports import TestResult


def test_put_elements(expectedElements):
    queue_one = AddingQueue()
    testReport = TestResult()

    queue_one.put(1)
    queue_one.put("dog")
    queue_one.put(False)

    print("Before deletion:")
    print("Printing the __dict__ property: ", queue_one.__dict__)
    print("--->Private property: ", queue_one._Queue__queue)
    del queue_one._Queue__queue
    print("After deletion:")
    print("Printing the __dict__ property: ", queue_one.__dict__)

    testReport.testResult(expectedElements, queue_one.get_total_elements())

def test_get_elements(expectedRemovals):
    queue_one = AddingQueue()
    testReport = TestResult()

    queue_one.put(1)
    queue_one.put("dog")
    queue_one.put(False)

    queue_one.get()
    queue_one.get()
    queue_one.get()

    print("Printing the __dict__ property: ", queue_one.__dict__)

    testReport.testResult(expectedRemovals, queue_one.get_total_elements())

def test_QueueError_Exception():
    queue_one = AddingQueue()
    testReport = TestResult()

    queue_one.put(1)
    queue_one.put("dog")
    queue_one.put(False)

    try:
        for i in range(5):
            queue_one.get()
    except QueueError:
        print("Queue is empty.")

    print("Printing the __dict__ property: ", queue_one.__dict__)

    testReport.testResult(0, queue_one.get_total_elements())

def test_isQueueEmpty_method():
    queue_one = AddingQueue()
    testReport = TestResult()

    queue_one.put(1)
    queue_one.put("dog")
    queue_one.put(False)

    for i in range(4):
        if not queue_one.isQueueEmpty():
            print(queue_one.get())
        else:
            print("Queue empty")

    print("Printing the __dict__ property: ", queue_one.__dict__)

    testReport.testResult(0, queue_one.get_total_elements())


if __name__ == "__main__":
    test_put_elements(3)
    test_get_elements(0)
    test_QueueError_Exception()
    test_isQueueEmpty_method()
