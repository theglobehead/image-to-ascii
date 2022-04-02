from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates

from modules.get_image import get_image_from_url
from modules.conver_image import ImageConverter

app = FastAPI()
templates = Jinja2Templates(directory="static")

origins = [
    "http://localhost",
    "http://localhost:8080",
    "https://shrouded-lake-21821.herokuapp.com/",
    "http://127.0.0.1:5500/test-api.html",
    "http://127.0.0.1:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
def home_page(request: Request):
    return templates.TemplateResponse("/html/index.html", {"request": request})

@app.get("/generate", response_class=PlainTextResponse)
def generate_ascii(url: str, width: int, height: int):
    img = get_image_from_url(url)
    res = ImageConverter.generate_ascii(img, (width, height))
    return res  

@app.get("/draw", response_class=HTMLResponse)
def draw_ascii(url: str, width: int, height: int):
    img = get_image_from_url(url)
    res = ImageConverter.generate_ascii(img, (width, height))
    return f"<pre>{res}</pre>"
