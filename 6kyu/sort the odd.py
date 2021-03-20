# https://www.codewars.com/kata/578aa45ee9fd15ff4600090d
# 6 Kyu
# Sort the odd

# My Solution
def sort_array(array):
    new_array = sorted([a for a in array if a % 2 == 1])
    for index, item in enumerate(array):
        if item % 2 == 0:
            new_array.insert(index, item)
    return new_array


# Codewars Solution
def sort_array(arr):
    odds = sorted((x for x in arr if x % 2 != 0), reverse=True)
    return [x if x % 2 == 0 else odds.pop() for x in arr]
