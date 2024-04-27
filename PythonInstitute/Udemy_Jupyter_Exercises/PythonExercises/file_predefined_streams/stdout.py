import sys


print('''By default the standard output is the console
If other string is written to the console it will 
be concatenated to the previous string written''')
sys.stdout.write('\nDefault writting goes to the console')
sys.stdout.write('\tConcatenated String')
