# https://www.codewars.com/kata/56a5d994ac971f1ac500003e
# 6 kyu
# Consecutive strings

# my original solution
def longest_consec(strarr, k):
    if (k <= 0) or (len(strarr) == 0) or (k > len(strarr)):
        return ""
    a = ""
    for i in range(len(strarr) - k + 2):
        t = "".join(strarr[i : i + k])
        if len(t) > len(a):
            a = t
    return a


# codewars solution
def longest_consec(strarr, k):
    result = ""

    if k > 0 and len(strarr) >= k:
        for index in range(len(strarr) - k + 1):
            s = "".join(strarr[index : index + k])
            if len(s) > len(result):
                result = s

    return result
