def repeatedString(s, n):
    # 1. Define the total char within a string
    # 2. Multiply the total char in a string by the total strings
    # 3. Add the char in the substring if any
    total_a_count = 0
    repeated_strings = n // len(s)

    if len(s) > 1:
        partial_string = s[:n % len(s)]
    else:
        partial_string = []

    for char in s:
        if char == 'a':
            total_a_count += 1

    total_a_count *= repeated_strings

    for char in partial_string:
        if char == 'a':
            total_a_count += 1

    print('\n'+s+str(partial_string))
    return total_a_count


print(repeatedString('abc', 10))
print(repeatedString('a', 1000000000000))
print(repeatedString('naranja', 11))
print(repeatedString('flores', 11))
print(repeatedString('aa', 11))
print(11%2)
print('antonio'[:])
print('antonio'[:1])
print('antonio'[:1+1])
print('antonio'[:-1])
