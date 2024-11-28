import os 
from rembg import remove
from PIL import Image

path  = input('Enter images Directory: ')
new_dir = input('Enter new Directory for the images: ')
images = os.listdir(path)


for image in images:
    input = Image.open(path)
    output = remove(input)
    output.save(new_dir)