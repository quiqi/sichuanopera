from comm.model import Model
import cv2


class DrawBbox(Model):
    def __init__(self, name: str = 'DrawBbox'):
        super().__init__(name)

    def run(self, frame: dict):
        face = frame['face']
        # faces = frame['bboxs']

        img = frame['img']
        # TODO: 画bbox框
        # 标记位置 说明：(x,y)为绘制的边框的左上角 （x+w，y+h）为绘制的边框的右下角 （255， 0， 0）为RGB三色值 1为线条的粗细值
        for face in face:   # list，但其实不是
            t = []
            for i in face:
                t.append(int(i))
            print(t)
            # img = cv2.rectangle(img, (t[0], t[1]), (t[2], t[3]), (255, 0, 0), 1)
            img = cv2.rectangle(img, (t[0], t[1]), (t[0] + t[2], t[1] + t[3]), (255, 0, 0), 1)
            # img = cv2.putText(img, str(t[-1]), (t[0], t[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
        frame['img'] = img
        return frame
