# https://www.codewars.com/kata/55e0467217adf9c3690000f9
# 5 Kyu
# My Very Own Python's Split Function


# My Solution
import re


def my_very_own_split(string, delimiter=None):
    if delimiter == "":
        raise ValueError("no delimiter provided")
    if len(string) == 0:
        yield ""
    if not delimiter:
        delimiter = delimiter or " "
        string = re.sub(r"\t+", " ", string)

    d = len(delimiter)
    while len(string):
        index = string.find(delimiter)
        if index == 0 and len(string) == d:
            string = ""
            yield ""
        if index == -1 and string:
            yield string
            break
        yield string[:index]
        string = string[index + d :]


# Codewars Solution
import re


def my_very_own_split(string, delimiter=None):
    if delimiter == "":
        raise ValueError("empty delimiter")
    if delimiter == None:
        delimiter = "\s+"
    else:
        delimiter = re.escape(delimiter)
    pos = 0
    for m in re.finditer(delimiter, string):
        yield string[pos : m.start()]
        pos = m.end()
    yield string[pos:]


# Codewars no re
def my_very_own_split(string, delimiter=None):

    if delimiter == "":
        raise ValueError

    if delimiter is None:
        string = string.replace("\t", " ")
        while "  " in string:
            string = string.replace("  ", " ")
        delimiter = " "

    last, l = 0, len(delimiter)
    for i in range(len(string)):
        if string[i : i + l] == delimiter:
            yield string[last:i]
            last = i + l
    yield string[last:]
