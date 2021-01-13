# https://www.codewars.com/kata/55f4e56315a375c1ed000159/train/python
# 5 Kyu
# Numbers that are a power of their sum of digits

# My Solution (couldn't solve)
from math import log


def power_sumDigTerm(n):
    matches = 0
    match = 0
    number = 4912
    while matches != n:
        sum_n = sum_of_digits(number)
        if sum_n != 1:
            power = round(log(number) / log(sum_n))
            if int(sum_n ** power) == number:
                matches += 1
                match = number
        number += 1
        print(number)
    return match


def sum_of_digits(number):
    sum_n = 0
    n = number
    while n:
        sum_n, n = sum_n + n % 10, n // 10
    return sum_n


# Codewars Solution
def power_sumDigTerm(n):
    return sorted(
        set(
            [
                a ** b
                for a in range(2, 100)
                for b in range(2, 100)
                if a == sum(map(int, str(a ** b)))
            ]
        )
    )[n - 1]
