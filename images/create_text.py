from PIL import Image
from string import letters
import os

def crop(dest, input, height, width):
    k = 0
    im = Image.open(input)
    imgwidth, imgheight = im.size
    for i in range(0,imgheight,height):
        for j in range(0,imgwidth,width):
            box = (j, i, j+width, i+height)
            a = im.crop(box)
            savefile = "%s.png" % letters[k]
            if "lower" in input:
                savefile = "_" + savefile
            elif "special" in input:
                savefile = "punc%s.png" % k
            elif "numbers" in input:
                savefile = "%s.png" % k
            a.save(os.path.join(dest,savefile))
            k += 1


crop("D:\\handwriter\\images", "numbers.png", 60, 48)            
crop("D:\\handwriter\\images", "lowers.png", 60, 48)
crop("D:\\handwriter\\images", "capitals.png", 60, 48)
crop("D:\\handwriter\\images", "special_chars.png", 60, 48)