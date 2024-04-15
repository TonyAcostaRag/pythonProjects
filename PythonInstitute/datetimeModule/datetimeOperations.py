import datetime as dt
import time

"""
Date formats
"""
currentDate = dt.date.today()
print("Today date:", currentDate, " <- Date Object")
print("Current year:", currentDate.year)
print("Current month:", currentDate.month)
print("Current day:", currentDate.day)
print("Day of the week in numeric (0 -> Monday, 6 -> Sunday):", currentDate.weekday())
print("Day of the week in iso numeric format (1 -> Monday, 7 -> Sunday)", currentDate.isoweekday())
print("replacing the attributes of the date object: ")
currentDate = currentDate.replace(year=2020, month=1, day=1)
print("Today date replaced:", currentDate)

instantiatedDateObject = dt.date(1993, 12,11)
print("\nCustomized date", instantiatedDateObject, " <- Date  Object")
instantiatedDateObject = instantiatedDateObject.replace(year=2020, month=1, day=1)
print("Customized date replaced:", instantiatedDateObject)

print("\nMINYEAR constant:", dt.MINYEAR)
print("MAXYEAR constant:", dt.MAXYEAR, end="\n\n")

'''
Date objects from timestamps and iso format
'''
currentTimestamp = time.time()
print("\nCurrent timestamp: ", currentTimestamp)
print("Current timestamp data type: ", type(currentTimestamp))
dateFromTimestamp = dt.date.fromtimestamp(currentTimestamp)
print("Date made from timestamp: ", dateFromTimestamp, " <- Date  Object")
dateFromTimestamp = dateFromTimestamp.replace(year=2020, month=1, day=1)
print("Date made from timestamp replaced: ", dateFromTimestamp)


isoformatDate = '1993-12-11'
dateObjectFromIsoFormatString = dt.date.fromisoformat(isoformatDate)
print("\nDate object made from isoformat string: ", dateObjectFromIsoFormatString, " <- Date Object",
      "\nType of the date object: ", type(dateObjectFromIsoFormatString),
      "\nType of the date of the iso format: ", type(isoformatDate))

dateObjectFromIsoFormatString = dateObjectFromIsoFormatString.replace(year=2020, month=1, day=1)
print("Date object made from isoformat string replaced: ", dateObjectFromIsoFormatString)

"""
Time objects.
"""
timeStampFromTime = dt.time(20, 30, 15, 1000)
print("\nTimestamp from time class: ", timeStampFromTime)
print("Timestamp hour attribute: ", timeStampFromTime.hour)
print("Timestamp minute attribute: ", timeStampFromTime.minute)
print("Timestamp second attribute: ", timeStampFromTime.second)
print("Timestamp microsecond attribute: ", timeStampFromTime.microsecond)
print("Timestamp tzinfo attribute: ", timeStampFromTime.tzinfo)
print("Timestamp fold: ", timeStampFromTime.fold)

dateStringFromTimestamp = time.ctime(time.time())
print("\nDate string made from a timestamp: ", dateStringFromTimestamp)
print("Date string made from a timestamp data type: ", type(dateStringFromTimestamp))


latest_timestamp = time.time()
gmtimeObjectForstructTime = time.gmtime(latest_timestamp)
print("\nstruct_time class definition attributes for gmtime: ", gmtimeObjectForstructTime, sep="\n")
print("struct_time class definition attributes gmtime object type: ", type(gmtimeObjectForstructTime))

localtimeObjectForStructTime = time.localtime(latest_timestamp)
print("\nstruct_time class definition attributes for local time: ", localtimeObjectForStructTime, sep="\n")
print("struct_time class definition attributes local time object type: ", type(localtimeObjectForStructTime))

"""
Datetime methods to return the current date and time.
"""
currentDateAndTime_today = dt.datetime.today()
print('\nCurrent date and time (today method): ', currentDateAndTime_today)

currentDateAndTime_now = dt.datetime.now()
print('Current date and time (now method): ', currentDateAndTime_now)

#currentDateAndTime_utcnow = dt.datetime.utcnow() # Deprecated method used instead the below form of now()
currentDateAndTime_utcnow = dt.datetime.now(dt.UTC)
print('Current date and time (utcnow method): ', currentDateAndTime_utcnow)

dateTimeObject = dt.datetime(2023, 3, 15, 11, 11)
timestampFromDateAndTime = dateTimeObject.timestamp()
print('Current timestamp based on Date and Time: ', timestampFromDateAndTime)

dateTimeObjectTwo = dt.datetime(2023, 12, 11)
print('\nDate in the directive format: ', dateTimeObjectTwo.strftime('%Y/%m/%d'))

dateTimeObjectThree = dt.datetime(2011, 11, 11, 11, 11, 11)
timeObject = dt.time(11, 11, 11)
print('Formatted date:', dateTimeObjectThree.strftime('%Y/%m/%d %H:%m:%S'))
print('Formatted time:', timeObject.strftime('%H:%M:%S'))
print('Invalid formatted time:', timeObject.strftime('%Y:%H:%M'))

timestampOne = 1572879180
structObjectBasedOnTimestamp = time.gmtime(timestampOne)
print('\nSpecified struct time:', time.strftime('%Y/%m/%d %H:%M:%S', structObjectBasedOnTimestamp))
print('Specified time by a tuple:', time.strftime('%Y/%m/%d %H:%M:%s', (2011, 11, 11, 11, 11, 11, 11, 11, 11)))
print('Local time:', time.strftime('%Y/%m/%d %H:%M:%S'))

print('\nCreating datetime object by a string with strptime method:',
      dt.datetime.strptime('2011/11/11 11:11:11', '%Y/%m/%d %H:%M:%S'))
print('Creating a struct object by a string with strptime method:',
      time.strptime('2011/11/11 11:11:11', '%Y/%m/%d %H:%M:%S'))

"""
TimeDelta objects/operations
"""
dt1 = dt.datetime(2024, 3, 16, 23, 56, 00)
dt2 = dt.datetime(1993, 12, 11, 21, 55, 00)

timeDeltaOne_dateTime = dt1 - dt2
print('\ntimeDelta operation with datetime objects:', timeDeltaOne_dateTime, type(timeDeltaOne_dateTime))

d1 = dt.date(2024, 3, 16)
d2 = dt.date(1993, 12, 11)

timeDeltaOne_Date = d1 - d2
print('timeDelta operation with time objects:', timeDeltaOne_Date, type(timeDeltaOne_Date))

delta = dt.timedelta(weeks=2, days=2, hours=2)
print()
print('delta:', delta)

delta2 = delta * 2
print('delta2:', delta2)

d = dt.date(2019, 10, 4) + delta2
print('d:', d)

deltaOp = dt.datetime(2019, 10, 4, 14, 53) + delta2
print('dt:', deltaOp)


t = dt.time(14, 53)
print(t.strftime("%H:%M:%S"))

delt1 = dt.datetime(2020, 9, 29, 14, 41, 0)
delt2 = dt.datetime(2020, 9, 28, 14, 41, 0)

print(delt1 - delt2)
