# https://www.codewars.com/kata/5b853229cfde412a470000d0
# 8 Kyu
# Twice as old


# My Solution
def twice_as_old(dad, son):
    diff = (dad / 2) - son
    time = 0
    if diff > 0:
        mod = 1
    else:
        mod = -1

    while diff != 0:
        dad += mod
        son += mod
        diff = (dad / 2) - son
        time += 1
    return time


# Codewars Solution
def twice_as_old(dad_years_old, son_years_old):
    return abs(dad_years_old - 2 * son_years_old)


# Codewars Solution 2
def twice_as_old(dad_years_old, son_years_old):
    twice_old = son_years_old * 2
    years_ago = dad_years_old - twice_old
    return abs(years_ago)
