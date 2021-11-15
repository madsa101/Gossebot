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
        batches = [[[], []]]
        batch = []
        labels = []
        slices = []
        self._reverseLists()
        x = 0

        while x < len(self.lines):
            if x % batch_size == 0 and x != 0:
                batches.append([[], []])

            batches[-1][0].append([])
            for s in range(1, timeframe + 1):
                i = x + s
                if i < len(self.lines):
                    batches[-1][0][-1].append([])
                    batches[-1][0][-1][-1].append(self.Open[i])
                    batches[-1][0][-1][-1].append(self.High[i])
                    batches[-1][0][-1][-1].append(self.Low[i])
                    batches[-1][0][-1][-1].append(self.Close[i])
                else:
                    del batches[-1]
                    self._reverseLists()
                    return batches

            batches[-1][1].append(1) if (self.Close[x] - self.Close[x + 1] >= 0) else batches[-1][1].append(0)
            x += 1

