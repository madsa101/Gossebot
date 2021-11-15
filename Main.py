import torch
from Reader import reader

leser = reader("ETH-BTC.csv")
print(leser.getBatches(5, 2))
"""
print('Target probabilities', torch.randn(3, 5).softmax(dim=1))
print('Target indices', torch.empty(3, dtype=torch.long).random_(5))

"""
