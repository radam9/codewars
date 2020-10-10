def func(x):
    y = "".join(str(ex) for ex in x)
    return f"({y[:3]}) {y[3:6]}-{y[6:]}"


a = func([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
a
