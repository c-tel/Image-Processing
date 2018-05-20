import cv2
import numpy as np
import sys
step = 35


def split_on_segments(img: np.ndarray) -> None:
    h, w = img.shape
    sys.setrecursionlimit((h*w)//100)
    visited = [[False for _ in range(w)] for _ in range(h)]
    deltas = [(1, 0), (0, 1), (1, 1), (-1, -1), (-1, 1), (1, -1), (-1, 0), (0, -1)]
    cur_color = 100

    def match(x, y):
        return not visited[x][y] and img[x, y]

    neighbours = []
    for i in range(h):
        for j in range(w):
            if match(i, j):
                neighbours.append((i, j))
                while neighbours:
                    k, l = neighbours.pop()
                    img[k, l] = cur_color
                    visited[k][l] = True
                    for m, n in deltas:
                        if h > k+m >= 0 and w > l+n >= 0 and match(k+m, l+n):
                            neighbours.append((k+m, l+n))
                cur_color += step


if __name__ == '__main__':
    dog = cv2.imread('figures.png', 0)
    split_on_segments(dog)
    cv2.imshow('res', dog)
    cv2.waitKey(0)
