# https://www.codewars.com/kata/5467e4d82edf8bbf40000155/train/python
# 7 Kyu
# Descending Order

# My Solution
def descending_order(num):
    nums = [n for n in str(num)]
    nums.sort()
    nums.reverse()
    return int("".join(nums))


# Codewars Solution
def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))