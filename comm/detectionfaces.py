from comm.model import Model
import cv2


class DetectionFace(Model):
    def __init__(self, name: str = 'DetectionFace'):
        super().__init__(name)
        self.face_cascade = cv2.CascadeClassifier("data/haarcascade_frontalface_default.xml")

    def run(self, frame: dict):
        img = frame['img']
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 灰度化
        # 显示图片（渲染画面）
        face = self.face_cascade.detectMultiScale(img,  # 输入的灰度图像
                                              scaleFactor=1.1,  # 图像缩放的比例
                                              minNeighbors=5,  # 构成目标矩形的最少相邻矩形个数
                                              minSize=(30, 30),  # 目标尺寸的最小大小
                                              flags=cv2.CASCADE_SCALE_IMAGE)
        frame['face'] = face    # 将新得到的数据写入 frame，传到下游
        return frame
