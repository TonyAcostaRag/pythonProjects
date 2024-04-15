
class TestResult:

    def __init__(self):
        pass

    def testResult(self, expectedResult,actualResult):

        print("Expected: ", expectedResult)
        print("Actual: ", actualResult)

        if actualResult == expectedResult:
            print("-----------", "---> PASSED", "-----------", sep="\n")
        else:
            print("-----------", "---> FAILED", "-----------", sep="\n")