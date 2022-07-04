from comm.model import Model
import tools.sort as sort
import numpy as np


class SORT(Model):
    def __init__(self, name: str = 'SORT'):
        super().__init__(name)
        self.sort = sort.Sort()

    def run(self, frame: dict):
        faces = frame['face']
        bboxs = []
        # (x, y, w, h) -> (x1, y1, x2, y2)
        for (x, y, w, h) in faces:
            bboxs.append([x, y, x+w, y+h])
        # 转化为 np
        bboxs = np.array(bboxs)
        if len(bboxs) == 0:
            bboxs = self.sort.update()
        else:
            bboxs = self.sort.update(bboxs)
        frame['bboxs'] = bboxs
        return frame