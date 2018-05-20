import cv2
import numpy as np

if __name__ == '__main__':
    img = cv2.imread('dog.png')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    sift = cv2.xfeatures2d.SIFT_create()
    kp = sift.detect(gray, None)
    img = cv2.drawKeypoints(gray, kp, img)
    cv2.imwrite('sift_keypoints.jpg', img)
