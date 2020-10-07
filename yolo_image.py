## uses trained weights to draw detected bounding box and distance on input image

import sys, os
import argparse
from yolo import YOLO, detect_video
from PIL import Image
os.environ["CUDA_VISIBLE_DEVICES"] = ""

def detect_img(yolo):
    while True:
        img = input('Input image filename:')
        try:
            image = Image.open(img)
        except:
            print('Open Error! Try again!')
            continue
        else:
            r_image = yolo.detect_image(image)
            r_image.show()
    yolo.close_session()

if __name__ == '__main__':
    detect_img(YOLO())

