import comm
from comm.model import Model
import cv2
import numpy as np
import os


if __name__ == '__main__':
    task = [
        comm.getcamera.GetCamera(),     # 读取摄像头
        comm.flip.Flip(),
        comm.detectionfaces.DetectionFace(),
        comm.exchangefaces.ExchangeFace(),
        # comm.drawbbox.DrawBbox(),
        comm.show.Show()
    ]
    while True:
        frame = {}
        try:
            for model in task:
                frame = model.run(frame)
        except Exception as e:
            print(e)

