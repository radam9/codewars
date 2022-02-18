# https://www.codewars.com/kata/554ca54ffa7d91b236000023
# 6 kyu
# Delete occurrences of an element if it occurs more than n times

# my original solution
def delete_nth(order, max_e):
    a = set(order)
    for e in a:
        if order.count(e) > max_e:
            for i in range(order.count(e) - max_e):
                order = order[::-1]
                order.remove(e)
                order = order[::-1]
    return order


# My Modified solution
def delete_nth(order, max_e):
    a = set(order)
    order = order[::-1]
    for e in a:
        if order.count(e) > max_e:
            for i in range(order.count(e) - max_e):
                order.remove(e)
    return order[::-1]


# codewars solution
def delete_nth(order, max_e):
    ans = []
    for o in order:
        if ans.count(o) < max_e:
            ans.append(o)
    return ans
