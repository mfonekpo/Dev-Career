from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="../static"), name="static")


templates = Jinja2Templates(directory="../templates")

@app.get("/index", response_class=HTMLResponse)
def render_page(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("index.html", context)













# @app.get("/")
# def read_root(request: Request):
#     return templates.TemplateResponse("form.html", {"request": request, "response": None})

# @app.post("/redact/")
# def redact_content(
#     request: Request,
#     text: str = Form(...), 
#     redact_words: str = Form(...), 
#     scramble_with: Optional[str] = Form("****")
# ):
#     # [Redaction logic remains the same...]
    
#     return templates.TemplateResponse("form.html", {"request": request, "response": response})