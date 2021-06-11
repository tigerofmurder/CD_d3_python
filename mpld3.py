import matplotlib.pyplot as plt
import numpy as np
import mpld3

fig, ax = plt.subplots()
np.random.seed(0)
ax.plot(np.random.normal(size=100),
        np.random.normal(size=100),
        'or', ms=10, alpha=0.3)
ax.plot(np.random.normal(size=100),
        np.random.normal(size=100),
        'ob', ms=20, alpha=0.1)

ax.grid(color='lightgray', alpha=0.7)

mpld3.show(fig)