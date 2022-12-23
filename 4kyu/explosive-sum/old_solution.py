# https://www.codewars.com/kata/52ec24228a515e620b0005ef
# 4 Kyu
# Explosive Sum


def Q(n):
    # Represent polynomial as a list of coefficients from x^0 to x^n.
    # G_0 = 1
    G = [int(g_pow == 0) for g_pow in range(n + 1)]
    for k in range(1, n):
        # G_k = G_{k-1} * (1 + x^k)
        # This is equivalent to adding G shifted to the right by k to G
        # Ignore powers greater than n since we don't need them.
        G = [
            G[g_pow] if g_pow - k < 0 else G[g_pow] + G[g_pow - k]
            for g_pow in range(n + 1)
        ]
    return G[n]


def exp_sum(number):
    polynomial = [int(exponent == 0) for exponent in range(number + 1)]
    for index in range(1, number):
        polynomial = [
            polynomial[exponent]
            if exponent - index < 0
            else polynomial[exponent] + polynomial[exponent - index]
            for exponent in range(number + 1)
        ]
    return sum(polynomial)
