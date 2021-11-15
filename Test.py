import torch
import torch.nn as nn
import torch.optim as optim
from Reader import reader


class Test(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.lstm = nn.LSTM(input_size=4, hidden_size=32, batch_first=True)
        self.linear = nn.Linear(32, 2)

    def forward(self, x):
        out, (c0, h0) = self.lstm(x)
        x = self.linear(h0)

        return x.squeeze(0)


# Model
model = Test()

# Gradient descent optimizer
optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)

# CrossEntropy Loss funksjon
criterion = nn.CrossEntropyLoss()

leser = reader("ETH-BTC.csv")

batch_size = 5
batches = []
labels = []
data_and_labels = leser.getBatches(batch_size, 15)

def train(data):
    # RANDOM DATA
    data_shape = (batch_size, 15, 4)

    out = model(torch.FloatTensor(data[0]))
    print(out.softmax(dim=1))

    # Kalkuler loss -> label = opp, output = ned -> 1 loss, enkelt forklart..
    loss = criterion(out, torch.LongTensor(data[1]))

    # Kalkuler gradients for hver parameter
    loss.backward()

    # Oppdater parametere
    optimizer.step()
    print(loss)


for batch in data_and_labels:
    train(batch)
