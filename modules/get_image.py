from urllib.request import urlopen
from PIL import Image

def get_image_from_url(url: str):
    return Image.open(urlopen(url))

    