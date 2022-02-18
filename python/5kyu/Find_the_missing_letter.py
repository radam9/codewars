# https://www.codewars.com/kata/5839edaa6754d6fec10000a2/train/python
# 5 Kyu
# Find the missing letter

# My Solution
from string import ascii_lowercase as abc, ascii_uppercase as ABC


def find_missing_letter(chars):
    if chars[0].islower():
        alpha = abc
    else:
        alpha = ABC
    first = alpha.index(chars[0])
    last = alpha.index(chars[-1]) + 1
    original = "".join(alpha[first:last])
    missing = [c for c in original if c not in "".join(chars)]
    return missing[0]


# Codewars Solution
def find_missing_letter(chars):
    n = 0
    while ord(chars[n]) == ord(chars[n + 1]) - 1:
        n += 1
    return chr(1 + ord(chars[n]))
