

from random_walk import RandomWalk

import matplotlib.pyplot as plt


rw=RandomWalk()

rw.fill_walk()
plt.scatter(rw.x_values,rw.y_values,s=15)
plt.show()
