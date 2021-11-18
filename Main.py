import torch
from Backtester import BackTester
from Reader import reader
from matplotlib import pyplot as plt
from Algorithms import *
import numpy as np

leser = reader("ETH-BTC.csv")
slices15 = leser.getSlices(10)
slices30 = leser.getSlices(25)
sma15 = sma(slices15)
cross = smaCross(slices15, slices30)
#plt.plot(range(len(leser.Open)), leser.Open)
tester = BackTester(cross, 1, leser.Open, 0.1)
tester.test()
plt.plot(cross[0], cross[1])
plt.plot(cross[0], np.zeros(737))
plt.show()
"""
print('Target probabilities', torch.randn(3, 5).softmax(dim=1))
print('Target indices', torch.empty(3, dtype=torch.long).random_(5))

"""
