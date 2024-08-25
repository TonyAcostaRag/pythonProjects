def read_int(prompt, min, max):

    while True:
        try:
            input_value = int(input(prompt))
            assert input_value >= min
            assert input_value <= max
            break
        except ValueError:
            print("Error: wrong input")
        except AssertionError:
            print("Error: the value is not within permitted range (",min,"..",max,")", sep="")

    return input_value

v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
