import calendar as cal

"""
 Printing the calendar.
"""
print(cal.calendar(2024, 3, 1, 6, 6))
cal.prcal(2024, 3, 1, 6, 6)

print(cal.month(2024, 3, 3, 1))
cal.prmonth(2024, 3, 3, 1)

"""
Setting a different first day of week.
"""
cal.setfirstweekday(cal.SUNDAY)

"""
Printing the calendar of a given month.
"""
cal.prmonth(2024, 3, 3)

"""
Week operations.
"""
print("\nWeekday: ", cal.weekday(2024, 3, 16))
print('Weekheader:', cal.weekheader(2))

"""
Determining the leap years.
"""
print('\nIs 2020 a leap year?', cal.isleap(2020))
print('Is 2024 a leap year?', cal.isleap(2024))

print('How many leap years have elapsed from 2020 to 2024?', cal.leapdays(2020, 2024))

"""
Creating Calendar objects.
"""
cal1 = cal.Calendar(cal.SUNDAY)
print('\nPrinting the weekdays:')
for day in cal1.iterweekdays():
    print(day, end=' ')

print()
print('\nPrinting the days of the given month:')
for day in cal1.itermonthdates(2024, 3):
    print(day, end=', ')

print()
print('\nPrinting the days of the given month:')
for day in cal1.itermonthdays(2024, 3):
    print(day, end=', ')

print()
print('\nPrinting the days of the given month:')
count = 0
for day in cal1.itermonthdays2(2024, 3):
    print(day, end=', ')
    count += 1
print()
print(count)

print()
print('\nPrinting the days of the given month:')
count = 0
for day in cal1.itermonthdays3(2024, 3):
    print(day, end=', ')
    count += 1
print()
print(count)

print()
print('\nPrinting the days of the given month:')
count = 0
for day in cal1.itermonthdays4(2024, 3):
    print(day, end=', ')
    count += 1
print()
print(count)

print()
print('\nPrinting the weeks of the given month:')
count = 0
for day in cal1.monthdays2calendar(2024, 3):
    print(day)
    count += 1
print()
print(count)
