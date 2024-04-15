from timer.Timer import Timer
from datetime import time


def format_time(timer_obj):

    timer_string = str(timer_obj.__str__())

    timer_formatted = ""
    temp = ""
    for i in range(len(timer_string)):
        if timer_string[i] != ":":
            temp += str(timer_string[i])
        if timer_string[i] == ":" or i == len(timer_string)-1:
            if int(temp) < 10:
                temp = "0" + temp
            timer_formatted += temp+":"
            temp = ""

    timer_formatted = timer_formatted[0:-1]
    time_format = time(int(timer_formatted[0:2]),
                       int(timer_formatted[3:5]),
                       int(timer_formatted[6:8]))
    return time_format


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(format_time(timer))
timer.prev_second()
print(format_time(timer))
