# react-fastapi-keyboard-listener

## Usage
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

## Rationale
why k8s on rpi
* when deploying ros node, need separate pod/container for it - ros is hard to setup, docker ros makes it easier to deploy
* configuring docker network is hard vs k8s services
* modular, scalable, high availability architecture
Why no: experimental device mounting