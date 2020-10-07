import cv2


#xmin,ymin,xmax,ymax
file = open("/home/smart/Jichen_Thesis/code/train_ali.txt", "r")
for line in file:
    print (line)
    no_images = len(line.split(' '))-1
    print (no_images)

    img_1_coo = line.split(' ')[1]
    img_2_coo = line.split(' ')[2]

    image = cv2.imread(line.split(' ')[0])

    min_1 = (int(img_1_coo.split(',')[0]),int(img_1_coo.split(',')[1]))
    max_1 = (int(img_1_coo.split(',')[2]),int(img_1_coo.split(',')[3]))
    print (min_1,max_1)
    image = cv2.rectangle(image,min_1,max_1,(0,255,0),2)

    min_2 = (int(img_2_coo.split(',')[0]),int(img_2_coo.split(',')[1]))
    max_2 = (int(img_2_coo.split(',')[2]),int(img_2_coo.split(',')[3]))
    print (min_2,max_2)
    image = cv2.rectangle(image,min_2,max_2,(255,0,0),2)

    image = cv2.resize(image,(960,640))
    cv2.imshow('img',image)

    cv2.waitKey(0)