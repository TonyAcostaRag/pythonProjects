hour = 23
min = 58
duration_in_min = 642

duration_in_hours = duration_in_min // 60
duration_in_mins_modulo = duration_in_min % 60
end_time_hour_temp = ( hour + duration_in_hours ) % 24

end_time_hour = end_time_hour_temp + ( duration_in_mins_modulo + min ) // 60
end_time_min = ( duration_in_mins_modulo + min ) % 60

print("hour: ", hour)
print("min: ", min)
print("duration_in_min: ", duration_in_min)

print("duration_in_hours: ", duration_in_hours)
print("duration in mins_modulo: ", duration_in_mins_modulo)
print("end_time_hour_temp", end_time_hour_temp)

print(f"{end_time_hour}:{end_time_min}")













