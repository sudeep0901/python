import matplotlib.pyplot as pyplot
import matplotlib.image as mpimg
import numpy as np
img = mpimg.imread(r'src\matplotlib\stinkbug.png')

print(len(img), type(img))

imgplot = pyplot.imshow(img)
pyplot.show()


ar = [np.random.randn(1000), np.random.randn(10000), np.random.randn(10000)]
lum_img =  img[:, :, 0]
pyplot.imshow(lum_img)

pyplot.show()
pyplot.imshow(lum_img, cmap="hot")
pyplot.colorbar()



pyplot.show()

pyplot.hist(lum_img.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k')
pyplot.show()

from PIL import Image

img = Image.open(r'src\matplotlib\stinkbug.png')
img.thumbnail((64, 64), Image.ANTIALIAS)  # resizes image in-place
imgplot = pyplot.imshow(img)
pyplot.show()

imgplot = pyplot.imshow(img, interpolation="nearest")
