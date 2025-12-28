from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
import time

app = FastAPI(title="AlertMate AI Server")

eye_start = None

@app.get("/")
def root():
    return {"status": "AlertMate Server Running"}

@app.post("/upload")
async def upload_image(request: Request):
    global eye_start

    image = await request.body()

    # ignore invalid frames
    if len(image) < 2000:
        eye_start = None
        return PlainTextResponse("false")

    now = time.time()

    # start timer
    if eye_start is None:
        eye_start = now
        return PlainTextResponse("false")

    # trigger only after 3 seconds CONTINUOUS
    if now - eye_start >= 3:
        return PlainTextResponse("true")

    return PlainTextResponse("false")
