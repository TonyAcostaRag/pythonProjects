
line = input("Enter a line of numbers: ")
if len(line) > 0:
    total = sum([ float(i) for i in line.split() ])
    print("The total is:", total)
else:
    print("No number introduced")
