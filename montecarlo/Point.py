import math
import random

class Point :
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y

    def distanceFrom(self, B):
        return math.sqrt((self.X - B.X)**2 + (self.Y - B.Y)**2)

    def distanceFromOrigin(self):
        O = Point(0, 0)
        return self.distanceFrom(O)

    def display(self):
        print(f"({self.X} , {self.Y})")

    def isInRedSurface(self) :
        return self.distanceFrom(Point(2, 2)) > 2

    @staticmethod
    def randomPoint():
        x = 2 * random.random()
        y = 2 * random.random()
        return Point(x, y)