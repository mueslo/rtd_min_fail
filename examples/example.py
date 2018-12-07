"""
=======
Example
=======

"""

import matplotlib.pyplot as plt

from rtd_min_fail import plot_thing

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plot_thing(ax)
plt.show()
