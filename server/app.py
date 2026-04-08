from fastapi import FastAPI
from openenv_core.env_server import create_app
from .engine import TollEnv
from .models import Action, Observation

# Initialize environment
env = TollEnv()

# Create OpenEnv compliant FastAPI app
app = create_app(
    env, 
    Action, 
    Observation, 
    env_name="toll_plaza_env"
)

@app.get("/")
async def health():
    return {"status": "running", "env": "Toll Plaza"}