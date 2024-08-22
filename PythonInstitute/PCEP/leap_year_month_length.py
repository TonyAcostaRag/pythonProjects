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
    

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, " \t->", end=" ")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
		
