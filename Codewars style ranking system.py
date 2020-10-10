# https://www.codewars.com/kata/51fda2d95d6efda45e00004e
# 4 kyu
# Codewars style ranking system

# My Solution
class User:
    RANKS = [x for x in range(-8, 9) if x != 0]

    def __init__(self):
        self.rank = -8
        self.progress = 0

    def inc_progress(self, task_rank):
        diff = task_rank - self.rank
        if 17 > diff > 0:
            self.progress += 10 * diff * diff
        elif diff == 0:
            self.progress += 3
        elif diff == -1:
            self.progress += 1
        if self.progress >= 100:
            remainder = self.progress % 100
            rank = (self.progress - remainder) / 100
            self.progress = remainder
            try:
                old_rank_index = __class__.RANKS.index(self.rank)
                self.rank = __class__.RANKS[old_rank_index + rank]
            except IndexError:
                self.rank = 8
                self.progress = 0

