# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec
# 6 kyu
# Presistent Bugger


def persistence(n):
    if len(str(n)) == 1:
        return 0
    c = 0
    while len(str(n)) > 1:
        a = 1
        for e in str(n):
            a *= int(e)
        n = a
        c += 1
    return c

