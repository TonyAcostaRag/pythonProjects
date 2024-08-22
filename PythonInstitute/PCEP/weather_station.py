
temps = [ [ 0.0 for h in range(24) ] for d in range(31)]

temps_test_values = [i for i in range (744)]
test_value_index = 0

for day in temps:
    for h in range(24):
        day[h] = temps_test_values[test_value_index] + 0.0
        test_value_index += 1

total_noon_temps = 0
highest_temp = -100
for day in temps:
    print("day: ", day)
    total_noon_temps += day[12]
    for hour in day:
        print("hour: ", hour, end=" ")
        if hour > highest_temp:
            highest_temp = hour
    print()
    
average = total_noon_temps / 31
total_20_C_Counter = 0

for day in temps:
    if day[12] >= 20.0:
        total_20_C_Counter += 1

print("\nAverage temperature at noon:", round(average, 2))
print("Highest temperature:", highest_temp)
print("Total :", highest_temp)  
print("Total noon with temp greater or equal to 20.0:", total_20_C_Counter)
