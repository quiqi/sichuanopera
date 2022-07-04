from comm.model import Model
import cv2


class ChalkEffects(Model):
    def __init__(self, name: str = 'ChalkEffects'):
        super().__init__(name)

    def run(self, frame: dict):
        img = frame['img']
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 灰度化
        img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                    cv2.THRESH_BINARY, 5, 3)
        img = cv2.bitwise_not(img)
        frame['img'] = img
        return frame
