import numpy as np


def dist_euclidiana_np(v1, v2):
    v1, v2 = np.array(v1), np.array(v2)
    diff = v1 - v2
    quad_dist = np.dot(diff, diff)
    return math.sqrt(quad_dist)

X = np.array([1.3, 2.5, 3.0, 4.1])
Y = np.array([4.7, 3.4, 2.2, 1.7])

print('%.2f' % dist_euclidiana_np(X, Y))
