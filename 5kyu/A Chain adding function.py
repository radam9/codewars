# https://www.codewars.com/kata/539a0e4d85e3425cb0000a88/solutions/python
# 5 Kyu
# A Chain adding function

# Codewars Solution
class add(int):
    def __call__(self, n):
        return add(self + n)
