__version__ = "1"

from mpl_toolkits.mplot3d import proj3d
import numpy as np

def plot_thing(ax):
    points = np.random.random((100, 3))
    ax.plot(*points.T, marker='.', ls='',
            label='random point', ms=1)
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_zlabel('$z$')
    ax.legend()
