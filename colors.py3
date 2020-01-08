from PIL import Image

im=Image.open("test.png")

width=im.size[0]
height=im.size[1]

print(width, 'x', height, '=', width*height)

new_im= Image.new('RGB', (width*height, 300), (255, 255, 255))
myimage=Image.new('RGB', (200,200), (255,255,0))

x=0
for i in range(0, height):
	for j in range(0, width):
		r,g,b= im.getpixel((j,i))

		new_im.putpixel((x, 290 - r), (255, 0, 0))
		new_im.putpixel((x, 290 - g), (0, 255, 0))
		new_im.putpixel((x, 290 - b), (0, 0, 255))

		x= x + 1
h=0
for k in range(200):
	for j in range(h):
		myimage.putpixel((k,j), (127,255,0))
	h=h+1	

new_im.save('rgb.png')
myimage.save('allwhite.png')
