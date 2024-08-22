
print('''
-------------------------------------------------
-- Indexing Strings.
-------------------------------------------------
    ''')

# Indexing strings.
print('\nPositive indexes')
the_string = 'silly walks'

for ix in range(len(the_string)):
    print(ix, end= ' ')
    print(the_string[ix])

print()

# Negative indexing strings.
print('\nNegative indexes')
the_string = 'silly walks'


for ix in range(len(the_string), 0, -1):
    print((ix * (-1)), end= ' ')
    print(the_string[(ix * (-1))])

print()

# Backwards indexing strings.
print('\nBackward indexes')
the_string = 'silly walks'


for ix in range(len(the_string)-1, -1, -1):
    print((ix * (-1)), end= ' ')
    print(the_string[ix])

print()



print('''
-------------------------------------------------
-- Iterating Strings.
-------------------------------------------------
    ''')
# Iterating through a string.

the_string = 'silly walks'

for character in the_string:
    print(character)

print()


