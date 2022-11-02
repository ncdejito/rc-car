# rc-car

![](proof.gif)

## Software
* React - with Reactive Programming
* FastAPI
* Ubuntu Core 22
* Docker Buildx

## Hardware
* Arduino
* RPi4
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
