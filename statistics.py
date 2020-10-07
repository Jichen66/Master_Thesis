import cv2

file = open("/home/smart/Jichen_Thesis/code/train_guo_final.txt", "r")
c1,p1=0,0
max = 0
i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15 = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
for line in file:
    #print (line)
    objects = len(line.split(' '))-2
    #print ('number of objects:',objects)

    data = line.split(' ')

    #image = cv2.imread(data[0])

    for i in range(objects):
        # #print(data[i+1])
        # xy_min = (int(float(data[i+1].split(',')[0])),int(float(data[i+1].split(',')[1])))
        # xy_max = (int(float(data[i+1].split(',')[2])),int(float(data[i+1].split(',')[3])))
        # font = cv2.FONT_HERSHEY_PLAIN
        distance = int(float(data[i+1].split(',')[-1]))
        if distance > max:
            max = distance
        if distance in range(0,10):
            i1 += 1
        elif distance in range(10,20):
            i2 += 1
        elif distance in range(20,30):
            i3 += 1
        elif distance in range(30,40):
            i4 += 1
        elif distance in range(40,50):
            i5 += 1
        elif distance in range(50,60):
            i6 += 1
        elif distance in range(60,70):
            i7 += 1
        elif distance in range(70,80):
            i8 += 1
        elif distance in range(80,90):
            i9 += 1
        elif distance in range(90,100):
            i10 += 1
        elif distance in range(100, 110):
            i11 += 1
        elif distance in range(110, 120):
            i12 += 1
        elif distance in range(120, 130):
            i13 += 1
        elif distance in range (130,140):
            i14 += 1
        else:
            i15 += 1

        # print (xy_min,xy_max,'distance:',distance)
        #
        label = int(float(data[i+1].split(',')[-2]))
        if label==2:
            c1 = c1 + 1
            ## person:blue  car:green
            # image = cv2.rectangle(image,xy_min,xy_max,(0,255,0),2)
            # image = cv2.putText(image,text,xy_min,font,1,(0,255,0),1)

        if label==0:
            p1 = p1 + 1
print ('car:',c1,'person:',p1)
print ('max:',max)
print (i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15)
    #         image = cv2.rectangle(image,xy_min,xy_max,(255,0,0),2)
    #         image = cv2.putText(image,text,xy_min,font,1,(255,0,0),1)
    #
    #
    # cv2.imshow('img',image)
    #
    # cv2.waitKey(0)