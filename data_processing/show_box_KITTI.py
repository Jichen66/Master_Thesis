# -*- coding: UTF-8 -*-
'''
show ground truth bounding box and distance for the KITTI images
'''
import os
import cv2

objects = 0
name = '007022'
label_path = "/home/smart/Jichen_Thesis/code/kitti/training/label_whole/"
image_path = "/media/smart/05F013960677C1A7/Jichen_Thesis/code/Cam01_val/"
file = open(label_path+name+'.txt', "r")
image = cv2.imread(image_path + name + '.png')
for line in file:
    objects += 1
    data = line.split(' ')
    xy_min = (int(float(data[4])), int(float(data[5])))
    xy_max = (int(float(data[6])), int(float(data[7])))
    font = cv2.FONT_HERSHEY_PLAIN
    distance = str(data[-2])
    print(xy_min, xy_max, 'distance:', distance)
    label = str(data[0])
    if label == 'Car':
        ## person:blue  car:green
        image = cv2.rectangle(image, xy_min, xy_max, (0,255,0),2)
        image = cv2.putText(image, distance, xy_min, font, 1, (0,255,0), 1)
    if label == 'Person':
        image = cv2.rectangle(image, xy_min, xy_max, (255,0,0), 2)
        image = cv2.putText(image, distance, xy_min, font, 1, (255,0,0), 1)

print('number of objects:', objects)
cv2.imshow('img', image)
cv2.waitKey(0)