import os
import cv2

path = 'C:/Users/srini/ImagesP105'
Images = []

for file in os.listdir(path):
    name,extension = os.path.splitext(file)
    print(name)

    if extension in ['.gif','.png','.jpg','.jpeg','.jfif']:
        file_name = path + '/' + file
        #print(file_name)

        Images.append(file_name)
        count = len(Images)

        frame = cv2.imread(Images[0])
        width,height,Channels = frame.shape
        size = (width,height)
        #print(size)

        out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DVIX'),0.8,size)

        for i in range(0,count-1):
            frame = cv2.imread(Images[i])
            out.write(frame)
        
print('Done')