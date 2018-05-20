import cv2
import numpy as np


def hist(image: np.ndarray) -> list:
    h, w = image.shape
    res = [0 for _ in range(256)]
    for i in range(h):
        for j in range(w):
            res[image[i, j]] += 1
    return res


def threshold(image: np.ndarray) -> int:
    t_prev = 0
    t_cur = 128
    imhist = hist(image)
    while not t_prev == t_cur:
        u0 = sum([i*imhist[i] for i in range(t_cur)]) / sum(imhist[:t_cur])
        u1 = sum([i*imhist[i] for i in range(t_cur+1, len(imhist))]) / sum(imhist[t_cur+1:])
        t_prev = t_cur
        t_cur = round((u0+u1)/2)
    return t_cur


def segmentation(image: np.ndarray) -> None:
    t = threshold(image)
    h, w = image.shape
    for i in range(h):
        for j in range(w):
            image[i, j] = 0 if image[i, j] < t else 255


if __name__ == '__main__':
    img = cv2.imread('chair.jpg', 0)
    segmentation(img)
    cv2.imshow('res', img)
    cv2.waitKey(0)
