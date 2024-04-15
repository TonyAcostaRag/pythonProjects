import calendar as cal


class MyCalendar(cal.Calendar):

    def count_weekday_in_year(self, year, weekday):
        total_weekday_count = 0

        for mes in range(1, 13):

            for week in self.monthdays2calendar(year, mes):
                for day in week:
                    if day[0] != 0:
                        if day[1] == weekday:
                            total_weekday_count += 1
                            break

        return total_weekday_count


myCal1 = MyCalendar()

print('Total of fridays count:', myCal1.count_weekday_in_year(2024, cal.FRIDAY))
print('Total of fridays count:', myCal1.count_weekday_in_year(2019, 0))
print('Total of fridays count:', myCal1.count_weekday_in_year(2000, 6))

print(dir(cal))
