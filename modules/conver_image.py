from math import ceil
from urllib.request import urlopen
from PIL import Image

class ImageConverter:
    #symbols = [" ","`","'",":",";",'"',"*","^","+","#","@"]    
    symbols = [".", ",", ":", "+", ";", "=", "x", "X", "Æ", "%", "$", "&", "¶", "@"]
    symbols.reverse()

    @classmethod
    def generate_ascii(cls, image: Image, size: tuple):
        width, height = size

        image = image.resize(size).convert('L')
        px = image.load()

        result = ""

        for line_n in range(height):
            for col_n in range(width):
                result += cls.symbols[ceil((px[col_n, line_n] / 255)*(len(cls.symbols)-1))]*2
            result += "\n"

        return result

#print(ImageConverter.generate_ascii(Image.open(urlopen("https://tinypng.com/images/social/website.jpg")),
#    (70, 40)
#))