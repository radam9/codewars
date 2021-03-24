# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1
# 6 Kyu
# Counting Duplicates

# My Solution 1
from collections import Counter


def duplicate_count(text):
    duplicates = Counter(text.lower())
    count = 0
    for value in duplicates.values():
        if value > 1:
            count += 1
    return count


# My Solution 2
def duplicate_count(text):
    text = text.lower()
    unique = set(text)
    duplicates = [text.count(letter) for letter in unique]
    count = 0
    for value in duplicates:
        if value > 1:
            count += 1
    return count


# Codewars Solution
def duplicate_count(s):
    return len([c for c in set(s.lower()) if s.lower().count(c) > 1])
