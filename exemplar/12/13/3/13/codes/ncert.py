import numpy as np
import matplotlib.pyplot as plt

# Simulated Values - Using 10000 dice rolls
def dice_roll(n):
        dice = np.array(np.random.randint(1, 7, size=n)) 
        return dice

dice = dice_roll(10000)
result = np.where(dice == 1, 1, -1)
result = np.where(dice == 6, 1, result)
result = np.where(dice == 3, 4, result)
print("Expected Profit per dice roll = ",np.sum(result)/10000)