import sys
from PIL import Image, ImageOps

#testing to make sure correct number of arguments are given
if len(sys.argv) < 3 :
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')

#testing to make sure that arguments are images and of same file type
if sys.argv[1][-4:] != '.jpg' and sys.argv[1][-5:] != '.jpeg' and sys.argv[1][-4:] != '.png':
    sys.exit('Invalid output')
elif sys.argv[2][-4:] != '.jpg' and sys.argv[2][-5:] != '.jpeg' and sys.argv[2][-4:] != '.png':
    sys.exit('Invalid output')

if (sys.argv[1][-4:] == '.jpg' and sys.argv[2][-4:] != '.jpg') or (sys.argv[1][-5:] == '.jpeg' and sys.argv[2][-5:] != '.jpeg') or (sys.argv[1][-4:] == '.png' and sys.argv[2][-4:] != '.png'):
    sys.exit('Input and output have different extensions')
else:
    pass
  
#using the Image module to overlay the shirt onto the given image
try:
    with Image.open(sys.argv[1]) as image:
        with Image.open("shirt.png") as shirt:
            image_copy = image.copy()
            shirt_copy = shirt.copy()
            fit_image = ImageOps.fit(image_copy,(600,600),centering=(0.0,0.5))
            fit_image.paste(shirt_copy,(0,0),shirt_copy)
            fit_image.save(sys.argv[2])
except FileNotFoundError:
    sys.exit('Input does not exist')
