#
#
#   App
#
#

import gradio as gr

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from pages.page_1 import app as page_1_app
from pages.page_2 import app as page_2_app


app = FastAPI()


gradio_apps = [
    {
        "title": "Page 1",
        "app": page_1_app,
        "path": "page_1"
    },
    {
        "title": "Page 2",
        "app": page_2_app,
        "path": "page_2"
    }
]

for gradio_app in gradio_apps:
    app = gr.mount_gradio_app(app, gradio_app["app"], path="/gradio/" + gradio_app["path"])

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
@app.get("/app/{path_name:path}")
def index(request: Request, path_name: str = ""):
    if not path_name:
        return RedirectResponse(url="/app/" + gradio_apps[0]["path"])

    return templates.TemplateResponse("index.html", {
        "request": request,
        "gradio_apps": gradio_apps,
        "current_path": path_name,
    })
