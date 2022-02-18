# https://www.codewars.com/kata/5508249a98b3234f420000fb/train/python
# 5 Kyu
# First Variation on Ceasar Cipher

# My Solution
from itertools import zip_longest


def moving_shift(string, shift):
    result = looper(string, shift)
    part_len = -(-len(string) // 5)
    result = ["".join(x) for x in zip_longest(*[iter(result)] * part_len, fillvalue="")]
    if len(result) != 5:
        return [*result, ""]
    return result


def demoving_shift(array, shift):
    return looper(array, shift)


def get_substitute(char, shift, alphabet):
    char_position = alphabet.find(char.lower())
    new_char = alphabet[(char_position + shift) % 26]
    if char.isupper():
        return new_char.upper()
    return new_char


def looper(_input, shift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = []
    for char in "".join(_input):
        if char.lower() in alphabet:
            result.append(get_substitute(char, shift, alphabet))
        else:
            result.append(char)
        shift += 1
    return "".join(result)


# Codewars Solution
from string import ascii_lowercase as abc, ascii_uppercase as ABC
from math import ceil


def _code(string, shift, mode):
    return "".join(
        abc[(abc.index(c) + i * mode + shift) % len(abc)]
        if c in abc
        else ABC[(ABC.index(c) + i * mode + shift) % len(ABC)]
        if c in ABC
        else c
        for i, c in enumerate(string)
    )


def moving_shift(string, shift):
    encoded = _code(string, shift, 1)
    cut = int(ceil(len(encoded) / 5.0))
    return [encoded[i : i + cut] for i in range(0, 5 * cut, cut)]


def demoving_shift(arr, shift):
    return _code("".join(arr), -shift, -1)