import cv2
import numpy as np


def count_g(z1, z2, z3, z4, z6, z7, z8, z9):
    gx = z7 + 2 * z8 + z9 - z1 - 2 * z2 - z3
    gy = z3 + 2 * z6 + z9 - z1 - 2 * z4 - z7
    return ((gx ** 2) + (gy ** 2))**0.5


def apply_filter(img: np.ndarray) -> np.ndarray:
    cv2.imshow('before', img)
    res = np.zeros(img.shape, np.uint8)
    h, w = img.shape
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            res[i, j] = img[i, j]
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            res[i, j] = count_g(img[i - 1, j - 1], img[i-1, j], img[i - 1, j + 1],
                                img[i, j - 1], img[i, j + 1],
                                img[i + 1, j - 1], img[i + 1, j], img[i + 1, j+1])
    cv2.imshow('after', res)
    cv2.waitKey(0)


if __name__ == '__main__':
    image = cv2.imread('valve.png', 0)
    apply_filter(image)


