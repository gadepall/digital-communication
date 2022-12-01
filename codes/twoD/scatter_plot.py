import matplotlib.pyplot as plt
import numpy as np
mean = [0, 0]
cov = [[1, 0], [0, 1]]  # diagonal covariance
A = 10
simlen = int(1e4)
n1, n2 = np.random.multivariate_normal(mean, cov, simlen).T
y1 = A + n1
y2 = n2
plt.plot( y1, y2, 'bx')


n1, n2 = np.random.multivariate_normal(mean, cov, simlen).T
y1 = n1
y2 = A + n2
plt.plot(y1, y2, 'rx')
plt.legend(['$\mathbf{x} = \mathbf{s}_0$','$\mathbf{x} = \mathbf{s}_1$'])
plt.xlabel("$y_1$")
plt.ylabel("$y_2$")

plt.show()
