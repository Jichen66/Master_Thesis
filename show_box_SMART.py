import cv2
"""
show ground truth box and distance in SMART dataset
"""
#xmin,ymin,xmax,ymax
file = open("/home/smart/Jichen_Thesis/code/train_ali.txt", "r")
for line in file:
    print (line)
    no_images = len(line.split(' '))-1
    print (no_images)

    img_1_coo = line.split(' ')[1]
    img_2_coo = line.split(' ')[2]

    image = cv2.imread(line.split(' ')[0])

    font = cv2.FONT_HERSHEY_PLAIN
    distance1 = str(int(img_1_coo.split(',')[-1]))+'m'
    distance2 = str(int(img_2_coo.split(',')[-1]))+'m'
    min_1 = (int(img_1_coo.split(',')[0]),int(img_1_coo.split(',')[1]))
    max_1 = (int(img_1_coo.split(',')[2]),int(img_1_coo.split(',')[3]))
    print (min_1,max_1,distance1)
    image = cv2.rectangle(image,min_1,max_1,(255,0,0),2)
    image = cv2.putText(image, distance1, min_1, font, 3, (255, 0, 0),3)

    min_2 = (int(img_2_coo.split(',')[0]),int(img_2_coo.split(',')[1]))
    max_2 = (int(img_2_coo.split(',')[2]),int(img_2_coo.split(',')[3]))
    print (min_2,max_2,distance2)
    image = cv2.rectangle(image,min_2,max_2,(255,0,0),2)
    image = cv2.putText(image, distance2, min_2, font, 3, (255, 0, 0), 3)

    image = cv2.resize(image,(960,640))
    cv2.imshow('img',image)

    cv2.waitKey(0)