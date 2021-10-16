import math
from Point import Point

class Vector :
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y

    def __init__(self, startPoint, endPoint):
        self.X = endPoint.X - startPoint.X
        self.Y = endPoint.Y - startPoint.Y

    def norm(self):
        return math.sqrt((self.X)**2 + (self.Y)**2)

    def dotProduct(self, B):
        return self.X*B.X + self.Y*B.Y