import random

def not_adj(desk):
    return not any(desk[i] == "M" and desk[i + 1] == "M" for i in range(len(desk) - 1))

def sim(n):
    desks = ["M", "M", "E", "E", "E", "E"]
    nonadj_count = sum(not_adj(random.sample(desks, len(desks))) for j in range(n))
    prob = nonadj_count/n
    return prob

n = 100000
result = sim(n)
print("The probability that the married couple will have nonadjacent desks is:",result)

