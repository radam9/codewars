# https://www.codewars.com/kata/5270d0d18625160ada0000e4/train/python
# 5 Kyu
# Greed is Good

# my solution
def score(dice):
    total = 0
    triples = {1: 1000, 2: 200, 3: 300, 4: 400, 5: 500, 6: 600}
    ones = {1: 100, 2: 0, 3: 0, 4: 0, 5: 50, 6: 0}
    counter = dict()
    for value in dice:
        if counter.get(value):
            counter[value] += 1
        else:
            counter[value] = 1

    for key, val in counter.items():
        if val == 0:
            continue
        elif val < 3 and ones.get(key):
            total += (val * ones[key])
        elif val >= 3:
            total += triples[key]
            total += ((val - 3) * ones.get(key))
    
    return total

# second solution influenced by codewars solutions
from collections import Counter

def score(dice):
    total = 0
    triples = {1: 1000, 2: 200, 3: 300, 4: 400, 5: 500, 6: 600}
    ones = {1: 100, 2: 0, 3: 0, 4: 0, 5: 50, 6: 0}
    dice = Counter(dice)
    for value in dice:
        total += (dice[value] // 3) * triples[value]
        total += (dice[value] % 3) * ones[value]
    return total