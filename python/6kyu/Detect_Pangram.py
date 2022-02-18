# https://www.codewars.com/kata/545cedaa9943f7fe7b000048
# 6 Kyu
# Detect Pangram

# My Solution
from string import ascii_lowercase as abc


def is_pangram(string):
    string = set(string.lower())
    return set(abc).issubset(string)
