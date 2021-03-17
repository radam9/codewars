# https://www.codewars.com/kata/57eb8fcdf670e99d9b000272
# 6 Kyu
# Highest Scoring Word

# My Solution
def high(text):
    words = text.split()
    score = lambda word: sum(ord(letter) - 96 for letter in word)
    scores = [score(word) for word in words]
    first_index = scores.index(max(scores))
    return words[first_index]


# Codewars Inspired Solution
def high(text):
    words = text.split()
    score = lambda word: sum(ord(letter) - 96 for letter in word)
    return max(words, key=score)
