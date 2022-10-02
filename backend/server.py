from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pyfirmata import Arduino

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

board = Arduino("/dev/ttyACM0")

speed = 0.6  # l298n=0.3, vnh2sp30=0.6

# Dual VNH2SP30
_ena = 5
_enb = 6
_in1 = 8
_in2 = 7
_in3 = 9
_in4 = 4

in1 = board.get_pin("d:{}:o".format(_in1))
in2 = board.get_pin("d:{}:o".format(_in2))
ena = board.get_pin("d:{}:p".format(_ena))
in3 = board.get_pin("d:{}:o".format(_in3))
in4 = board.get_pin("d:{}:o".format(_in4))
enb = board.get_pin("d:{}:p".format(_enb))


def forward():
    in1.write(1)
    in2.write(0)
    in3.write(1)
    in4.write(0)
    ena.write(speed)
    enb.write(speed)


def left():
    in1.write(1)
    in2.write(0)
    in3.write(0)
    in4.write(1)
    ena.write(speed)
    enb.write(speed)


def right():
    in1.write(0)
    in2.write(1)
    in3.write(1)
    in4.write(0)
    ena.write(speed)
    enb.write(speed)


def stop():
    in1.write(0)
    in2.write(0)
    in3.write(0)
    in4.write(0)
    ena.write(0)
    enb.write(0)


@app.get("/{key}")
async def main(key):
    print(f"Received: {key}")
    move = {"w": forward, "a": left, "s": stop, "d": right}
    move[key]()
    return {"message": "Hello World"}
