import numpy as np
from PIL import Image

w = 4
h = 4
data = np.zeros((h, w, 3), dtype=np.uint8)
data[1, 1] = [255, 0, 0]
data[3, :] = [255, 255, 255]
data[:, 3] = [255, 255, 255]
img = Image.fromarray(data, 'RGB')
img.save('input.png')
img.show()