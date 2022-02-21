import random

def rollDie():
    """returns a random int between 1 and 6"""
    return random.choice([1,2,3,4,5,6])

def runSim(goal, numTrials, txt):
    success = 0
    for t in range(numTrials):
        result = ''
        for i in range(len(goal)):
            result += str(rollDie())
        if result == txt:
            success += 1

    print('Actual probability of', txt, '=',
          round(1/(6**len(goal)), 8)) 
    estProbability = round(success/numTrials, 8)
    print('Estimated Probability of', txt, '=',
          round(estProbability, 8))


# runSim('11111', 1000000, '11111')

def sameDate(numPeople, numSame):
    possibleDates = range(366)
#    possibleDates = 4*list(range(0, 57)) + [58]\
#                    + 4*list(range(59, 366))\
#                    + 4*list(range(180, 270))
    birthdays = [0]*366
    for p in range(numPeople):
        birthDate = random.choice(possibleDates)
        birthdays[birthDate] += 1
    return max(birthdays) >= numSame

def birthdayProb(numPeople, numSame, numTrials):
    numHits = 0
    for t in range(numTrials):
        if sameDate(numPeople, numSame):
            numHits += 1
    return numHits/numTrials

print(birthdayProb(300, 2, 100000))