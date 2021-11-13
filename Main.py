import torch


print('Target probabilities', torch.randn(3, 5).softmax(dim=1))
print('Target indices', torch.empty(3, dtype=torch.long).random_(5))
