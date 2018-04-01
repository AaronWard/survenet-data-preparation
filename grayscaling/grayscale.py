from PIL import Image
import numpy as np
import os, os.path

img_path = 'C:/Users/aaron/Desktop/Cropped Dataset/happy/' 

def grayify(file_name):
      image = Image.open(img_path + file_name)
      image = image.convert('L')
      image.save(img_path + file_name)

#Load the directory and traverse over all the image files
list = os.listdir(img_path)
for file in list:

    file_n = file
    print(file_n)

    #error with PIL occurs so this is used to prevent
    #an OSError
    if(file_n == "desktop.ini"):
        print("AHHHH")
    else:
        grayify(file_n)
