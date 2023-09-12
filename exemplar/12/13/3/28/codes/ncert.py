import numpy as np
import matplotlib.pyplot as plt

# Simulated Values - Using 10000 dice rolls
def dice_roll(n):
        dice = np.array(np.random.randint(1, 7, size=(n,3)))
        return dice

dice = dice_roll(10000)
print("Expected Profit per dice roll = ",np.count_nonzero(dice==2)/10000)