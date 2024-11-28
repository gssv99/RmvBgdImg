import os 
from rembg import remove
from PIL import Image
from Config import Input, Output


teste_path = str(os.path.dirname(__file__) + Input)
teste_dir = str(os.path.dirname(__file__) + Output)

print("Iniciou")
path  = teste_path 
new_dir = teste_dir 
images = os.listdir(path)

for image in images:
    print(image)
    input = Image.open(path + "/" + image)
    output = remove(input)
    output.save(new_dir + "/" + image)
    
print("Fim")  