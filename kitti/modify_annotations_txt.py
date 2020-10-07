# -*- coding: UTF-8 -*-
# modify_annotations_txt.py
import glob
import string
"""
combine Truck,Van,Tram,Car,Misc into Car class. and combine 'Person_sitting','Cyclist','Pedestrian','Person' into Person class
"""
txt_list = glob.glob('/media/smart/05F013960677C1A7/Jichen_Thesis/code/kitti/label_test_480/*.txt')
print (txt_list)
def show_category(txt_list):
    category_list= []
    for item in txt_list:
        try:
            with open(item) as tdf:
                for each_line in tdf:
                    labeldata = each_line.strip().split(' ') 
                    category_list.append(labeldata[0]) # class information
        except IOError as ioerr:
            print('File error:'+str(ioerr))
    print(set(category_list)) 

def merge(line):
    each_line=''
    for i in range(len(line)):
        if i!= (len(line)-1):
            each_line=each_line+line[i]+' '
        else:
            each_line=each_line+line[i] 
    each_line=each_line+'\n'
    return (each_line)

print('before modify categories are:\n')
show_category(txt_list)

for item in txt_list:
    new_txt=[]
    try:
        with open(item, 'r') as r_tdf:
            for each_line in r_tdf:
                labeldata = each_line.strip().split(' ')
                if labeldata[0] in ['Truck','Van','Tram','Car','Misc']: # combine into "car"
                    labeldata[0] = labeldata[0].replace(labeldata[0],'car')
                if labeldata[0] in ['Person_sitting','Cyclist','Pedestrian','Person']: # combine into 'person'
                    labeldata[0] = labeldata[0].replace(labeldata[0],'person')
                if labeldata[0] == 'DontCare': # ignore 'Dontcare'
                    continue
                new_txt.append(merge(labeldata)) # rewritting
        with open(item,'w+') as w_tdf:  
            for temp in new_txt:
                w_tdf.write(temp)
    except IOError as ioerr:
        print('File error:'+str(ioerr))

print('\nafter modify categories are:\n')
show_category(txt_list)
