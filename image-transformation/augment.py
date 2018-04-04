from PIL import Image
import os, os.path
import numpy as np
import Augmentor

'''
This script is used for augmenting images slightly

'''
# Augment images for angry
p = Augmentor.Pipeline('C:/Users/aaron/Desktop/Cropped Dataset/angry')
p.random_distortion(probability=1, grid_width=4, grid_height=4, magnitude=7)
p.sample(609)

# Augment images for happy
p = Augmentor.Pipeline('C:/Users/aaron/Desktop/Cropped Dataset/happy')
p.random_distortion(probability=1, grid_width=4, grid_height=4, magnitude=7)
p.sample(81)

# Augment images for neutral
p = Augmentor.Pipeline('C:/Users/aaron/Desktop/Cropped Dataset/neutral')
p.random_distortion(probability=1, grid_width=4, grid_height=4, magnitude=7)
p.sample(358)

# Augment images for sadness
p = Augmentor.Pipeline('C:/Users/aaron/Desktop/Cropped Dataset/sadness')
p.random_distortion(probability=1, grid_width=4, grid_height=4, magnitude=7)
p.sample(541)

# Augment images for suprise
p = Augmentor.Pipeline('C:/Users/aaron/Desktop/Cropped Dataset/suprise')
p.random_distortion(probability=1, grid_width=4, grid_height=4, magnitude=7)
p.sample(445)

# Augment images for fear
p = Augmentor.Pipeline('C:/Users/aaron/Desktop/Cropped Dataset/fear')
p.random_distortion(probability=1, grid_width=4, grid_height=4, magnitude=7)
p.sample(784)