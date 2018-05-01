# source: https://stackoverflow.com/questions/10607468/how-to-reduce-the-image-file-size-using-pil

#test voorbeeld: https://www.my-smarthome.be/niko-enkelvoudige-drukknop-met-ledpure-bakelite-br.html

from os import walk
import numpy as np
from PIL import Image
import cv2

path = "ripped_png/"   #"img/"
path_destination = "result_png/"


# Read all files in dir
f = []
for (dirpath, dirnames, filenames) in walk(path):
    f.extend(filenames)
    break

print(f)
for img_file in f:
    print(img_file)
    im = cv2.imread(path+ img_file, cv2.IMREAD_UNCHANGED)  # read also transparency (alpha) channel

    #print(im[100][50])
    #row, col = im.shape[:2]
    #bottom = im[row - 2:row, 0:col]
    #mean = cv2.mean(bottom)[0]

    color = [255,255,255]
    bordersize = 110
    border = cv2.copyMakeBorder(im, top=bordersize, bottom=bordersize, left=bordersize, right=bordersize,
                                borderType=cv2.BORDER_CONSTANT, value=color)
    cv2.imwrite(path_destination + img_file, border)

    #cv2.imshow('image', im)
    #cv2.imshow('bottom', bottom)
    #cv2.imshow('border', border)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()


