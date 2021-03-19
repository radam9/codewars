# https://www.codewars.com/kata/55c04b4cc56a697bb0000048
# 5 Kyu
# Scramblies


# My Solution
from collections import Counter


def scramble(s1, s2):
    soup = Counter(s1)
    word = Counter(s2)
    for key, count in word.items():
        if count > soup[key]:
            return False
    return True


# Codewars Solution
def scramble(s1, s2):
    for c in set(s2):
        if s1.count(c) < s2.count(c):
            return False
    return True


# Codewars Solution 2
from collections import Counter


def scramble(s1, s2):
    return len(Counter(s2) - Counter(s1)) == 0
