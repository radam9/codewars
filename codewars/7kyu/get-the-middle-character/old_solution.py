# https://www.codewars.com/kata/56747fd5cb988479af000028
# 7 Kyu
# Get the Middle Character

# My Solution
def get_middle(string):
    length = len(string)
    center = length // 2
    if length % 2 == 0:
        return string[center - 1 : center + 1]
    else:
        return string[center]


# Codewars Solution 1
def get_middle(s):
    return s[(len(s) - 1) // 2 : len(s) // 2 + 1]


# Codewars Solution 2
def get_middle(s):
    index, odd = divmod(len(s), 2)
    return s[index] if odd else s[index - 1 : index + 1]


# Codewars Inspired Solution
def get_middle(string):
    length = len(string)
    return string[(length - 1) // 2 : length // 2 + 1]
