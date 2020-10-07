#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
extract ground truth box and distance for each object
"""
import os
import string
import numpy as np

#fo = open("train_guo_final.txt","w")
fo = open("train_guo_final2.txt","w")   ## label.txt
dict = {'Car':1, 'Person':0}
path="/media/smart/05F013960677C1A7/Jichen_Thesis/code/kitti/training/label/"  # reading path
path_list=os.listdir(path)
path_list.sort() 
i_0,i_1,i_2,i_3 = 0,0,0,0
for file_name in path_list:
    full_path = os.path.join(path, file_name)
    name = file_name[:-4]  # extract filename before.txt
    img_name = name + '.png'
    img_path = os.path.join('/media/smart/05F013960677C1A7/Jichen_Thesis/code/kitti/training/image/', img_name) 
    fo.write(img_path)
    fo.write(' ')
    txt = open(full_path)
    split_lines = txt.readlines()
    for split_line in split_lines:
        line=split_line.strip().split()

        fo.write(str(int(float(line[4]))) + ',')
        fo.write(str(int(float(line[5]))) + ',')
        fo.write(str(int(float(line[6]))) + ',')
        fo.write(str(int(float(line[7]))) + ',')
        fo.write(str(dict[line[0]]) + ',')
        fo.write(str(float(line[-2]))+ ' ')
        #fo.write(str(float(np.sqrt(np.square(float(line[-2]))+np.square(float(line[-4]))))) + ' ')

    fo.write('\n')
fo.close()


