from PIL import Image
import glob

imagelist = []

for filename in glob.glob('img/*'):
	im= Image.open(filename)
	imagelist.append(im)

size=128

new_im = Image.new('RGB', (256,256))

x=0
y=0

for im in imagelist:
	if x == 256:
		y = y + size
		x=0
	im.thumbnail((size, size))
	new_im.paste(im, (x,y))
	x = x + size

new_im.save('collage.png')