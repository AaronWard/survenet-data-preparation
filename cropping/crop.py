import cv2
import os, os.path

'''
This is a file for cropping the images to only the facial area
and save to a new data set

It used the OpenCV haar cascade file to detect the facial features and crops it
'''
def facecrop(image):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    img = cv2.imread(image)

    minisize = (img.shape[1],img.shape[0])
    miniframe = cv2.resize(img, minisize)

    faces = face_cascade.detectMultiScale(miniframe)

    for f in faces:
        x, y, w, h = [ v for v in f ]
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,255,255))
        sub_face = img[y:y+h, x:x+w]
        fname, ext = os.path.splitext(image)
        cv2.imwrite(fname+"_cropped_"+ext, sub_face)
    return


list = os.listdir('C:/Users/aaron/Desktop/Updated CK+ dataset/Colored - sadness/')
for file in list:

    file_name = file
    facecrop('C:/Users/aaron/Desktop/Updated CK+ dataset/Colored - sadness/' + file_name)
