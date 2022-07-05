# 油画特效
# 将 frame['img'] 转化成油画风格， 然后存到 frame['canva'] 中

import cv2
from comm.model import Model


class SketchEffect(Model):
    def __init__(self, name: str = 'sketch_effect'):
        super().__init__(name)

    def run(self, frame: dict):
        img = frame['img']
        sketch = None
        # 你的代码
        # TODO: 将 img 转化为 canva
        # 结束你的代码
        frame['sketch'] = sketch
        return frame