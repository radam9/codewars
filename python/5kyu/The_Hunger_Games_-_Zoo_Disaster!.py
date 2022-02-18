# https://www.codewars.com/kata/5902bc7aba39542b4a00003d/train/python
# 5 Kyu
# The Hunger Games - Zoo Disaster!

# My Solution
rules = {
    "antelope": ["grass"],
    "big-fish": ["little-fish"],
    "bug": ["leaves"],
    "bear": ["big-fish", "bug", "chicken", "cow", "leaves", "sheep"],
    "chicken": ["bug"],
    "cow": ["grass"],
    "fox": ["chicken", "sheep"],
    "giraffe": ["leaves"],
    "lion": ["antelope", "cow"],
    "panda": ["leaves"],
    "sheep": ["grass"]
}

def who_eats_who(zoo):
    output = [zoo]
    loop = True
    zoo = zoo.split(",")
    while loop:
        loop = attempt_eating(zoo, output)
    output.append(",".join(zoo))
    return output

def attempt_eating(zoo, output):
    zoo_len = len(zoo) - 1
    for index, creature in enumerate(zoo):
        if 0 < index <= zoo_len and zoo[index - 1] in rules.get(creature, []):
            output.append(f"{creature} eats {zoo[index - 1]}")
            zoo.pop(index - 1)
            return True
        elif 0 <= index < zoo_len and zoo[index + 1] in rules.get(creature, []):
            output.append(f"{creature} eats {zoo[index + 1]}")
            zoo.pop(index + 1)
            return True
    else:
        return False

# Solution influenced by codewars
def who_eats_who(zoo):
    rules = {
        "antelope": ["grass"],
        "big-fish": ["little-fish"],
        "bug": ["leaves"],
        "bear": ["big-fish", "bug", "chicken", "cow", "leaves", "sheep"],
        "chicken": ["bug"],
        "cow": ["grass"],
        "fox": ["chicken", "sheep"],
        "giraffe": ["leaves"],
        "lion": ["antelope", "cow"],
        "panda": ["leaves"],
        "sheep": ["grass"]
    }
    output = [zoo]
    zoo = zoo.split(",")
    while True:
        zoo_len = len(zoo) - 1
        for index, creature in enumerate(zoo):
            if 0 < index <= zoo_len and zoo[index - 1] in rules.get(creature, []):
                eaten = index - 1
                break
            elif 0 <= index < zoo_len and zoo[index + 1] in rules.get(creature, []):
                eaten = index + 1
                break
        else:
            break
        output.append(f"{creature} eats {zoo[eaten]}")
        zoo.pop(eaten)
    output.append(",".join(zoo))
    return output
