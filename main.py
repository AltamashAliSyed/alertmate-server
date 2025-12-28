from fastapi import FastAPI
from pydantic import BaseModel
from state_tracker import DriverState

app = FastAPI(title="AlertMate Simple AI")

state = DriverState()

class DetectData(BaseModel):
    eye_closed: bool
    yawning: bool

@app.get("/")
def root():
    return {"status": "AlertMate Server Running"}

@app.post("/detect")
def detect(data: DetectData):
    alert = False
    reason = None

    if data.eye_closed:
        if state.eye_closed_3s():
            alert = True
            reason = "EYE_CLOSED_3_SEC"
    else:
        state.reset_eye()

    if data.yawning:
        if state.yawn_3s():
            alert = True
            reason = "YAWN_3_SEC"
    else:
        state.reset_yawn()

    return {
        "alert": alert,
        "reason": reason
    }
