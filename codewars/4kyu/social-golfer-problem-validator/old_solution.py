# https://www.codewars.com/kata/556c04c72ee1147ff20000c9
# 4 Kyu
# Social Golfer Problem Validator

# My Solution
def valid(schedule):
    group_len_check = list(set(len(day) for day in schedule))
    groups = [group for day in schedule for group in day]
    group_size_check = list(set(len(group) for group in groups))
    daily_players = group_len_check[0] * group_size_check[0]
    unknown_player = set()
    for group in groups:
        unknown_player.update(set(group))
        for grp in groups:
            if grp != group:
                if len(set(group).intersection(set(grp))) > 1:
                    return False
    if any(
        [
            len(group_len_check) != 1,
            len(group_size_check) != 1,
            len(unknown_player) != daily_players,
        ]
    ):
        print(f"len_check: {group_len_check} - size_check: {group_size_check}")
        return False
    for day in schedule:
        play_once_check = set(player for group in day for player in group)
        if len(play_once_check) != (daily_players):
            print(
                f"play_once_check: {play_once_check} - size_check: {4 * group_size_check[0]}"
            )
            return False
    return True


# Codewars Influenced Solution
def valid(schedule):
    daily_group_count = len(schedule[0])
    group_size = len(schedule[0][0])
    players = [player for player in "".join(schedule[0])]
    pairs = {}
    for day in schedule:
        if len(day) != daily_group_count:
            return False
        for group in day:
            if len(group) != group_size:
                return False
            for player in group:
                if player not in players:
                    return False
                if player not in pairs:
                    pairs[player] = set(group)
                else:
                    if len(pairs[player] & set(group)) > 1:
                        return False
                    pairs[player].add(group)
    return True