from comm.model import Model
import cv2


class GetCamera(Model):  # 图片读取模块
    # 子类应该继承父类的：除了构造函数之外的所有成员函数和成员变量
    def __init__(self, name: str = 'get_camera'):
        # 构造函数
        super().__init__(name)
        self.camera = cv2.VideoCapture(0)

    def run(self, frame: dict):
        ret, img = self.camera.read()
        frame['img'] = img
        return frame
