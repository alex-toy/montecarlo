import numpy as np
import random
import matplotlib.pyplot as plt

numberWeeks = 20
print(f"Nombre de semaines de simulation : {numberWeeks}.")
NumberDays = numberWeeks * 5
StockDelivery = 100
stockQty = StockDelivery
nextDelivery = 0
ConsumptionRate = 20
dayNum = 0

stockQties = []

CE = 2
CP = 100
CET = 0
CPT = 0

for dayNum in range(1, NumberDays+1) : 

    if dayNum % 5 == 0 :
        DeliveryDelay = random.choice([1, 2, 3])
        nextDelivery = dayNum + DeliveryDelay

    if dayNum == nextDelivery :
        stockQty += StockDelivery

    stockQty -= ConsumptionRate

    if stockQty > 0 : CET += CE*stockQty 
    if stockQty < 0 : CPT += -CP*stockQty 
    stockQties.append(stockQty)

meanCET = CET/numberWeeks
print(f"Moyenne des coûts d'entretien sur une semaine : {meanCET} euros")

meanCPT = CPT/numberWeeks
print(f"Moyenne des coûts de pénurie sur une semaine : {meanCPT} euros")
print(f"Moyenne des coûts de stockage sur une semaine : {meanCET+meanCPT} euros")

plt.bar(list(range(1, NumberDays+1)), stockQties)
plt.show()

