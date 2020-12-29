# https://www.codewars.com/kata/51c8e37cee245da6b40000bd
# 4 Kyu
# Strip Comments

# My Solution
def solution(string, markers):
    lines = string.splitlines()
    for marker in markers:
        lines = [line.split(marker)[0].strip() for line in lines]
    return "\n".join(lines)


# My Nasty Solution
def solution(string, markers):
    lines = string.splitlines()
    for marker in markers:
        lines = [
            "".join(list(line)[: (line.index(marker))]).rstrip()
            if marker in line
            else line
            for line in lines
        ]
    return "\n".join(lines)