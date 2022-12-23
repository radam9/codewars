# https://www.codewars.com/kata/546f922b54af40e1e90001da
# 6 Kyu
# Replace With Alphabet Position

# My Solution
from string import ascii_lowercase as abc


def alphabet_position(text):
    return " ".join(
        str(abc.index(letter) + 1) for letter in text.lower() if letter in abc
    )


# Codewars Solution
def alphabet_position(text):
    return " ".join(str(ord(c) - 96) for c in text.lower() if c.isalpha())
