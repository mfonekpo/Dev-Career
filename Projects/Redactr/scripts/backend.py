from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from logic import scan_stats
import uvicorn


app = FastAPI()
app.mount("/static", StaticFiles(directory="../static"), name="static")


templates = Jinja2Templates(directory="../templates")

@app.get("/", response_class=HTMLResponse)
def render_page(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("index.html", context)


@app.post("/redact", response_class=HTMLResponse)
def redact_text(request: Request, content: str = Form(...), words: str = Form(...), replacement: str = Form("****")):
    scrambled_content, matches, duration = scan_stats(content, words, replacement)
    context = {"request": request,
               "redacted_content": scrambled_content,
               "words_scanned": len(content.split()), 
               "matches": len(matches), 
               "scrambled_words": ', '.join(matches),
               "duration": f"{round(duration, 2)}"
               }
    return templates.TemplateResponse("index.html", context)


# if __name__ == "__main__":
    # uvicorn.run(app, host="0.0.0.0", port=8888)