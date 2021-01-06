# https://www.codewars.com/kata/57814d79a56c88e3e0000786
# 6 kyu
# Simple Encryption #1 - Alternating Split

# my original solution
def decrypt(encrypted_text, n):
    nt = encrypted_text
    if nt == None or len(nt) <= 0:
        return nt
    i = len(nt) // 2
    if n > 0:
        for _ in range(n):
            if len(nt) % 2 == 0:
                nt = "".join(map(lambda x, y: x + y, nt[i:], nt[:i]))
            else:
                nt = "".join(map(lambda x, y: x + y, nt[i:], nt[:i])) + nt[-1]
    return nt


def encrypt(text, n):
    if text == None or len(text) <= 0:
        return text
    if n > 0:
        for _ in range(n):
            text = text[1::2] + text[::2]
    return text

