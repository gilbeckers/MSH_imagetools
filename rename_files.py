from os import walk
import os

path = "ripped/"


# Read all files in dir
f = []
for (dirpath, dirnames, filenames) in walk(path):
    f.extend(filenames)
    break

for fname in f:
    os.rename(path+fname, path+ "a" + fname)

