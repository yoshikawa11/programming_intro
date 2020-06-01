import random


def variance(X):
    """Xは数を要素とするリストと仮定する
        この関数は，Xの分散を返す．"""
    mean = sum(X) / len(X)
    tot = 0.0
    for x in X:
        tot += (x - mean) ** 2
    return tot / len(X)


def stdDev(X):
    """Assumes that X is a list of numbers.
       Returns the standard deviation of X"""
    """Xは数を要素とするリストと仮定する．
        この関数は，Xの標準偏差を返す．"""
    return variance(X) ** 0.5


def throwNeedles(numNeedles):
    inCircle = 0
    for Needles in range(1, numNeedles + 1):
        x = random.random()
        y = random.random()
        if (x*x + y*y)**0.5 <= 1:
            inCircle += 1
    #円の4分の1の領域にある針のみを数えているので，4倍する．
    return 4*(inCircle/numNeedles)


def getEst(numNeedles, numTrials):
    estimates = []
    for t in range(numTrials):
        piGuess = throwNeedles(numNeedles)
        estimates.append(piGuess)
    sDev = stdDev(estimates)
    curEst = sum(estimates)/len(estimates)
    print('Est. =', str(round(curEst, 5)) + ',',
          'Std. dev. =', str(round(sDev, 5)) + ',',
          'Needles =', numNeedles)
    return (curEst, sDev)


def estPi(precision, numTrials):
    numNeedles = 1000
    sDev = precision
    while sDev > precision/1.96:
        curEst, sDev = getEst(numNeedles, numTrials)
        numNeedles *= 2
    return curEst


estPi(0.01, 100)
