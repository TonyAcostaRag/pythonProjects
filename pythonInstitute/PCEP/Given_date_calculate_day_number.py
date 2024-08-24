def is_year_leap(year):
    if year%4 == 0:
        if year % 100 == 0:
            return year % 400 == 0
        return True
    else:
        return False


def days_in_month(year, month):
    months_lengths   = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if month < 1 or month > 12:
        return
    
    if is_year_leap(year):
        months_lengths[1] += 1
    else:
        months_lengths[1] += 0
        
    month_length = months_lengths[month-1]
    
    return month_length


def day_of_year(year, month, day):
    
    if month < 1 or month > 12:
        return
    
    if day < 1 or day > 31:
        return
    
    if day > days_in_month(year, month):
        return
    
    total_days = 0
    for i in range(1, month):
        total_days += days_in_month(year, i)
        
    return total_days + day


test_results_expected = [366, 365, None, None, None, None, None, None]
test_data_year      = [2000, 2001, 2001, 2001, 2001, 2001, 2023, 2000]
test_data_month     = [12, 12, 0, 13, 12, 12, 9, 2]
test_data_day       = [31, 31, 31, 31, 32, 0, 31, 30]


for i in range(len(test_results_expected)):
    actual_result = day_of_year(test_data_year[i], test_data_month[i], test_data_day[i])
    print("Test data:", test_data_year[i], "/",
                            test_data_month[i], "/",
                            test_data_day[i],
            "\nActual result:", actual_result, "\nTest Status", end="")
    if test_results_expected[i] == actual_result:
        print(" -> " + "OK", end="\n\n")
    else:
        print(" -> " + "Failed, ", "value expected:", test_results_expected[i], end="\n\n")

