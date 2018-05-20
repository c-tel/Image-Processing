import numpy as np
import cv2
from tracing import Bounds
from math import atan2
from matplotlib import pyplot as plt


def vec_len(vec):
    return (vec[0] ** 2 + vec[1] ** 2) ** 0.5


def curvature(contour: list, k: int=1):
    n = len(contour)
    res = np.zeros(n)

    def curv_i(i: int):
        cur = contour[i]
        next = contour[(i+k) % n]
        prev = contour[(i-k) % n]
        f_vec = cur[0] - next[0], cur[1] - next[1]
        b_vec = cur[0] - prev[0], cur[1] - prev[1]
        mod_f = vec_len(f_vec)
        mod_b = vec_len(b_vec)
        arg_f = atan2(abs(f_vec[0]), abs(f_vec[1]))
        arg_b = atan2(abs(b_vec[0]), abs(b_vec[1]))
        mean = (arg_f + arg_b)/2
        arg_dif = abs(arg_f - mean)
        return arg_dif*(mod_b+mod_f) / (2*mod_b*mod_f)

    for i in range(n):
        res[i] = curv_i(i)
    plt.plot(res)
    plt.show()


if __name__ == '__main__':
    bounds6 = Bounds('6.png')
    bounds = Bounds('romb.png')
    bounds0 = Bounds('circle.png')
    cont_vec = bounds.contour
    cont_vec6 = bounds6.contour
    cont_vec0 = bounds0.contour

    curvature(cont_vec, 1)
    curvature(cont_vec6, 5)
    curvature(cont_vec0, 10)
