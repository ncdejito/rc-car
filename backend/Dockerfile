FROM arm64v8/python:3.8-slim

SHELL ["/bin/bash", "-c"]

WORKDIR /code

COPY requirements.txt /code/requirements.txt

RUN python3 -m pip install --upgrade pip

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code

ENV use_motor=False

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
