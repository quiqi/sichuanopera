from comm.model import Model
import cv2


class MakeUp(Model):
    def __init__(self, name: str = 'makeup'):
        super().__init__(name)
        root = 'data/facialMakeup/' # python 如何连接路径
        img_name = os.listdir(root)
        self.makeups = []
        for name in img_name:
            makeup = cv2.imread(root + name)
            self.makeups.append(makeup)
        print(img_name)

    def run(self, frame: dict):
        img = frame['img']
        bboxs = frame['bboxs']
        print(bboxs)
        for bbox in bboxs:
            h = int(bbox[3] - bbox[1])
            w = int(bbox[2] - bbox[0])
            makeup = self.makeups[int(bbox[-1]) % len(self.makeups)]
            makeup = cv2.resize(makeup, dsize=(w, h))
            mask = 255 * np.ones(makeup.shape, makeup.dtype)
            img = cv2.seamlessClone(makeup, img, mask, (int(bbox[2] + bbox[0])//2, int(bbox[3] + bbox[1])//2), cv2.NORMAL_CLONE)
        frame['img'] = img
        return frame