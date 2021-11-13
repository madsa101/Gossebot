import numpy as np
import torch


class reader:
    def __init__(self, file):
        self.file = open(file)
        self.lines = []
        self.Dates = []
        self.Open = []
        self.High = []
        self.Low = []
        self.Close = []
        self.AdjClose = []
        self.Volume = []
        index = 0

        for line in self.file:
            if index >= 1:
                try:
                    self.lines.append(line), self.Open.append(float(self.lines[index - 1].split(",")[1]))
                    self.High.append(float(self.lines[index - 1].split(",")[2])), self.Low.append(
                        float(self.lines[index - 1].split(",")[3]))
                    self.Close.append(float(self.lines[index - 1].split(",")[4])), self.Dates.append(
                        self.lines[index - 1].split(",")[0])
                    self.AdjClose.append(self.lines[index - 1].split(",")[5]), self.Volume.append(
                        self.lines[index - 1].split(",")[6])
                except ValueError:
                    del self.lines[index - 1]
                    continue
            index += 1

        self.inputs = np.ndarray([4, len(self.lines)])
        self.file.close()
        self.tensor = torch.FloatTensor()

    def printAll(self):
        iterator = iter(self.lines)
        done_looping = False
        while not done_looping:
            try:
                item = next(iterator)
            except StopIteration:
                done_looping = True
            else:
                print(item)

    def _reverseLists(self):
        self.Open.reverse()
        self.High.reverse()
        self.Low.reverse()
        self.Close.reverse()

    def getDates(self):
        pass

    def getBatches(self, batch_size, timeframe):
        slices = []
        labels = []
        x = 0
        self._reverseLists()

        while x < batch_size:
            slices.append([])
            s = 0
            for i in range(x + 1, timeframe + x + 1):
                slices[x].append([])
                slices[x][s].append(self.Open[i])
                slices[x][s].append(self.High[i])
                slices[x][s].append(self.Low[i])
                slices[x][s].append(self.Close[i])
                s += 1
            labels.append(1) if (self.Close[x] - self.Close[x + 1] >= 0) else labels.append(0)
            x += 1

        self._reverseLists()

        return slices, labels

