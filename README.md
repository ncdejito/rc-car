# rc-car

![](proof.gif)

## Software
* React - with Reactive Programming
* FastAPI
* Ubuntu Core 22

## Hardware
* Arduino
* Rpi4

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