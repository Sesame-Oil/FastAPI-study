from fastapi.responses import FileResponse
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def 작명():
    return FileResponse('index.html')

@app.get("/favicon.ico")