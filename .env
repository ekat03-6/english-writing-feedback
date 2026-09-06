from fastapi import FastAPI, Form 
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel 

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

# 受け取るJSONのデータ型を追加します
class EssayRequest(BaseModel):
    topic: str
    essay: str


@app.get("/")
def home():
    return FileResponse("templates/writing.html")


# 受け取り方を「Form」から「JSON」に変更
@app.post("/submit")
def submit(request: EssayRequest):
    print(request.topic)
    print(request.essay)

    return {"message": "received"}