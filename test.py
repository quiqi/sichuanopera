import cv2
import os
import numpy as np
from comm.model import Model


class MakeUp(Model):
    def __init__(self, name: str = 'makeup'):
        super().__init__(name)
        self.makeups = cv2.imread('data/facialMakeup/2.png')

    def run(self, frame: dict):
        img = frame['img']
        bboxs = frame['bboxs']
        for bbox in bboxs:
            h = bbox[2] - bbox[0]
            w = bbox[3] - bbox[1]
            makeup = cv2.resize(self.makeups, dsize=(int(h), int(w)))
            mask = 255 * np.ones(makeup.shape, makeup.dtype)
            frame['img'] = cv2.seamlessClone(makeup, img, mask, (int(bbox[0] + w//2), int(bbox[1] + h//2)), cv2.NORMAL_CLONE)

        return frame


if __name__ == '__main__':
    img = cv2.imread('data/facialMakeup/2.png')
    img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_NEAREST)
    me = cv2.imread('data/me.png')
    mask = 255 * np.ones(img.shape, img.dtype)
    output = cv2.seamlessClone(img, me, mask, (me.shape[0]//2, me.shape[1]//2), cv2.NORMAL_CLONE)
    cv2.imshow('output', output)
    cv2.waitKey()