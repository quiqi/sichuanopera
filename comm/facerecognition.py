import os

import cv2
import numpy as np
from comm.model import Model


class FaceRecognition(Model):
    def __init__(self, name: str = 'face_recognition'):
        super().__init__(name)
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.recognizer.read('data/level.yml')

    def run(self, frame: dict):
        img = frame['img']
        bboxs = frame['bboxs']
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        for bbox in bboxs:
            bbox = [int(i) for i in bbox]
            face = gray[bbox[1]: bbox[3], bbox[0]: bbox[2]]
            id, confid = self.recognizer.predict(face)
            print('id:{}, confid:{}'.format(id, confid))
            cv2.imshow('face', face)
            cv2.waitKey(1)
        return frame




def train(root: str = 'data/sl/'):
    recognition = cv2.face.LBPHFaceRecognizer_create()
    # 载入数据

    # 获得数据
    # 获得类目录
    cls = os.listdir(root)
    labels = []     # 存储标签
    imgs = []       # 存储图像
    for i, c in enumerate(cls):
        # 获得第 i 个人的人脸列表
        img_names = os.listdir(root + c)
        for img_name in img_names:
            labels.append(i)
            img = np.load(root + c + '/' + img_name)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            imgs.append(img)
            cv2.imshow('f', imgs[-1])
            cv2.waitKey(1)

    # 训练
    recognition.train(imgs, np.array(labels))
    recognition.write('data/level.yml')