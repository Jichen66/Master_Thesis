# -*- coding: utf-8 -*-
import os
f = open('train_guo_final2.txt','r+',encoding='utf-8')
lines = f.readlines()
f.seek(0,0)
f.truncate()
for line in lines:
   line_new = line.replace('/media/smart/05F013960677C1A7/Jichen_Thesis/code/kitti/training/','/home/ubuntu/jichen_code/code/training_image/')
   #line_new = line.replace('/smart/Ali-Thesis/qqwweee/keras-yolo3-dist/Cam01_5m_R1/', '/ubuntu/jichen_code/code/training_image/SMART/')
   f.write(line_new)
f.close()