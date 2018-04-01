from PIL import Image
import os, os.path

'''
This script is used for flipping images. Using this will double the size of the dataset and
improve accuracy because the model will be better trained on variance.
'''
def flip_image(file_name):
    
    im = Image.open('C:/Users/aaron/Desktop/Cropped Dataset/suprise/' + file_name)
    new_file_name = "flipped_" + file_name #Retitles the image name
    im.transpose(Image.FLIP_LEFT_RIGHT).save('C:/Users/aaron/Desktop/Cropped Dataset/suprise/' + new_file_name) #Save it to the same folder as the original images

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