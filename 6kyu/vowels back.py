# https://www.codewars.com/kata/57cfd92c05c1864df2001563
# 6 Kyu
# Vowels Back


# My Solution
from string import ascii_lowercase as abc


def vowel_back(string):
    result = [None] * len(string)
    alphabet = {key: value for value, key in enumerate(abc, 1)}
    cases = {"a": -5, "i": -5, "u": -5, "c": -1, "o": -1, "d": -3, "e": -4}

    for index, letter in enumerate(string):
        case = cases.get(letter, 9)
        shift = ((case + alphabet[letter]) % 26) - 1
        new_letter = abc[shift]

        if new_letter in {"c", "d", "e", "o"}:
            new_letter = letter
        result[index] = new_letter

    return "".join(result)


# Codewars Solution
def vowel_back(string):
    return string.translate(
        str.maketrans("abcdefghijklmnopqrstuvwxyz", "vkbaafpqistuvwnyzabtpvfghi")
    )
