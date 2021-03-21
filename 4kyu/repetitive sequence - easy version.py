# https://www.codewars.com/kata/5f134651bc9687000f8022c4
# 4 Kyu
# Repetitive Sequence - Easy Version

# My Solution
from itertools import chain, repeat


def find(n):
    if n <= 3:
        return [0, 1, 2, 2][n]
    arr = [[2]]
    arr_sum = 5
    arr_len = 4
    for i, arr_i in enumerate(chain.from_iterable(arr), 3):
        arr_sum += i * arr_i
        if arr_sum >= n:
            x = (arr_sum - n) // i
            return arr_len + arr_i - (x + 1)
        arr_len += arr_i
        if arr_len < 70_000:
            arr.append(repeat(i, arr_i))


# Iterative solution - too slow
def find(n):
    sequence = [0, 1, 2, 2]
    index = 3
    while n > len(sequence) - 1:
        sequence.extend((index for _ in range(sequence[index])))
        index += 1
    return sequence[n]


# Fastest Codewars Solution
cache = [0, 2, 4]
pc = [0, 2, 6]

repeat = len(cache) - 1
b = cache[-1]
while pc[-1] < 2 ** 41:
    if len(cache) >= b:
        repeat += 1
        b = cache[repeat]
    cache.append(cache[-1] + repeat)
    pc.append(pc[-1] + (cache[-1] - cache[-2]) * (len(cache) - 1))

from bisect import bisect


def find(n):
    repeat = bisect(pc, n)
    return cache[repeat - 1] + (n - pc[repeat - 1]) // repeat
