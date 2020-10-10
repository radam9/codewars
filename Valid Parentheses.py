# https://www.codewars.com/kata/52774a314c2333f0a7000688
# 5 Kyu
# Valid Parentheses


# My Solution
def valid_parentheses(string):
    counter = 0
    for s in string:
        if s == "(":
            counter += 1
        elif s == ")":
            counter -= 1
        if counter < 0:
            return False
    if counter != 0:
        return False
    return True


# Codewars Solution
def valid_parentheses(string):
    counter = 0
    for s in string:
        if s == "(":
            counter += 1
        elif s == ")":
            counter -= 1
        if counter < 0:
            return False
    return counter == 0
