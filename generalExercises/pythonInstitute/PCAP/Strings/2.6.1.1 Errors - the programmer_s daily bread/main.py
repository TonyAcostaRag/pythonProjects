
import math

def calculate_Sqrt_test(user_input):
    inputValidation = True

    while ( inputValidation):

        print("User input:", user_input) # Test suite
        for i in range(0, len(user_input)):

            if user_input[i] == "-":
                return "Bad" # Test suite
            elif user_input[i] == ".":
                pass
            elif not user_input[i].isalpha() and not user_input[i].isdigit():
                return "Bad" # Test suite
            elif user_input[i].isalpha():
                return "Bad" # Test suite

            if i == len(user_input)-1:
                inputValidation = False

    x = float(user_input)

    return math.sqrt(x) # Test suite

def calculate_Sqrt():
    inputValidation = True

    while ( inputValidation):
        user_input = input("Enter a number equal or greater than 0: ")
        for i in range(0, len(user_input)):

            if user_input[i] == "-":
                break
            elif user_input[i] == ".":
                pass
            elif not user_input[i].isalpha() and not user_input[i].isdigit():
                break
            elif user_input[i].isalpha():
                break

            if i == len(user_input)-1:
                inputValidation = False

    x = float(user_input)
    y = math.sqrt(x)
    print("The square root of", user_input, "equals to", y)

    return y
