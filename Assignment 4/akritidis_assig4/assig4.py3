from PIL import Image
import glob

img1=Image.open("img/Kalmar.png") #command to open each image in a separate variable
img2=Image.open("img/Kalmar_slott.png")
img3=Image.open("img/Kronoberg.png")
img4=Image.open("img/LNU_library.png")
img5=Image.open("img/Resecentrum_Vaxjo.png")
img6=Image.open("img/Teleborgs.jpg")
img7=Image.open("img/Vaxjochurch.png")
img8=Image.open("img/Vaxo_University.jpg")
img9=Image.open("img/White_lake.png")

tup=()
sum=0
x=0

width=img1.size[0]  #variable for thw width of the photo
height=img1.size[1]  #variable for the height of the photo
for i in range(0, height): #I take all the pixels from 0 to last for the height axis
	for j in range(0, width): #the same as above for the width
		tup=img1.getpixel((j,i))[:3]  #I extract only the first three columns to take the rgb color
		sum= sum + tup[0] #I add the values of the first column which is the red color
		x= x + 1 #increment to count how many lines the pictures has
average=sum/x #divide the sum of the pixels with the number of lines to get the average value
average= str(round(average,2)) #command to round the average value in a two decimal float number

tup2=()  #I do the same for the rest of the photos similarly to the above case
sum2=0
x2=0
average2=0

width2=img2.size[0]
height2=img2.size[1]
for i in range(0, height2):
	for j in range(0, width2):
		tup2=img2.getpixel((j,i))[:3]
		sum2= sum2 + tup2[0]
		x2= x2 + 1
average2=sum2/x2
average2= str(round(average2,2))

tup3=()
sum3=0
x3=0
average3=0

width3=img3.size[0]
height3=img3.size[1]
for i in range(0, height3):
	for j in range(0, width3):
		tup3=img3.getpixel((j,i))[:3]
		sum3= sum3 + tup3[0]
		x3= x3 + 1
average3=sum3/x3
average3= str(round(average3,2))

tup4=()
sum4=0
x4=0
average4=0

width4=img4.size[0]
height4=img4.size[1]
for i in range(0, height4):
	for j in range(0, width4):
		tup4=img4.getpixel((j,i))[:3]
		sum4= sum4 + tup4[0]
		x4= x4 + 1
average4=sum4/x4
average4= str(round(average4,2))

tup5=()
sum5=0
x5=0
average5=0

width5=img5.size[0]
height5=img5.size[1]
for i in range(0, height5):
	for j in range(0, width5):
		tup5=img5.getpixel((j,i))[:3]
		sum5= sum5 + tup5[0]
		x5= x5 + 1
average5=sum5/x5
average5= str(round(average5,2))

tup6=()
sum6=0
x6=0
average6=0

width6=img6.size[0]
height6=img6.size[1]
for i in range(0, height6):
	for j in range(0, width6):
		tup6=img6.getpixel((j,i))[:3]
		sum6= sum6 + tup6[0]
		x6= x6 + 1
average6=sum6/x6
average6= str(round(average6,2))

tup7=()
sum7=0
x7=0
average7=0

width7=img7.size[0]
height7=img7.size[1]
for i in range(0, height7):
	for j in range(0, width7):
		tup7=img7.getpixel((j,i))[:3]
		sum7= sum7 + tup7[0]
		x7= x7 + 1
average7=sum7/x7
average7= str(round(average7,2))

tup8=()
sum8=0
x8=0
average8=0

width8=img8.size[0]
height8=img8.size[1]
for i in range(0, height8):
	for j in range(0, width8):
		tup8=img8.getpixel((j,i))[:3]
		sum8= sum8 + tup8[0]
		x8= x8 + 1
average8=sum8/x8
average8= str(round(average8,2))

tup9=()
sum9=0
x9=0
average9=0

width9=img9.size[0]
height9=img9.size[1]
for i in range(0, height9):
	for j in range(0, width9):
		tup9=img9.getpixel((j,i))[:3]
		sum9= sum9 + tup9[0]
		x9= x9 + 1
average9=sum9/x9
average9= str(round(average9,2))

imagelist2 = []
averagelist= [] #I create this empty list to insert the values of the nine average values I found
averagelist.extend([average,average2,average3,average4,average5,average6,average7,average8,average9])

for filename in glob.glob('img/*'): #command to find all the photos in the directory img
	imagelist2.append(filename) #I append them to the empty list I created above

finalist=[]

for a,b in zip(imagelist2,averagelist): #I chain the values of imagelist2 and averagelist in one list
	finalist.append((a,b))

finalist=sorted(finalist,key=lambda x:float(x[1])) #sort in ascending mode
print("The average values of the red color are the following")
print("===========================================================")


for t in finalist:
	print(t)

print("===========================================================")

imagelist=[]
sortedlist=[x[0] for x in finalist] #a list which contains the path of the photos in the order presented before(sorted from smallest tp bigger)

for pic in sortedlist:  
		im=Image.open(pic) 
		imagelist.append(im) 


size1=213 #width of each photo inside the collage
size2=160 #height of each photo inside the collage

new_pic= Image.new('RGB', (639,480)) #creation of a new picture with these dimensions

x=0
y=0

for pic in imagelist:
	if x == 639: #this means when three pictures are already inserted (213 * 3) the width will reach its maximum pixel
		y = y+ size2 
		x=0 #so create a new line
	pic.thumbnail((size1,size2)) #here I set the dimensions of each thumbnail
	new_pic.paste(pic, (x,y)) #I pasted them all in one picture
	x= x + size1

new_pic.save('collage.png')
print("Collage has been created")



			




		
