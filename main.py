from fastapi import FastAPI
from models import Action
from engine import TollEnv # Import your engine

app = FastAPI()
env = TollEnv() # Initialize it here

@app.post("/reset")
async def reset(task_id: int = 0):
    return env.reset(task_id)

@app.post("/step")
async def step(action: Action):
    obs, reward, done, info = env.step(action)
    return {"observation": obs, "reward": reward, "done": done, "info": info}

@app.get("/state")
async def get_state():
    return {"state": env.state}