"""
=======
Example
=======

"""

from rtd_min_fail import plot_thing

import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plot_thing(ax)
plt.show()
