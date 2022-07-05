from comm.model import Model
import cv2


class DrawBbox(Model):
    def __init__(self, name: str = 'DrawBbox'):
        super().__init__(name)

    def run(self, frame: dict):
        if 'draw' in frame.keys():
            img = frame['img']
            draw = frame['draw']
            # TODO: 画bbox框
            # 标记位置 说明：(x,y)为绘制的边框的左上角 （x+w，y+h）为绘制的边框的右下角 （255， 0， 0）为RGB三色值 1为线条的粗细值
            for (bbox, s) in draw:  # list，但其实不是
                face = [int(i) for i in bbox]
                img = cv2.rectangle(img, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (255, 0, 0), 1)
                img = cv2.putText(img, s, (face[0], face[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255),2)
            frame['img'] = img
        return frame
