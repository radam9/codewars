# https://www.codewars.com/kata/5709bdd2f088096786000008
# 8 Kyu
# noobCode 01: SUPERSIZE ME.... or rather, this integer!

# My Solution
n = 56789
a = [x for x in str(n)]
int("".join(a.sort(reverse=True)))
