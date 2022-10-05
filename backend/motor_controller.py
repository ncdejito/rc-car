from pyfirmata import Arduino
import yaml

# load config as variables
with open("config.yaml", "r") as f:
    config = yaml.load(f, yaml.Loader)
    locals().update(config)

if use_motor:
    board = Arduino("/dev/ttyACM0")

    in1 = board.get_pin("d:{}:o".format(_in1))
    in2 = board.get_pin("d:{}:o".format(_in2))
    ena = board.get_pin("d:{}:p".format(_ena))
    in3 = board.get_pin("d:{}:o".format(_in3))
    in4 = board.get_pin("d:{}:o".format(_in4))
    enb = board.get_pin("d:{}:p".format(_enb))


def get_moveset():
    if use_motor:
        return {"w": forward, "a": left, "s": stop, "d": right}
    else:
        # print next line
        return {"w": print, "a": print, "s": print, "d": print}


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
