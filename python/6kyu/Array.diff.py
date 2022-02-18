# https://www.codewars.com/kata/523f5d21c841566fde000009/solutions/python
# 6 Kyu
# Array.diff

# My Solution
def array_diff(a, b):
    common = set(a).intersection(set(b))
    return [num for num in a if num not in common]


# Codewars solution
def array_diff(a, b):
    return [x for x in a if x not in b]