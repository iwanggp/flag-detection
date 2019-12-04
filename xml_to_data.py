# -*- coding: utf-8 -*-
# @Time    : 2019/10/17 9:27 PM
# @Author  : gpwang
# @File    : xml_to_data.py
# @Software: PyCharm
import os
from xml.etree import ElementTree


# 经XML文件修改为YOlo可识别的格式
class XML_preprocessor(object):
    def __init__(self, data_path):
        self.data_path = data_path
        self.data = []
        self._preprocess_XML()

    def _preprocess_XML(self):
        filenames = os.listdir(self.data_path)
        print(filenames)
        for filename in filenames:
            temp = []
            if filename == '.DS_Store':
                continue
            tree = ElementTree.parse(self.data_path + filename)
            root = tree.getroot()
            image_name = root.find('filename').text
            temp.append('model_data/train/' + image_name)
            for object_tree in root.findall('object'):
                for bounding_box in object_tree.iter('bndbox'):
                    xmin = float(bounding_box.find('xmin').text)
                    ymin = float(bounding_box.find('ymin').text)
                    xmax = float(bounding_box.find('xmax').text)
                    ymax = float(bounding_box.find('ymax').text)
                class_name = object_tree.find('name').text
                temp.append(str(int(xmin)) + "," + str(int(ymin)) + "," + str(int(xmax)) + "," + str(
                    int(ymax)) + "," + str(int(class_name) - 1))

            self.data.append(temp)


data = XML_preprocessor('label_train/').data
with open('model_data/kitti_simple_label.txt', 'w') as file:
    for cutWords in data:
        file.write(' '.join(cutWords) + '\n')
