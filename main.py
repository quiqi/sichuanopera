import comm


if __name__ == '__main__':
    task = [
        comm.getcamera.GetCamera(),     # 读取摄像头
        comm.flip.Flip(),
        comm.detectionfaces.DetectionFace(),
        comm.sort.SORT(),
        comm.drawbbox.DrawBbox(),
        comm.show.Show()
    ]
    while True:
        frame = {}
        for model in task:
            frame = model.run(frame)

