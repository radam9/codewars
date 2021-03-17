# https://www.codewars.com/kata/5842df8ccbd22792a4000245
# 6 Kyu
# Write Number in Expanded Form


# My Solution
def expanded_form(num):
    values = []
    tens = 10
    while num > 0:
        n = num % tens
        if n != 0:
            values.append(str(n))
        num = num - n
        tens *= 10
    return " + ".join(values[::-1])


# Codewars Solution
def expanded_form(num):
    num = str(num)
    return " + ".join(
        c + "0" * (len(num) - i - 1) for i, c in enumerate(num) if c != "0"
    )
