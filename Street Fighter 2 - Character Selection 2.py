# https://www.codewars.com/kata/5853213063adbd1b9b0000be/train/python
# 5 Kyu
# Street Fighter 2 - Character Selection

# My Solution
def super_street_fighter_selection(fighters, position, moves):
    directions = {"right": [0, 1], "left": [0, -1], "up": [-1, 0], "down": [1, 0]}
    chars = []
    y, x = position
    for move in moves:
        dy, dx = directions[move]
        y += dy
        if not 0 <= y < len(fighters) or not fighters[y][x]:
            y -= dy
        x = (x + dx) % len(fighters[y])
        while not fighters[y][x]:
            x = (x + dx) % len(fighters[y])
        chars.append(fighters[y][x])
    return chars