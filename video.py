import sys, os
import argparse
from yolo import YOLO, detect_video
from PIL import Image
os.environ["CUDA_VISIBLE_DEVICES"] = ""

####### notice which weight file did yolo.py load !!!!!!!!#########

if __name__ == '__main__':
    detect_video(YOLO(),"/home/smart/Desktop/dashcam/2014_1122_122434_035A.mp4")

    #2014_1122_122434_035A
    #detect_video(YOLO(), "/home/smart/2.mp4")
    #detect_video(YOLO(), "/home/smart/pp.avi")
    #detect_video(YOLO(),"/home/smart/Desktop/dashcam/2014_1122_121545_034AA.mp4")



