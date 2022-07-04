from comm.model import Model
import cv2


class Flip(Model):
    def __init__(self, name: str = 'Flip'):
        super().__init__(name)

    def run(self, frame: dict):
        img = frame['img']
        img = cv2.flip(img, 1)
        frame['img'] = img
        return frame
