import time

class DriverState:
    def __init__(self):
        self.eye_start = None
        self.yawn_start = None

    def eye_closed_3s(self):
        if self.eye_start is None:
            self.eye_start = time.time()
        return (time.time() - self.eye_start) >= 3

    def reset_eye(self):
        self.eye_start = None

    def yawn_3s(self):
        if self.yawn_start is None:
            self.yawn_start = time.time()
        return (time.time() - self.yawn_start) >= 3

    def reset_yawn(self):
        self.yawn_start = None
