# https://www.codewars.com/kata/51ba717bb08c1cd60f00002f
# 4 kyu
# Range Extraction

# My Solution
from itertools import groupby


def solution(array):
    result = []
    for _, group in groupby(enumerate(array), key=lambda x: x[0] - x[1]):
        range_ = [value for key, value in group]
        if len(range_) <= 2:
            result.extend([str(item) for item in range_])
        else:
            result.append(f"{range_[0]}-{range_[-1]}")
    return ",".join(result)


# Codewars Solution
def solution(args):
    out = []
    beg = end = args[0]

    for n in args[1:] + [""]:
        if n != end + 1:
            if end == beg:
                out.append(str(beg))
            elif end == beg + 1:
                out.extend([str(beg), str(end)])
            else:
                out.append(str(beg) + "-" + str(end))
            beg = n
        end = n

    return ",".join(out)
