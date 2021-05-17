import os
import sys
from PIL import Image

size = (128, 128)

path = os.getcwd() + "/assets/images"
for filename in os.listdir(path):
    infile = path+"/"+filename
    outfile = os.path.splitext(infile)[0] + ".thumbnail.jpg"
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                im.thumbnail(size)
                im.save(outfile, "JPEG")
                print(outfile)
        except OSError:
            print("cannot create thumbnail for", infile)
