import cv2
import numpy as np


if __name__ == '__main__':
    # 相对地址
    img = cv2.imread('data/me.png')
    makeup = cv2.imread('data/facialMakeup/3.png')
    print(makeup.shape)
    makeup = cv2.resize(makeup, dsize=(makeup.shape[1]//2, makeup.shape[0]//2))
    print(makeup.shape)
    cv2.imshow('img', makeup)
    cv2.waitKey(0)


    # 生成了一个全255矩阵，(0, 0, 0)
    mask = 255 * np.ones(makeup.shape, makeup.dtype)
    # cv2中的长宽，是反的
    output = cv2.seamlessClone(makeup, img, mask, (img.shape[1]//2, img.shape[0]//2), cv2.MONOCHROME_TRANSFER)


    cv2.imshow('img', output)
    cv2.waitKey(0)