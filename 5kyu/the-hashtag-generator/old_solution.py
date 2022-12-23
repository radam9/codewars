# https://www.codewars.com/kata/52449b062fb80683ec000024
# 5 kyu
# The Hashtag Generator

# My First Solution


def generate_hashtag(s):
    if not s:
        return False
    new_s = [x.capitalize() for x in s.strip().split()]
    new_s.insert(0, "#")
    new_s = "".join(new_s)
    return new_s if len(new_s) <= 140 else False


# My Second Solution
def generate_hashtag(s):
    new_s = [x.capitalize() for x in s.strip().split()]
    new_s.insert(0, "#")
    new_s = "".join(new_s)
    return False if (len(s) == 0 or len(new_s) > 140) else new_s


# My Third Solution
def generate_hashtag(s):
    new_s = "".join([x.capitalize() for x in s.strip().split()])
    new_s = "#" + new_s
    return False if (len(s) == 0 or len(new_s) > 140) else new_s


# Codewars Solution
def generate_hashtag(s):
    output = "#"
    for word in s.split():
        output += word.capitalize()
    return False if (len(s) == 0 or len(output) > 140) else output
