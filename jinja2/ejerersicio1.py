from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="fast apiconjinja2")

app.mount('/recurso', StaticFiles(directory='recursos'), name = "recursos")

miPlantilla = Jinja2Templates(directory="templates")

@app.get("/inicio", response_class=HTMLResponse)
async def read_item(request: Request):
    return miPlantilla.TemplateResponse("index.html", {"request":request})
