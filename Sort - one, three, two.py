# https://www.codewars.com/kata/56f4ff45af5b1f8cd100067d/train/python
# 5 Kyu
# Sort : one, three, two

# My Solution
def sort_by_name(array):
    numtoword = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
    }
    wordtonum = {}
    result = []
    for num in array:
        numasword = ""
        hundreds = num // 100
        tens = (num - hundreds * 100) // 10
        units = num - (hundreds * 100 + tens * 10)
        if hundreds and (tens or units):
            numasword = f"{numtoword[hundreds]} hundred and "
        elif hundreds:
            numasword = f"{numtoword[hundreds]} hundred"
        if tens == 1:
            numasword += f"{numtoword[num - hundreds * 100]}"
        elif tens > 1:
            numasword += f"{numtoword[tens * 10]} "
        if units != 0 and tens != 1:
            numasword += numtoword[units]
        if not numasword:
            numasword = "zero"
        result.append(numasword)
        wordtonum[numasword] = num
    result.sort()
    return [wordtonum[r] for r in result]


# Codewars Solution
def int_to_word(num):
    d = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
    }

    assert 0 <= num

    if num < 20:
        return d[num]

    if num < 100:
        if num % 10 == 0:
            return d[num]
        else:
            return d[num // 10 * 10] + "-" + d[num % 10]

    if num < 1000:
        if num % 100 == 0:
            return d[num // 100] + " hundred"
        else:
            return d[num // 100] + " hundred and " + int_to_word(num % 100)


def sort_by_name(arr):
    return sorted(arr, key=int_to_word)