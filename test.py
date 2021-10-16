import numpy as np
import matplotlib.pyplot as plt

arrivalRate = 9
departureRate = 12

nbHours = 5
precision = 3600
nbSeconds = precision * nbHours

nbArrivals = np.random.poisson(arrivalRate, nbSeconds)
nbDepartures = np.random.poisson(departureRate, nbSeconds)


print(nbArrivals.mean())
print(nbDepartures.mean())