import numpy as np

simlen = 10000000

test = np.random.choice([1, 2, 3, 4, 5, 6], size=simlen, p=[(2/9), (1/9), (2/9), (1/9), (2/9), (1/9)])

print("Actual:", (4/9))
print("Experimental:", (test > 3).mean())

