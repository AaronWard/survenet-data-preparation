import os, os.path
import math
from PIL import Image

old_path = "C:/Users/aaron/Desktop/Cropped Dataset/happy/"

new_train_path = 'C:/Users/aaron/Desktop/data/training/happy/'
new_test_path = 'C:/Users/aaron/Desktop/data/testing/happy/'

#Load the directory and traverse over all the image files
list = os.listdir(old_path)

# define the size of the first 80 percent of images
num_files = len(list)
num_training_files = num_files * .8
num_training_files = math.ceil(num_training_files)

num_testing_file = num_files * .2
num_testing_file = math.ceil(num_testing_file)

print("num files: ", num_files)
print("num training files: ", num_training_files)
print("num testing files: ", num_testing_file)


#Add the first 80 percent to the training folder
for img in list[1:num_training_files]: 
    i = Image.open(old_path + img)
    i.save(new_train_path+img)


#Add the remaining 20 percent to the training folder
for img in list[num_training_files:]:
    i = Image.open(old_path + img)
    i.save(new_test_path+img)