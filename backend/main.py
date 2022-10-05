from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import motor_controller

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

moveset = motor_controller.get_moveset()


@app.on_event("startup")
async def app_startup():
    print("Moveset loaded:")
    print(moveset)


@app.get("/{key}")
async def main(key):
    msg = f"Received: {key}"
    print(msg)
    moveset[key]()
    return {"message": msg}


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
