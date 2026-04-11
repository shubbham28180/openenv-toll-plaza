import uvicorn
from openenv_core.env_server import create_app
from .engine import TollPlazaEngine
from .models import Action, Observation

# Sirf class bhejna hai, bracket nahi
app = create_app(
    TollPlazaEngine, 
    Action, 
    Observation, 
    env_name="toll_plaza_env"
)

# Is line ki zaroorat nahi hai HF pe, par rehne do niche
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)