import datetime as dt

dt1 = dt.datetime(2020, 11, 4, 14, 53)

"""
2020/11/04 14:53:00
20/November/04 14:53:00 PM
Wed, 2020 Nov 04
Wednesday, 2020 November 04
Weekday: 3
Day of the year: 309
Week number of the year: 44
"""

print(dt1.strftime('%Y/%m/%d %H:%M:%S'))
print(dt1.strftime('%y/%B/%d %H:%M:%S %p'))
print(dt1.strftime('%a, %Y %b %d'))
print(dt1.strftime('%A, %Y %B %d'))
print(dt1.strftime('Weekday: %w'))
print(dt1.strftime('Day of the year: %-j'))
print(dt1.strftime('Week number of the year: %-W'))
