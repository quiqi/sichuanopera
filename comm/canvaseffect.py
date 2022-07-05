# 油画特效
# 将 frame['img'] 转化成油画风格， 然后存到 frame['canvas'] 中

import cv2
from comm.model import Model


class CanvasEffect(Model):
    def __init__(self, name: str = 'canvas_effect'):
        super().__init__(name)

    def run(self, frame: dict):
        img = frame['img']
        canvas = None
        # 你的代码
        # TODO: 根据 img 生成油画风格的
        # 结束你的代码
        frame['canvas'] = canvas
        return frame