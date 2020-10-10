# https://www.codewars.com/kata/52a89c2ea8ddc5547a000863/train/python
# 5 Kyu
# Can you get the loop ?

# My Solution (Very Slow)
def loop_size(node):
    nodes = []
    while node not in nodes:
        nodes.append(node)
        node = node.next
    length = len(nodes) - nodes.index(node)
    return length


# My Second Solution (Inspired by Codewars Solutions - A lot faster [about 12 times faster])
def loop_size(node):
    nodes = {}
    count = 0
    while node not in nodes:
        nodes[node] = count
        node = node.next
        count += 1
    return count - nodes[node]


# Tortoise and Rabbit Codewars Solution
def loop_size(node):
    turtle, rabbit = node.next, node.next.next

    # Find a point in the loop.  Any point will do!
    # Since the rabbit moves faster than the turtle
    # and the kata guarantees a loop, the rabbit will
    # eventually catch up with the turtle.
    while turtle != rabbit:
        turtle = turtle.next
        rabbit = rabbit.next.next

    # The turtle and rabbit are now on the same node,
    # but we know that node is in a loop.  So now we
    # keep the turtle motionless and move the rabbit
    # until it finds the turtle again, counting the
    # nodes the rabbit visits in the mean time.
    count = 1
    rabbit = rabbit.next
    while turtle != rabbit:
        count += 1
        rabbit = rabbit.next

    # voila
    return count
