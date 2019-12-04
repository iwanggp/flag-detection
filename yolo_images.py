# -*- coding: utf-8 -*-
# @Time    : 2019/10/31 08:26 PM
# @Author  : gpwang
# @File    : yolo_images.py
# @Software: PyCharm
import os

import matplotlib.pyplot as plt
from PIL import Image
from tqdm import tqdm

from yolo import YOLO

path_test = "./sample/"
path_test_1 = ""
path_result = "./result/result.csv"


# 检测图片
def detect_img(yolo, path_result):
    filenames = os.listdir(path_test)
    info = []
    for filename in tqdm(filenames):
        img_path = path_test + filename
        try:
            image = Image.open(img_path)
            r_image, temp = yolo.detect_image(image)
            plt.imshow(r_image)
            plt.show()
            temp.insert(0, filename)
            info.append(temp)
        except Exception as e:
            print("错误文件：" + img_path)

    with open(path_result, 'w')as file:
        for cutWords in info:
            file.write('\t'.join(cutWords) + '\n')


if __name__ == '__main__':
    detect_img(YOLO(), path_result)
