import numpy as np
import matplotlib.pyplot as plt

arrivalRate = 9
departureRate = 12

nbHours = 1
precision = 3600

nbSeconds = precision * nbHours
arrivalRate = arrivalRate / precision
departureRate = departureRate / precision

nbArrivals = np.random.poisson(arrivalRate, nbSeconds)
nbDepartures = np.random.poisson(departureRate, nbSeconds)
nbClientsWaiting = np.empty([nbSeconds])

for i in range(1, nbSeconds) :
    if nbDepartures[i] < nbClientsWaiting[i-1] + nbArrivals[i] :
        nbClientsWaiting[i] = nbClientsWaiting[i-1] + nbArrivals[i] - nbDepartures[i]
    else :
        nbClientsWaiting[i] = 0

    if nbClientsWaiting[i] != nbClientsWaiting[i-1] :
        print(nbClientsWaiting[i])
        #pass


print(nbClientsWaiting.mean())
