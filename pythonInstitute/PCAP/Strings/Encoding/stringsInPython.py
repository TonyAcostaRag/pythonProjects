# Example 1

print(
'''
-------------------------------------------------
-- Verifing the length of different strings... --
-------------------------------------------------
''')

word = 'by'
print(len(word))


# Example 2

empty = ''
print(len(empty))


# Example 3

i_am = 'I\'m'
print(len(i_am))

print(i_am)

multiline = '''Line #1


Line #2'''

print(len(multiline))
print(multiline)


# String operations.
print(
'''
-------------------------------------------------
-- Operations with strings.
-- Concatenations (No commutative).
-- Replicate (commutative).
-------------------------------------------------
''')


str1 = 'a'
str2 = 'b'

print(str1 + str2)
print(str2 + str1)
print(5 * 'a')
print('b' * 4)


# Demonstrating the ord() function.
print(
'''
-------------------------------------------------
-- Demonstrating the ord() function.
-------------------------------------------------
''')


char_1 = 'a'
char_2 = ' '  # space

print(ord(char_1))
print(ord(char_2))


print('Printing code point directly without variables')
print(ord(' '))
print(ord('a'))

print('\nPrinting code points of a greek and polish alphabets (α, ę)')
print(ord('α'))
print(ord('ę'))


# Demonstrating the chr() function.
print(
'''
-------------------------------------------------
-- Demonstrating the chr() function.
-------------------------------------------------
''')


print('chr(ord(\'a\')) == \'a\':')

if chr(ord('a')) == 'a':
    print('This is true')
    print('Code point of a is: ', end = ' ')
    print(ord('a'))

if ord(chr(111)) == 111:
    print('This is true')
    print('Char of 111 is: ' + chr(111))









