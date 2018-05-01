import urllib
import urllib.request
import cv2

fname = "products_original.txt"
base_url = "http://www.niko.eu/niko/images/"
path_destination = "ripped_png/"

with open(fname) as f:
    content = f.readlines()
content = [x.strip() for x in content] # remove whitespace characters like `\n` at the end of each line

counter = 0
for product in content:

    url = base_url + product + ".jpg"
    print("ripping " + product + "  url: " + url)
    urllib.request.urlretrieve(url, path_destination + "a" +product + ".png")  #urllib.urlretrieve(base_url, product+".jpg")
    counter +=1

print("images ripped", counter)


#print(content)

