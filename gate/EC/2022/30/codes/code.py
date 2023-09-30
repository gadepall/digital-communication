import numpy as np
import matplotlib.pyplot as plt

# Define the range of angular frequencies
w = np.linspace(-10, 10, 1000)

# Calculate the PSD S_X(w)
S_X = 2 / (9 + w**2)

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(w, S_X, label='S_X(w) = 2 / (9 + w^2)')
plt.title('Power Spectral Density S_X(w)')
plt.xlabel('Angular Frequency (w)')
plt.ylabel('S_X(w)')
plt.grid(True)
plt.legend()
plt.show()

