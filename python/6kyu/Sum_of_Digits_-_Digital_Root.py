# https://www.codewars.com/kata/541c8630095125aba6000c00
# 6 Kyu
# Sum of Digits / Digital Root

# My Solution
def digital_root(number):
    while len(str(number)) > 1:
        number = sum(int(num) for num in str(number))
    return number


# Codewars solution 1
def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int, str(n))))


# Codewars solution 2
def digital_root(n):
    return n % 9 or n and 9
