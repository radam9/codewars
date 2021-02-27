# https://www.codewars.com/kata/55aa075506463dac6600010d/train/python
# 5 Kyu
# Integers: Recreation One

# My Solution
def list_squared(m, n):
    result = []
    for num in range(m, n + 1):
        divisor_sum = divisors_check(num)
        if divisor_sum:
            result.append([num, divisor_sum])
    return result


def divisors_check(num):
    divisors = []
    for n in range(1, int(num ** 0.5) + 1):
        if (num / n) % 1 == 0:
            divisors.append(n)
            if num / n != n:
                divisors.append(num / n)
    sums = sum([d ** 2 for d in divisors])
    if (sums ** 0.5) % 1 == 0:
        return sums
    return 0


# Codewars Inspired Solution
def list_squared(m, n):
    result = []
    for num in range(m, n + 1):
        divisor_sum = divisors_check(num)
        if divisor_sum:
            result.append([num, divisor_sum])
    return result


def divisors_check(num):
    divisors = set()
    for n in range(1, int(num ** 0.5) + 1):
        if (num / n) % 1 == 0:
            divisors.update([n, num / n])
    sums = sum(d ** 2 for d in divisors)
    if int(sums ** 0.5) ** 2 == sums:
        return sums
    return 0


# 2nd Codewars Inspired Solution
def list_squared(m, n):
    result = []
    for num in range(m, n + 1):
        divisors = set()
        for n in range(1, int(num ** 0.5) + 1):
            if (num / n) % 1 == 0:
                divisors.update([n, num / n])
        sums = sum(d ** 2 for d in divisors)
        if int(sums ** 0.5) ** 2 == sums:
            result.append([num, sums])
    return result