import os 
from rembg import remove
from PIL import Image
from Config import Input, Output

teste_path = str(os.path.dirname(__file__) + Input)
teste_dir = str(os.path.dirname(__file__) + Output)

print("Início")
path  = teste_path 
new_dir = teste_dir 
images = os.listdir(path)

if images:  
    for image in images:
        print(image)
        input = Image.open(path + "/" + image)
        output = output = remove(input, alpha_matting=True, alpha_matting_foreground_threshold=180,alpha_matting_background_threshold=30, alpha_matting_erode_size=5)
        output.save(new_dir + "/" + image + ".png")
else: 
    print("Não há nenhuma imagem para tratar")    
print("Fim")  