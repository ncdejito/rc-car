# rc-car

![](proof.gif)

## Software
* React - can [add](https://www.youtube.com/watch?v=A3nw2M47K50&t=1555s) a video component later on if I want to stream an RPi camera
* FastAPI - no need to write custom C++ firmware code using pyfirmata
* Ubuntu Core 22
* Docker Buildx - can add a container app sending autonomous movement commands to FastAPI later on

## Hardware
* Arduino
* RPi4
* L298N motor driver - can be replaced by L293D to make compatible for stronger motors for bigger cars (like a delivery robot)
* Robot body - wiring diagram from [OpenBot](https://github.com/isl-org/OpenBot/tree/master/body/diy#option-1-diy), modified smartphone brain with RPi

## Run on dev machine
1. In terminal 1, run backend
```
cd backend
poetry install
source $(poetry env info --path)/bin/activate
python main.py
```

1. In terminal 2, run frontend
```
cd frontend
npm start
```

## Run on RPi4
Use docker instructions described in backend/README.md and frontend/README.md

## References
* OpenBot: Turning Smartphones into Robots [paper](https://arxiv.org/abs/2008.10631)
