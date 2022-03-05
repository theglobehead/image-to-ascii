from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from modules.get_image import get_image_from_url
from modules.conver_image import ImageConverter

app = FastAPI()

@app.get("/generate")
def generate_ascii(url: str, width: int, height: int):
    img = get_image_from_url(url)
    res = ImageConverter.generate_ascii(img, (width, height))
    print(res)
    return res  

@app.get("/draw", response_class=HTMLResponse)
def draw_ascii(url: str, width: int, height: int):
    img = get_image_from_url(url)
    res = ImageConverter.generate_ascii(img, (width, height))
    print(res)
    return f"<pre>{res}</pre>"