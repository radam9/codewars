# https://www.codewars.com/kata/56c30ad8585d9ab99b000c54
# 5 Kyu
# Play with two Strings

# My Solution
def work_on_strings(first, second):
    for letter in first:
        second = casing(letter, second)
    for letter in second:
        first = casing(letter, first)
    return "".join(first + second)


def casing(letter, string):
    dic = string.maketrans(
        {letter.lower(): letter.upper(), letter.upper(): letter.lower()}
    )
    return string.translate(dic)


# Codewars Solution
def work_on_strings(a, b):
    new_a = [
        letter if b.lower().count(letter.lower()) % 2 == 0 else letter.swapcase()
        for letter in a
    ]
    new_b = [
        letter if a.lower().count(letter.lower()) % 2 == 0 else letter.swapcase()
        for letter in b
    ]
    return "".join(new_a + new_b)
