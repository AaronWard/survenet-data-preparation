from PIL import Image
import numpy as np

def noramlize(file_name):
    #
    #
    #
    #




#Load the directory and traverse over all the image files
list = os.listdir('C:/Users/aaron/Desktop/Cropped Dataset/suprise/')
for file in list:

    file_n = file
    print(file_n)

    #error with PIL occurs so this is used to prevent
    #an OSError
    if(file_n == "desktop.ini"):
        print("AHHHH")
    else:
        flip_image(file_n)