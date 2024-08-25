class WeekDayError(Exception):
    pass


class Weeker:

    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    def __init__(self, day):
        if day not in Weeker.days:
            raise WeekDayError

        self.__day = day

    def __str__(self):
        return str(self.__day)

    def add_days(self, n):

        current_index = Weeker.days.index(self.__day)
        calculated_index = current_index + n

        while calculated_index >= len(Weeker.days):
            calculated_index -= 7

        self.__day = Weeker.days[calculated_index]

    def subtract_days(self, n):

        current_index = Weeker.days.index(self.__day)
        calculated_index = current_index - n

        while calculated_index < 0:
            calculated_index += 7

        self.__day = Weeker.days[calculated_index]
