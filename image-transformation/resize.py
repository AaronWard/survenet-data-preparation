from PIL import Image
import os, os.path

new_hieght = 100
new_width = 100

def resize(file_name):
    img = Image.open(file_name)
    wpercent = (100/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((new_width, new_hieght), Image.ANTIALIAS)
    img.save(file_name)


image = "flipped_S005_001_00000005_cropped_.png"
resize(image)