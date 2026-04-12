from fastapi import FastAPI
from crisis_environment import CrisisEnvironment

app = FastAPI()
env = CrisisEnvironment()

@app.get("/reset")
def reset():
    return env.reset()

@app.post("/step")
def step(action: dict):
    return env.step(action)