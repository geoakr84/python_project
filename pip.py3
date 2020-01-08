from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


cat=[100,98,65,96,120]
namecat=['a','b','c','d','e']
rectangle = Image.new('RGB', (300,300), (255,255,255))
draw=ImageDraw.Draw(rectangle)
for x in range(5):
	for w in range(20):
		for y in range(299,299-cat[x],-1):
			rectangle.putpixel(((x*40)+w,y),(127,127,127))

draw.text((0,0),"Sample Text",(0,0,0))


rectangle.save('graph.png')