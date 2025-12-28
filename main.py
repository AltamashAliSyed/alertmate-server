from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
import time

app = FastAPI(title="AlertMate AI Server")

# simple timer logic (demo)
eye_start = None
yawn_start = None

@app.get("/")
def root():
    return {"status": "AlertMate Server Running"}

@app.post("/upload")
async def upload_image(request: Request):
    global eye_start, yawn_start

    image = await request.body()
    if len(image) < 1000:
        return PlainTextResponse("false")

    # 🔴 DEMO LOGIC (replace with real AI later)
    # simulate eye closed after 3 sec
    now = time.time()
    if eye_start is None:
        eye_start = now

    if now - eye_start >= 3:
        return PlainTextResponse("true")

    return PlainTextResponse("false")
