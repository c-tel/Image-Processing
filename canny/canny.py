import cv2
import numpy as np
import sobel
from math import pi, atan2


def blur(img: np.ndarray) -> np.ndarray:
    return cv2.GaussianBlur(img, (7, 7), 1)


# set pixel to zero if it is not local maximum
def non_max_suppression(mods: np.ndarray, args: np.ndarray) -> np.ndarray:
    h, w = args.shape
    for i in range(h):
        for j in range(w):
            args[i, j] = normalize(args[i, j])
    res = np.copy(mods)
    for i in range(1, h-1):
        for j in range(1, w-1):
            k, l, m, n = neighbours(args[i, j], i, j)
            if not (mods[i, j] > mods[k, l] and mods[i, j] > mods[m, n]):
                res[i, j] = 0
    return res


# neighbours to check depend on gradient angle
def neighbours(arg, i: int, j: int) -> (int, int, int, int):
    if arg == pi/4:
        return i+1, j-1, i-1, j+1
    if arg == pi/2:
        return i - 1, j, i + 1, j
    if arg == 3*pi/4:
        return i-1, j-1, i+1, j+1
    if arg == pi:
        return i, j-1, i, j+1
    return i - 1, j - 1, i + 1, j + 1


# round angle to pi/4
def normalize(arg):
    arg = round(arg/(pi/4))*pi/4
    return arg if arg > 0 else arg+pi


def double_threshold(suppressed, high, low):
    h, w = suppressed.shape
    for i in range(1, h-1):
        for j in range(1, w-1):
            if suppressed[i, j] > high:
                suppressed[i, j] = 255
            elif suppressed[i, j] < low:
                suppressed[i, j] = 0
    deltas = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    for i in range(1, h-1):
        for j in range(1, w-1):
            if low <= suppressed[i, j] <= high:
                sum = 0
                for k, l in deltas:
                    sum += suppressed[i+k, j+l]
                if sum > 255:
                    img[i, j] = 255
                else:
                    img[i, j] = 0
    return suppressed


if __name__ == '__main__':
    img = blur(cv2.imread('valve.png', 0))
    mods, args = sobel.apply_filter(img)
    buf = non_max_suppression(mods, args)
    cv2.imshow('res1', double_threshold(buf, 200, 50))
    cv2.waitKey(0)
