# https://www.codewars.com/kata/53368a47e38700bd8300030d/solutions/python
# 7kyu
# Format a string of names like 'Bart, Lisa & Maggie'.

# my original solution
def namelist(names):
    if len(names) == 0:
        return ""
    elif len(names) == 1:
        return names[0]["name"]
    b = list()
    for i in names:
        b.append(i["name"])
    return ", ".join(b[:-1]) + " & " + b[-1]


# codewars solution
def namelist(names):
    if len(names) == 0:
        return ""
    elif len(names) == 1:
        return names[0]["name"]
    return ", ".join([n["name"] for n in names[:-1]]) + " & " + names[-1]["name"]


# codewars solution2
def namelist(names):
    return ", ".join([name["name"] for name in names])[::-1].replace(",", "& ", 1)[::-1]

