from Algorithms import *


class BackTester:

    def __init__(self, signals, startingFunds, prices, deadzone):
        self.signals = signals  # liste med "signaler" -1 til 1
        self.ethWallet = startingFunds
        self.btcWallet = 0
        self.prices = prices
        self.deadzone = deadzone

    def test(self):
        index = self.signals[0][0]
        for signal in self.signals[2]:
            if signal > self.deadzone:  # BUY ETH
                self.ethWallet += signal * self.btcWallet / self.prices[index]
                self.btcWallet -= signal * self.btcWallet
            elif signal < (-1*self.deadzone):  # SELL ETH
                self.btcWallet += -signal * self.ethWallet * self.prices[index]
                self.ethWallet -= -signal * self.ethWallet
            else:
                pass
            print(self.ethWallet + (self.btcWallet / self.prices[index]))
            index += 1


