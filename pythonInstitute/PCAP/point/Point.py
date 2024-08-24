import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return math.hypot((x-self.getx()), y-self.gety())

    def distance_from_point(self, point):
        return math.hypot((point.getx()-self.getx()), point.gety()-self.gety())
