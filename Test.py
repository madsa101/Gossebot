import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from Reader import reader


class Test(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.lstm = nn.LSTM(input_size=4, hidden_size=32, batch_first=True)
        self.linear = nn.Linear(32, 2)

    def forward(self, x):
        out, (h0, c0) = self.lstm(x)
        x = self.linear(h0)

        return x.squeeze(0)


# Model
model = Test()

# Gradient descent optimizer
optimizer = optim.Adam(model.parameters(), lr=0.03)

# CrossEntropy Loss funksjon
criterion = nn.CrossEntropyLoss()

leser = reader("ETH-BTC.csv")

batch_size = 10
data_and_labels = leser.getBatches(batch_size, 5)

aBatch = data_and_labels[0]
lossPlot = []

def train(data):
    # RANDOM DATA
    data_shape = (batch_size, 15, 4)

    out = model(torch.Tensor(data[0]))
    print(out.softmax(dim=1))

    # Kalkuler loss -> label = opp, output = ned -> 1 loss, enkelt forklart..
    loss = criterion(out, torch.LongTensor(data[1]))

    # Kalkuler gradients for hver parameter
    loss.backward()

    # Oppdater parametere
    optimizer.step()
    print(loss.item())
    lossPlot.append(loss.item())


    print(out.argmax(dim=-1))


for r in range(50):
    train(aBatch)

for param in model.parameters():
    print(param.grad)

"""
for batch in data_and_labels:
    train(batch)
"""
plt.plot(lossPlot)
plt.show()

"""
for batch in data_and_labels:
    train(batch)
"""