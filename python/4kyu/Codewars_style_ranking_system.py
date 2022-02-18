# https://www.codewars.com/kata/51fda2d95d6efda45e00004e
# 4 kyu
# Codewars style ranking system

# My Solution
class User:
    RANKS = tuple(x for x in range(-8, 9) if x != 0)

    def __init__(self):
        self.rank = -8
        self.progress = 0

    def inc_progress(self, task_rank):
        diff = __class__.RANKS.index(task_rank) - __class__.RANKS.index(self.rank)
        if 17 > diff > 0:
            self.progress += 10 * diff * diff
        elif diff == 0:
            self.progress += 3
        elif diff == -1:
            self.progress += 1
        while self.progress >= 100 and self.rank < 8:
            old_rank_index = __class__.RANKS.index(self.rank)
            self.rank = __class__.RANKS[old_rank_index + 1]
            self.progress -= 100

        if self.rank == 8:
            self.progress = 0