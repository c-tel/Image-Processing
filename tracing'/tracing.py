import numpy as np
import cv2


class Bounds:
    __neighbours = [(0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)]

    @staticmethod
    def __temp_dir(prev_dir):
        return (prev_dir + (6 if prev_dir % 2 else 7)) % 8

    def __init__(self, path_to_img: str):
        self.img = cv2.imread(path_to_img, 0)
        self.contour = []
        self.__do_trace()
        self.__build_bounds_img()

    def __start_pxl(self) -> (int, int):
        h, w = self.img.shape
        for i in range(h):
            for j in range(w):
                if self.img[i, j] == 255:
                    return i, j

    def __next_pxl(self, prev_ind: (int, int), prev_dir: int) -> (tuple, int):
        temp_dir = Bounds.__temp_dir(prev_dir)
        for i in range(8):
            cur_ind = prev_ind[0] + Bounds.__neighbours[temp_dir][0], prev_ind[1] + Bounds.__neighbours[temp_dir][1]
            if self.img[cur_ind] == 255:
                return cur_ind, temp_dir
            temp_dir = 0 if temp_dir == 7 else temp_dir + 1

    def __do_trace(self):
        start = self.__start_pxl()
        self.contour.append(start)
        cur_pxl, cur_dir = self.__next_pxl(start, 7)
        while not cur_pxl == start:
            self.contour.append(cur_pxl)
            cur_pxl, cur_dir = self.__next_pxl(cur_pxl, cur_dir)

    def __build_bounds_img(self) -> np.ndarray:
        self.contour_img = np.zeros(self.img.shape, np.uint8)
        for pxl in self.contour:
            self.contour_img[pxl] = 255


if __name__ == '__main__':
    bounds = Bounds('contour.tif')
    print(len(bounds.contour))
    cv2.imshow('res', bounds.contour_img)
    cv2.waitKey(0)
