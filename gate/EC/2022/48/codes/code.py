import numpy as np

# Define a matrix with string entries
matrix = np.array([
    ["p7", "p1", "p4"],
    ["p3", "p2", 0],
    ["p6", 0, "p5"]
])

# Use numpy's print function to display the matrix
print("Transition Matrix\n",matrix)
print("The following options are correct \np7+p1+p4=1\np3+p2 = p6+p5")
