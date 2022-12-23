# https://www.codewars.com/kata/585d7d5adb20cf33cb000235
# 6 kyu
# Find the unique number

# my original solution
def find_uniq(arr):
    for i in set(arr):
        if arr.count(i) == 1:
            return i


# codewars solution
def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b
