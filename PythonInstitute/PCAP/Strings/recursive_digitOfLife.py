def calculateDigitOfLife(dob):
    digit = 0

    for ch in dob:
        digit += int(ch)

    if len(str(digit)) == 1:
        return digit
    else:
        return calculateDigitOfLife(str(digit))

testData = ["19991229", "20000101"]
expectedResult = [6, 4]

for i in range(0, len(testData)):
    if calculateDigitOfLife(testData[i]) == expectedResult[i]:
        print("TC", i+1, " PASSED")
    else:
        print("TC", i+1, " FAILED")
