import cv2
from matplotlib import pyplot as plot


def equalize(img):
    cv2.imshow('before', img)
    plot.hist(img.ravel(), 256, [0, 256])
    plot.show()

    rows, cols = img.shape
    alpha = 255 / (rows * cols)

    hist = [0 for _ in range(256)]
    for x in range(rows):
        for y in range(cols):
            hist[img[x, y]] += 1

    cum_sum = [hist[0]]
    for i in hist[1:]:
        cum_sum.append(cum_sum[-1] + i)

    for i in range(rows):
        for j in range(cols):
            img[i, j] = cum_sum[img[i, j]] * alpha

    cv2.imshow('after', img)
    plot.hist(img.ravel(), 256, [0, 256])
    plot.show()

    cv2.waitKey(0)


if __name__ == '__main__':
    equalize(cv2.imread('Geneva.tif', 0))
