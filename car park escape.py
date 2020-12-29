# https://www.codewars.com/kata/591eab1d192fe0435e000014/train/python
# 5 Kyu
# Car Park Escape

# My Solution
def escape(carpark):
    route = []
    location = 0
    for level in carpark:
        if 2 in level:
            location = level.index(2)
        elif len(route) == 0:
            continue
        if 1 in level:
            goal = level.index(1)
        else:
            goal = len(level) - 1
        steps = location - goal
        if steps > 0:
            route.append("L" + str(steps))
        elif steps < 0:
            route.append("R" + str(abs(steps)))

        if len(route) and "D" in route[-1] and 1 in level:
            route[-1] = "D" + str(int(route[-1][-1]) + 1)
        elif 1 in level:
            route.append("D1")
        location -= steps
    return route
