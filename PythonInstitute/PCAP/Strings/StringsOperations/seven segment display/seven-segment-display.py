digits = [
    '1111110',  # 0
    '0110000',  # 1
    '1101101',  # 2
    '1111001',  # 3
    '0110011',  # 4
    '1011011',  # 5
    '1011111',  # 6
    '1110000',  # 7
    '1111111',  # 8
    '1111011',  # 9
]


def print_number(num):
    # 2. Indexing the digits lists.
    input_digits = []
    for ch in range(0, len(num)):
        input_digits.append(digits[int(num[int(ch)])])

    # 3. Fill the List to print the lines.
    display_list = [ [ [0, 0, 0] for i in range(0, len(num)) ] for j in range(0, 5 ) ]

    for digit in range(0, len(input_digits)):
        for segment in range(0, len(input_digits[digit])):

            if segment == 0:
                if input_digits[digit][segment] == '1':
                    display_list[0][digit][0] = '#'
                    display_list[0][digit][1] = '#'
                    display_list[0][digit][2] = '#'
            elif segment == 1:
                if input_digits[digit][segment] == '1':
                    display_list[0][digit][2] = '#'
                    display_list[1][digit][2] = '#'
                    display_list[2][digit][2] = '#'
            elif segment == 2:
                if input_digits[digit][segment] == '1':
                    display_list[2][digit][2] = '#'
                    display_list[3][digit][2] = '#'
                    display_list[4][digit][2] = '#'
            elif segment == 3:
                if input_digits[digit][segment] == '1':
                    display_list[4][digit][0] = '#'
                    display_list[4][digit][1] = '#'
                    display_list[4][digit][2] = '#'
            elif segment == 4:
                if input_digits[digit][segment] == '1':
                    display_list[2][digit][0] = '#'
                    display_list[3][digit][0] = '#'
                    display_list[4][digit][0] = '#'
            elif segment == 5:
                if input_digits[digit][segment] == '1':
                    display_list[0][digit][0] = '#'
                    display_list[1][digit][0] = '#'
                    display_list[2][digit][0] = '#'
            elif segment == 6:
                if input_digits[digit][segment] == '1':
                    display_list[2][digit][0] = '#'
                    display_list[2][digit][1] = '#'
                    display_list[2][digit][2] = '#'

    for file_list in display_list:
        print()
        for list in file_list:
            print("", end="  ")
            for i in list:
                if i == '#':
                    print(i, end="")
                else:
                    print(" ", end="")

print_number(input("Enter the number you wish to display: "))
