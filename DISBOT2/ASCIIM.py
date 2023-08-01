import PIL
import requests as req
import os
import time,random,PIL
from PIL import Image
from io import BytesIO
#Начало АСКИИ
def ASCII(new_width,path):
  
    ASCII_CHARS = ['.',"'",'^',':','"','*','-','~','+','=','s','n','A','G','#','$','%','&','@']

    try:
        new_width=int(new_width)
    except:
        (new_width,"is not a valid number")
     
    def resize_image(image, new_width):
        width, height = image.size
        ratio = height/width/2.1
        new_height = int(new_width * ratio)
        resized_image = image.resize((new_width, new_height))
        return(resized_image)

    def grayify(image):
        grayscale_image = image.convert("L")
        return(grayscale_image)

    def pixels_to_ascii(image):
        pixels = image.getdata()
        characters = "".join([ASCII_CHARS[pixel//15] for pixel in pixels])
        return(characters)

    def main(new_width,path):
    
       try:
           response = req.get(path)
           image = Image.open(BytesIO(response.content))
       except:
           print(image)
           print(path,"is not a valid pathname to an image.")
        
       new_image_data = pixels_to_ascii(grayify(resize_image(image,new_width)))

       pixel_count = len(new_image_data)
       ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0,pixel_count,new_width))

       return(ascii_image)

    return(main(new_width,path))
#конец
