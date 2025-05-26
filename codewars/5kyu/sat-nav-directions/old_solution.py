# https://www.codewars.com/kata/5a9b4d104a6b341b42000070
# 5 Kyu
# Sat Nav directions

# My Solution
def sat_nav(directions):
    car = Car()
    for d in directions:
        msg = d.split()
        if "Head" in d:
            car.head(msg[-1])
        elif "Take" in d:
            car.turn(msg[-1], msg[-2])
        elif "Go" in d:
            value = msg[-1]
            if "km" in value:
                distance = int(float(value[:-2]) * 10)
            else:
                distance = int(int(value[:-1]) / 100)
            car.move(distance)
        elif "Turn" in d:
            car.turn("TURN")
        else:
            print(car.location)
            return car.location


class Car(object):
    COMPASS = {"NORTH": [0, 1], "EAST": [1, 0], "SOUTH": [0, -1], "WEST": [-1, 0]}
    STEPS = {"NEXT": 10, "2nd": 20, "3rd": 30, "4th": 40, "5th": 50}
    COMP = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    DICT = {"LEFT": -1, "RIGHT": 1, "TURN": 2}

    def __init__(self):
        self.location = [0, 0]
        self.bearing = []

    def head(self, direction: str):
        self.bearing = __class__.COMPASS[direction]

    def move(self, step: int):
        self.location[0] += step * self.bearing[0]
        self.location[1] += step * self.bearing[1]

    def turn(self, direction: str, step=None):
        if step:
            step = __class__.STEPS[step]
            if self.bearing[0] != 0:
                if self.location[0] % 10 != 0:
                    step = self.go_to_intersection(step, index=0)
                self.move(step)
            else:
                if self.location[1] % 10 != 0:
                    step = self.go_to_intersection(step, index=1)
                self.move(step)

        current_dir = __class__.COMP.index(self.bearing)
        self.bearing = __class__.COMP[(current_dir + __class__.DICT[direction]) % 4]

    def go_to_intersection(self, step, index):
        modifier = 5 * (self.bearing[index] + 1) - (
            (self.location[index] % 10) * self.bearing[index]
        )
        return step + modifier - 10


# Codewars Solution
import re

N, S, E, W = "NORTH", "SOUTH", "EAST", "WEST"
DIRS = {N: (0, 1), S: (0, -1), E: (1, 0), W: (-1, 0)}
TURNS = {
    "LEFT": {DIRS[N]: DIRS[W], DIRS[S]: DIRS[E], DIRS[E]: DIRS[N], DIRS[W]: DIRS[S]},
    "RIGHT": {DIRS[N]: DIRS[E], DIRS[S]: DIRS[W], DIRS[E]: DIRS[S], DIRS[W]: DIRS[N]},
}

PATTERN = re.compile(
    r"Head (?P<head>\w+)"
    + r"|Take the (?P<nTurn>\d*)(?P<isNext>\w+) (?P<turnTo>LEFT|RIGHT)"
    + r"|Go straight on for (?P<straight>[\d.]+)(?P<unit>k?m)"
    + r"|(?P<flip>Turn around!)"
)


def sat_nav(directions):
    def go(d):
        return x + d * moves[0], y + d * moves[1]

    x, y, moves = 0, 0, (0, 0)
    for i in range(len(directions) - 1):
        d, m = 0, PATTERN.match(directions[i])

        if m.group("straight"):  # Move forward without rounding
            d = round(10 * float(m.group("straight")))
            if m.group("unit") == "m":
                d //= 1000  # Convert "were metters" to hectometers
            x, y = go(d)  # Move

        elif m.group("turnTo"):  # Take next turn:
            d = 10 * (
                m.group("isNext") == "NEXT" or int(m.group("nTurn"))
            )  #    will move one complete block forward...
            x, y = (
                z - z % (10 if dz > 0 else -10) for z, dz in zip(go(d), moves)
            )  #    ...cut the exceeding part (changing the sign of the mod argument handle the direction, thanks to python...!)
            moves = TURNS[m.group("turnTo")][moves]

        elif m.group("flip"):
            moves = -moves[0], -moves[1]  # Turn around, in place
        elif m.group("head"):
            moves = DIRS[m.group("head")]  # Initial direction

    return [x, y]
