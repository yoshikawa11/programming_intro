import random

def calcBayes(priorA, probBifA, probB):
    """ priorA:事象Aの事前確率でBとは独立
        probBifA:Aが与えられた条件付きBの確率
        probB:事情Bの確率
        Bが与えられた条件下で事象Aを得る事後確率が結果として戻される"""
    return priorA * probBifA / probB


# priorA = 0.9
priorA = 1 / 3
prob6ifA = 1 / 5
prob6 = (1 / 5 + 1 / 6 + 1 / 7) / 3

numRolls = 200
postA = priorA
for i in range(numRolls + 1):
    if i % (numRolls // 10) == 0:
        print(i, ' 回振った時点でタイプAである確率 = ', round(postA, 4))
    isSix = random.random() <= 1 / 7 # サイコロはタイプCである
    if isSix:
        postA = calcBayes(postA, prob6ifA, prob6)
    else:
        postA = calcBayes(postA, 1 - prob6ifA, 1 - prob6)
