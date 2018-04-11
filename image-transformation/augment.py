from PIL import Image
import os, os.path
import numpy as np
import Augmentor
import skimage
from skimage import data, io, filters


'''
This script is used for augmenting images slightly

'''
# # Augment images for angry
# p = Augmentor.Pipeline('C:/Users/aaron/Desktop/model-training-tensorflow/data/testing/angry')
# p.random_distortion(probability=1, grid_width=4, grid_height=4, magnitude=7)
# p.sample(152)

# # Augment images for fear
# p = Augmentor.Pipeline('C:/Users/aaron/Desktop/model-training-tensorflow/data/testing/fear')
# p.random_distortion(probability=1, grid_width=4, grid_height=4, magnitude=7)
# p.sample(196)


# # Augment images for happy
# p = Augmentor.Pipeline('C:/Users/aaron/Desktop/model-training-tensorflow/data/testing/happy')
# p.random_distortion(probability=1, grid_width=4, grid_height=4, magnitude=7)
# p.sample(21)

# # Augment images for neutral
# p = Augmentor.Pipeline('C:/Users/aaron/Desktop/model-training-tensorflow/data/testing/neutral')
# p.random_distortion(probability=1, grid_width=4, grid_height=4, magnitude=7)
# p.sample(90)

# # Augment images for sadness
# p = Augmentor.Pipeline('C:/Users/aaron/Desktop/model-training-tensorflow/data/testing/sadness')
# p.random_distortion(probability=1, grid_width=4, grid_height=4, magnitude=7)
# p.sample(135)

# # Augment images for suprise
# p = Augmentor.Pipeline('C:/Users/aaron/Desktop/model-training-tensorflow/data/testing/suprise')
# p.random_distortion(probability=1, grid_width=4, grid_height=4, magnitude=7)
# p.sample(111)


####################################################################################################