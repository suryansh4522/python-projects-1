import imageio.v3 as iio
filenames = ['shukla.jpg','shukla2.jpg']
images = []
for filename in filenames:
    images.append(iio.imread(filename))
iio.imwrite('shukla.gif', images, duration=500, loop = 0)