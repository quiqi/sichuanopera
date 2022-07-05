import cv2
from comm.model import Model
import numpy as np
import copy


class ExchangeFace(Model):
    def __init__(self, name: str = 'exchange_face'):
        super().__init__(name)

    def run(self, frame: dict):
        img = frame['img']
        faces = frame['face']
        if len(faces) == 0:
            return frame
        face_img = []
        bboxs = []
        for (x, y, w, h) in faces:
            cx = x + w/2
            cy = y + h/2
            x1 = int(cx - 0.4 * w)
            y1 = int(cy - 0.4 * h)
            x2 = int(cx + 0.4 * w)
            y2 = int(cy + 0.4 * h)
            bboxs.append([x1, y1, x2, y2])
        bboxs = np.array(bboxs)
        # print('bbox1:{}'.format(bboxs))
        bboxs = bboxs[np.argsort(bboxs[:, 0])]
        # print('bbox2:{}'.format(bboxs))

        for (x1, y1, x2, y2) in bboxs:
            face_img.append(copy.deepcopy(img[y1:y2, x1:x2]))
            cv2.imshow('face', face_img[-1])
            cv2.waitKey(1)

        for i, (x1, y1, x2, y2) in enumerate(bboxs):
            t_img = face_img[(i+1) % len(bboxs)]
            t_img = cv2.resize(t_img, dsize=(x2-x1, y2-y1))
            mask = 255 * np.ones(t_img.shape, t_img.dtype)
            img = cv2.seamlessClone(t_img, img, mask, (int(x1 + x2)//2, int(y1 + y2)//2), cv2.NORMAL_CLONE)
        frame['img'] = img
        return frame


