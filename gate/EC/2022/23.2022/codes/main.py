import matplotlib.pyplot as plt
import numpy as np

def plot_function(a):
    x = np.linspace(-10, 10, 1000)
    y = (np.abs(x) <= a).astype(int)  

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_xlabel('Frequency')
    ax.set_ylabel('|H(f)|')
    ax.grid(True)
    ax.set_xticks([-a, a,0])
    ax.set_xticklabels(['-a', 'a','0'])
    ax.set_yticks([0, 1])
    plt.savefig("../figs/figure.png")
    plt.show()
a = 5
plot_function(a)
