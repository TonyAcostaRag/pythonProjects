import sys


print('By default the standard input is from the keyboard')
for line in sys.stdin:
    if line.rstrip() == 'q':
        break
    print(line)

print('You pressed q, so I want to quit now')
