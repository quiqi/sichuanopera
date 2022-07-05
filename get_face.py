import comm
from comm.model import Model
import cv2
import numpy as np
import os


if __name__ == '__main__':
    name = input('please input your name:')
    print('好看的{}您好，接下来将会录入您的帅脸，请等待摄像头开启'.format(name))
    print('1. 为了保证人脸数据的多样性，请在录入过程中缓慢摇头和点头，有眼镜的同学请戴上眼镜然后摘下眼镜。')
    print('2. 请确保只有一张人脸会入镜，包括照片。')
    print('3. 录入过程大概将持续100~200秒，请选择光线较好的位置进行数据采集')
    task = [
        comm.getcamera.GetCamera(),     # 读取摄像头
        comm.flip.Flip(),
        comm.detectionfaces.DetectionFace(),
        comm.sort.SORT(),
        comm.facecollect.FaceCollect(name),
        comm.show.Show()
    ]
    t_num = task[4].num
    while task[4].num < 100:
        frame = {}
        try:
            for model in task:
                frame = model.run(frame)
            if t_num != task[4].num:
                t_num = task[4].num
                print('采集进度：{}/{}'.format(task[4].num, 100))
        except Exception as e:
            print(e)