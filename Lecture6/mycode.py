from operator import le
import pylab
import random


def flip(numFlips):
    head = 0
    for i in range(numFlips):
        coin = random.choice(["H", "T"])
        if coin == "H":
            head += 1
    return head / numFlips


def flipSim(numFlip, numTrials):
    headFrac = []
    for t in range(numTrials):
        headFrac.append(flip(numFlip))
    mean = sum(headFrac) / len(headFrac)
    return mean

# print(flipSim(10, 100000))
# print(flipSim(10, 100000))


def regressToMean(numFlip, numTrial):
    fracHeads = []
    for t in range(numTrial):
        fracHeads.append(flip(numFlip))

    extremes, nextTrials = [], []
    for i in range(len(fracHeads) - 1):
        if fracHeads[i] < 0.33 or fracHeads[i] > 0.66:
            extremes.append(fracHeads[i])
            nextTrials.append(fracHeads[i+1])

    # Plot results
    pylab.plot(range(len(extremes)), extremes, 'ko', label='Extreme')
    pylab.plot(range(len(nextTrials)), nextTrials, 'k^', label='Next Trial')
    pylab.axhline(0.5)
    pylab.ylim(0, 1)
    pylab.xlim(-1, len(extremes) + 1)
    pylab.xlabel('Extreme Example and Next Trial')
    pylab.ylabel('Fraction Heads')
    pylab.title('Regression to the Mean')
    pylab.legend(loc='best')


regressToMean(40, 15)


def variance(X):
    """Assumes that X is a list of numbers.
        Returns the standard deviation of X"""
    mean = sum(X)/len(X)
    tot = 0
    for x in X:
        tot += (x-mean)**2
    return tot / len(X)


def stdDev(X):
    """Assumes that X is a list of numbers.
        Returns the standard deviation of X"""
    return variance(X)**0.5
