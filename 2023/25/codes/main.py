import numpy as np
import matplotlib.pyplot as plt

num_samples = 10000
num_simulations = 1000
sigma_0 = 1.0

sigma_hat_1 = np.zeros(num_simulations)
sigma_hat_2 = np.zeros(num_simulations)

for i in range(num_simulations):
    samples = np.random.normal(0, sigma_0, num_samples)
    sigma_hat_1[i] = np.sum(samples**2) / num_samples
    sigma_hat_2[i] = np.sum(samples**2) / (num_samples - 1)

plt.figure(figsize=(8, 6))

plt.scatter(range(num_simulations), sigma_hat_1, c='b', marker='o', label=r'$\hat{\sigma}^2_1$')
plt.scatter(range(num_simulations), sigma_hat_2, c='g', marker='o', label=r'$\hat{\sigma}^2_2$')

mean_sigma_hat_1 = np.mean(sigma_hat_1)
mean_sigma_hat_2 = np.mean(sigma_hat_2)

plt.axhline(sigma_0**2, color='r', linestyle='solid', linewidth=2, label=r'Theoretical $\sigma_0^2$', alpha=0.7)
plt.axhline(mean_sigma_hat_1, color='b', linestyle='dashed', linewidth=2, label=r'Mean $\hat{\sigma}^2_1$', alpha=0.7)
plt.axhline(mean_sigma_hat_2, color='g', linestyle='dashed', linewidth=2, label=r'Mean $\hat{\sigma}^2_2$', alpha=0.7)

plt.xlabel('Simulation Number')
plt.ylabel(r'$\mathrm{E}(\sigma^2)$')  # LaTeX formatting with \mathrm for upright font
plt.title('Scatter Plot of $\hat{\sigma}^2_1$ and $\hat{\sigma}^2_2$ vs. Theoretical $\sigma_0^2$')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

