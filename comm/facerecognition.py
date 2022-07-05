import os

import cv2
import numpy as np
from comm.model import Model
import json


class FaceRecognition(Model):
    def __init__(self, name: str = 'face_recognition'):
        super().__init__(name)
        self.recognizer = cv2.face.LBPHFaceRecognizer_create(threshold=70)
        self.recognizer.read('data/level.yml')
        with open('data/ci.json') as f:
            self.class_label = json.load(f)

    def run(self, frame: dict):
        id_name = {}
        img = frame['img']
        bboxs = frame['bboxs']
        draw = []
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        for bbox in bboxs:
            bbox = [int(i) for i in bbox]
            face = gray[bbox[1]: bbox[3], bbox[0]: bbox[2]]
            id, confid = self.recognizer.predict(face)
            if str(id) in self.class_label.keys() and confid <= 70:
                id_name[bbox[-1]] = self.class_label[str(id)]
            else:
                id_name[bbox[-1]] = 'stranger'
            draw.append([bbox, 'name:{}, confid:{}'.format(id_name[bbox[-1]], confid)])
            # cv2.imshow('face', face)
            # cv2.waitKey(1)
        frame['id_name'] = id_name
        frame['draw'] = draw
        return frame


def train(root: str = 'data/sl/'):
    recognition = cv2.face.LBPHFaceRecognizer_create()
    # 载入数据

    # 获得数据
    # 获得类目录
    cls = os.listdir(root)
    labels = []     # 存储标签
    imgs = []       # 存储图像
    class_label = {}
    for i, c in enumerate(cls):
        # 获得第 i 个人的人脸列表
        img_names = os.listdir(root + c)
        class_label[int(i)] = c
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
    with open('data/ci.json', 'w') as f:
        json.dump(class_label, f)