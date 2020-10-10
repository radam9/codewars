# https://www.codewars.com/kata/525c7c5ab6aecef16e0001a5
# 4 kyu
# parseInt() reloaded

# My Solution
def parse_int(string):
    numbers = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
        "eleven": 11,
        "twelve": 12,
        "thirteen": 13,
        "fourteen": 14,
        "fifteen": 15,
        "sixteen": 16,
        "seventeen": 17,
        "eighteen": 18,
        "nineteen": 19,
        "twenty": 20,
        "thirty": 30,
        "forty": 40,
        "fifty": 50,
        "sixty": 60,
        "seventy": 70,
        "eighty": 80,
        "ninety": 90,
    }

    multipliers = {"hundred": 100, "thousand": 1000, "million": 1000000}

    number = string.replace("-", " ").replace(" and", "")
    multiplier = 1
    result = 0

    for word in number.split(" ")[::-1]:
        if word == "hundred":
            multiplier *= multipliers[word]
            continue
        elif word in multipliers:
            multiplier = multipliers[word]
            continue
        result += numbers[word] * multiplier
    return result


# Codewars Solution
words = {
    w: n
    for n, w in enumerate(
        "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
    )
}
words.update(
    {
        w: 10 * n
        for n, w in enumerate(
            "twenty thirty forty fifty sixty seventy eighty ninety hundred".split(), 2
        )
    }
)
thousands = {
    w: 1000 ** n
    for n, w in enumerate(
        "thousand million billion trillion quadrillion quintillion sextillion septillion octillion nonillion decillion".split(),
        1,
    )
}


def parse_int(strng):
    num = group = 0
    for w in strng.replace(" and ", " ").replace("-", " ").split():
        if w == "hundred":
            group *= words[w]
        elif w in words:
            group += words[w]
        else:
            num += group * thousands[w]
            group = 0
    return num + group
