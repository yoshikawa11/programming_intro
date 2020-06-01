import random

def rollDie():
    return random.choice([1, 2, 3, 4, 5, 6])

def checkPascal(numTrials):
    """ numTrialsは1以上の整数(int)と仮定する
        勝利する確率の評価値を表示する"""
    numWins = 0
    for i in range(numTrials):
        for j in range(24):
            d1 = rollDie()
            d2 = rollDie()
            if d1 == 6 and d2 == 6:
                numWins += 1
                break
    print('Probability of winning = ', numWins/numTrials)


checkPascal(10000)
print('1-(35.0/36.0)**24 ', 1-(35.0/36.0)**24)
