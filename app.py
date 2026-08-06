from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


@app.get("/")
def home():
    return FileResponse("templates/writing.html")


@app.post("/submit")
def submit(
    topic: str = Form(...),
    essay: str = Form(...)
):
    print(topic)
    print(essay)

    return {"message": "received"}