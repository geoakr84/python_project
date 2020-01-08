from PIL import Image
from PIL import PSDraw


catIm = Image.open('zophie.png')
catCopyIm=catIm.copy()



catIm=catIm.resize((600,800), Image.ANTIALIAS)

width=catIm.size[0]
height=catIm.size[1]

im = Image.new('RGBA', (100, 200), 'purple')

catIm.save('newzophie.png')

im.save('im.png')

croppedIm = catIm.crop((235, 245, 465, 460))
croppedIm=croppedIm.resize((100,100), Image.ANTIALIAS)
croppedIm.save('cropped.png')
croppedIm.rotate(270).save('rotated270.png')
rotated270=Image.open('rotated270.png')


catCopyIm.paste(croppedIm,(50,50))
catCopyIm.paste(croppedIm,(280,350))
catCopyIm.paste(rotated270, (50,350))
catCopyIm.save('catCopyIm.png')

SQUARE_FIT_SIZE = 300
LOGO_FILENAME= 'logocat.png'

logoim=Image.open(LOGO_FILENAME)
logowidth, logoheight = logoim.size

catCopyIm.paste(logoim, (width - logowidth, height - logoheight), logoim)

print ("Width: ",width," Height: ",height)

