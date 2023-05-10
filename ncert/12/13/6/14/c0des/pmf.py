import matplotlib.pyplot as plt
import numpy as np

pmf = np.array([1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8])

#possible values are
values = np.arange(1,9)

fig, ax = plt.subplots()
ax.stem(values,pmf[:len(values)], use_line_collection=True)

ax.set_xlabel('Outcome')
ax.set_ylabel('PMF')
ax.set_title('pmf of outcomes after spinning')

ax.set_xticks(values)
ax.set_xticklabels(values)

ax.set_ylim([0, 1/6])

plt.show()
