from comm.model import Model
import cv2


class Show(Model):
    def __init__(self, name: str = 'Show'):
        super().__init__(name)

    def run(self, frame: dict):
        # 4. 显示图片
        img = frame['img']
        cv2.imshow('img', img)
        cv2.waitKey(1)
        return frame
