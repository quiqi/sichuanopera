# SiChuanOpera
> python模块化编程练习项目
> 

## 数据采集脚本：get_face.py
```bash
python get_face.py
```
按照脚本的要求输入名字（建议不要有中文），然后采集一百张图片

## 识别器训练脚本
```bash
python train.py
```

## 人脸识别模块：
需要从上游得到目标跟踪信息，也就是上游必须有检测和跟踪模块（DetectionFaces 和 SORT）
将给下游传递：`frame['id_name']`，表示跟踪算法得到的id号对应的人名，如果没有识别成功，会将人名标记成`stranger`(陌生人)


## levelapperance 脚本
一个示例脚本，用于演示人脸识别模块的效果


## 使用方式：
1. 安装依赖包: ` pip install opencv-contrib-python`
2. 录入人脸: `python get_face.py`
3. 训练识别器: `python train.py`
4. 使用人脸识别脚本测试: `python levelapperance.py`
