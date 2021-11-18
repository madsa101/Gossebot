def sma(slices):
    # regne ut Simple Moving Average, sum av verdier delt på antall verdier i perioden
    smaData = []
    perioder = []
    slice_size = len(slices[0])
    for f in range(len(slices)):
        summ = 0
        for _data in slices[f]:
            summ += _data[0]
        smaData.append(summ / float(len(slices[f])))
        perioder.append(f + slice_size + 1)
    return [perioder, smaData]


def smaCross(short_slices, long_slices):
    smaCross = []
    tradeSignaler = [0]
    smaShort = sma(short_slices)
    smaLong = sma(long_slices)
    perioder = []
    longShortDiff = len(short_slices) - len(long_slices)

    for x in range(len(long_slices)):
        smaCross.append(smaShort[1][x + longShortDiff] - smaLong[1][x])
        perioder.append(smaLong[0][x])
        if x > 0:
            if (smaCross[x] >= 0 and smaCross[x - 1] >= 0) or (smaCross[x] < 0 and smaCross[x - 1] < 0):
                tradeSignaler.append(0)
            elif smaCross[x] >= 0 and smaCross[x - 1] < 0:
                tradeSignaler.append(1)
            else:
                tradeSignaler.append(-1)

    return perioder, smaCross, tradeSignaler
