import time


class Vehicle:
    def change_direction(self, on):
        pass

    def turn(self):
        self.change_direction(self, True)
        time.sleep(2.5)
        self.change_direction(self, False)

