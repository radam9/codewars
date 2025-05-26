# https://www.codewars.com/kata/52597aa56021e91c93000cb0
# 5 Kyu
# Moving Zeros To The End


# My Solution
def move_zeros(array):
    zeroless_array = [a for a in array if a != 0]
    return zeroless_array + [0] * array.count(0)
