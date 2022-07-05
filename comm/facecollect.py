import time

import cv2
from comm.model import Model
import numpy as np
import copy
import os
import shutil


class FaceCollect(Model):
    def __init__(self, user_name: str, name: str = 'exchange_face'):
        super().__init__(name)
        self.root = 'data/sl/{}/'.format(user_name)
        self.num = 0
        self.last_time = time.time()
        if os.path.exists(self.root):
            shutil.rmtree(self.root)
        if not os.path.exists(self.root):
            os.makedirs(self.root)

    def run(self, frame: dict):
        if time.time() - self.last_time < 1:
            return frame
        self.last_time = time.time()
        bboxs = frame['bboxs']
        if len(bboxs) == 1:
            bbox = bboxs[0]
            bbox = [int(i) for i in bbox]
            try:
                img = frame['img']
                face = copy.deepcopy(img[bbox[1]:bbox[3], bbox[0]:bbox[2]])
                cv2.imshow('face', face)
                cv2.waitKey(1)
                np.save(self.root + str(self.num) + '.npy', face)
                self.num += 1
            except Exception as e:
                # print(e)
                pass
        else:
            # print('请确定画面中有且只有一张人脸')
            pass


        return frame
