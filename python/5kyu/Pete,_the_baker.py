# https://www.codewars.com/kata/525c65e51bf619685c000059
# 5 Kyu
# Pete, the baker

# My Solution
def cakes(recipe, available):
    if len(recipe) > len(available):
        return 0
    cakes = [int(available.get(key) / recipe.get(key)) for key in recipe]
    return min(cakes)


# Codewares Solution
def cakes(recipe, available):
    return min(available.get(e, 0) / recipe[e] for e in recipe)

