print('''---------------
-- Slices
---------------''')

# Slices

alpha = "abdefg"

print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[3:-2])
print(alpha[-3:4])
print(alpha[::2])
print(alpha[1::2])


print('''\n\n------------------------------
The in and not in operators
------------------------------''')

# The in and not in operators
alphabet = "abcdefghijklmnopqrstuvwxyz"

print('The in operator')

print("f" in alphabet)
print("F" in alphabet)
print("1" in alphabet)
print("ghi" in alphabet)
print("Xyz" in alphabet)


print('\nThe not in operator')

print("f" not in alphabet)
print("F" not in alphabet)
print("1" not in alphabet)
print("ghi" not in alphabet)
print("Xyz" not in alphabet)

print(alphabet)

del alphabet

#print(alphabet)


print('\nString copy')

alphabet = "bcdefghijklmnopqrstuvwxy"

alphabet = "a" + alphabet
alphabet = alphabet + "z"

print(alphabet)


print('''\n\n------------------------------
The min operator
------------------------------''')

# Demonstrating min() - Example 1:
print('\nThe minimum element of "aAbByYzZ" is:', end= ' ')
print(min("aAbByYzZ"))
print('\nCode print of "a" is: ', end=' ')
print(ord('a'))
print('Code print of "A" is: ', end=' ')
print(ord('A'))



# Demonstrating min() - Examples 2 & 3:
t = 'The Knights Who Say "Ni!"'
print('\nThe minimum element of: "' + t + '"is: ') 
print('->' + min(t) + '<-')

t = [0, 1, 2]
print('The minimum element of', end = ' ')
print(t, end = ' ')
print('is: ')
print(min(t))


print('''\n\n------------------------------
The max operator
------------------------------''')

# Demonstrating max() - Example 1:
print('The maximum element of "aAbByYzZ" is:', end = ' ')
print(max("aAbByYzZ"))

# Demonstrating max() - Examples 2 & 3:
t = 'The Knights Who Say "Ni!"'
print('\nThe maximum element of "' + t + '" is:')
print('->' + max(t) + '<-')

t = [0, 1, 2]
print('The maximum element of', end = ' ')
print(t, end = ' ')
print('is: ')
print(max(t))


