import numpy as np
import math


def G(z1, z2, z3, z4, z6, z7, z8, z9) -> (float, float):
    gx = z7 + 2 * z8 + z9 - z1 - 2 * z2 - z3
    gy = z3 + 2 * z6 + z9 - z1 - 2 * z4 - z7
    return gx, gy


def apply_filter(img: np.ndarray) -> (np.ndarray, np.ndarray):
    mods = np.zeros(img.shape, np.uint8)
    args = np.zeros(img.shape, np.uint8)
    h, w = img.shape
    for i in range(h):
        for j in range(w):
            mods[i, j] = img[i, j]
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            gx, gy = G(img[i - 1, j - 1], img[i - 1, j], img[i - 1, j + 1],
                       img[i, j - 1], img[i, j + 1],
                       img[i + 1, j - 1], img[i + 1, j], img[i + 1, j + 1])
            mods[i, j] = ((gx**2)+(gy**2))**0.5
            args[i, j] = math.atan2(gy, gx)
    return mods, args
