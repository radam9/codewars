# https://www.codewars.com/kata/55e0467217adf9c3690000f9/train/python
# 5 Kyu
# My Very Own Python's Split Function

# My Solution
def my_very_own_split(string, delimiter=None):
    if delimiter == "":
        raise
    delimiter = delimiter or " "
    temp = ""
    new_string = ""
    for s in string:
        if s == "\t" and temp == "\t":
            continue
        else:
            new_string += ""
        if s != temp:
            new_string += s
        temp = s
    d = len(delimiter)
    print(f"String: {string}\nDelimiter: '{delimiter}'")
    while True:
        index = string.find(delimiter)
        if index == 0:
            string = string[d::]
            yield ""
        if index == -1:
            if string:
                yield string
            break
        part = string[:index]
        string = string[index + d :]
        yield part


for a in my_very_own_split("abc def ghi jklmno    prrrr", " "):
    print(a)
x = 0