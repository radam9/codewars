# https://www.codewars.com/kata/552c028c030765286c00007d/solutions/python
# 6 kyu
# IQ Test


def iq_test(numbers):
    b = [int(e) for e in numbers.split(" ")]
    c = [i % 2 for i in b]
    if c.count(0) == 1:
        return c.index(0) + 1
    return c.index(1) + 1

