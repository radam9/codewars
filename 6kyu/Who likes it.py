# https://www.codewars.com/kata/5266876b8f4bf2da9b000362/train/python
# 6 Kyu
# Who likes it?

# My Solution
def likes(names):
    length = len(names)
    if length == 0:
        return f"no one likes this"
    elif length == 1:
        return f"{names[0]} likes this"
    elif length == 2:
        return f"{names[0]} and {names[1]} like this"
    elif length == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    return f"{names[0]}, {names[1]} and {length - 2} others like this"


# Codewars Influenced Solution
def likes(names):
    n = len(names)
    return {
        0: "no one likes this",
        1: "{} likes this",
        2: "{} and {} like this",
        3: "{}, {} and {} like this",
        4: "{}, {} and {others} others like this",
    }[min(4, n)].format(*names[:3], others=n - 2)
