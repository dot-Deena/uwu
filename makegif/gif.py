import imageio.v3 as img  
from PIL import Image
import numpy as np

# resizing images
img1 = Image.open('isagi.png')
img2 = Image.open('barou.png')
img2 = img2.resize(img1.size)

# Convert the images to numpy arrays
img1_array = np.array(img1)
img2_array = np.array(img2)

images = [img1_array,img2_array]

img.imwrite('isagibarou.gif',images, duration=700, loop = 0)