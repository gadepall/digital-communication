import numpy as np

n = 1000
set = np.random.randint(1, 100, size=n)

div = set % 7 == 0
div_count = np.sum(div)

print("prb of div =", div_count / n)
print("prb of not div =", (n - div_count) / n)
