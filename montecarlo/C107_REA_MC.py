import numpy as np
import random
import matplotlib.pyplot as plt
from Point import Point
from Vector import Vector

countPointInRed = 0
numPoints = 10000
surface = 4

for i in range(0, numPoints) :
    point = Point.randomPoint()
    if point.isInRedSurface() : countPointInRed += 1

print(f"La surface de la partie rouge est de : {countPointInRed/numPoints*surface}.")