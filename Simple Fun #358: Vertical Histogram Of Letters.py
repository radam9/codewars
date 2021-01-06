#
# 5 Kyu
# Simple Fun #358: Vertical Histogram Of Letters

# My Solution
from string import ascii_uppercase as abc


def vertical_histogram_of(string):
    counter = {}
    for letter in string:
        if letter not in abc or letter in counter:
            continue
        counter[letter] = string.count(letter)
    keys = sorted(list(key for key in counter))
    max_count = counter[max(counter, key=counter.get)] if counter else 0
    output = ""
    values = [counter[key] for key in keys]
    for i in range(max_count):
        line = " ".join(["*" if value > 0 else " " for value in values])
        output = f"{line.rstrip(' ')}\n" + output
        values = [value - 1 for value in values]
    return f"{output}{' '.join(keys)}"


# Codewars Solution
from collections import Counter


def verticalHistogramOf(s):
    def buildLine(h):
        return " ".join(h and " *"[cnts[k] >= h] or k for k in keys).rstrip()

    cnts = Counter(filter(str.isupper, s))
    keys = sorted(cnts)
    m = max(cnts.values(), default=0)
    return "\n".join(map(buildLine, reversed(range(m + 1))))
