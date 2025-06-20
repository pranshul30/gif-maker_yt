import imageio.v3 as iio

file=['1.png','2.png']
images=[ ]

for i in file:
  images.append(iio.imread(i))
  
iio.imwrite('3.gif',images,duration=200,loop=0)  