from main import calculate_Sqrt_test

testData = ["!", "%", "°", "|", "/", "f", "-f", "-", "-1", "25.5", "25.", "25"]

testObjective = ["Invalid symbol",
                 "Invalid symbol",
                 "Invalid symbol",
                 "Invalid symbol",
                 "Invalid symbol",
                 "Invalid letter",
                 "Invalid symbol",
                 "Invalid symbol",
                 "Invalid negative number",
                 "Valid positive",
                 "Valid positive",
                 "Valid positive"]
expectedResult = ["Bad", "Bad", "Bad", "Bad", "Bad", "Bad", "Bad",
                "Bad", "Bad", 5.049752469181039, 5.0, 5.0]

total_pass = 0
total_fail = 0
print()
for i in range(0, len(testData)):
    functionResult = calculate_Sqrt_test(testData[i])
    print("TC", i+1, ": ", testObjective[i], sep="")
    print("Actual result:\t\t", functionResult)
    print("Expected result:\t", expectedResult[i])
    if functionResult == expectedResult[i]:
        print("PASSED\n")
        total_pass += 1
    else:
        print("FAILED\n")
        total_fail += 1

print("Total PASSED:", total_pass)
print("Total FAILED:", total_fail)
