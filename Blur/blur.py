import cv2
import numpy as np
from cmath import pi, e


class Blur:
    def wg(self, x: int, y: int) -> float:
        return round(1/(2 * pi * self.sigma**2)*(e**(-(x*x+y*y)/(2*self.sigma**2))), 5)

    def __init__(self, n: int, sigma: float):
        self.n = n
        self.sigma = sigma
        self.mask = np.zeros((n, n))
        self.delta = n//2
        for i in range(n):
            for j in range(n):
                self.mask[i, j] = self.wg(i-self.delta, j-self.delta)

    def filter(self, img: np.ndarray) -> np.ndarray:
        cv2.imshow('before', img)
        res = np.zeros(img.shape, np.uint8)
        h, w = img.shape
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                res[i, j] = img[i, j]
        for i in range(self.delta, h - self.delta):
            for j in range(self.delta, w - self.delta):
                pxl = 0
                for k in range(self.n):
                    for l in range(self.n):
                        pxl += img[i + k - self.delta, j + l - self.delta] * self.mask[k, l]
                res[i, j] = pxl
        cv2.imshow('after', res)
        cv2.waitKey(0)


if __name__ == '__main__':
    n = int(input('Enter the size of mask'))
    s = float(input('Enter the sigma'))
    b = Blur(n, s)
    img = cv2.imread('dog.png', 0)
    b.filter(img)
