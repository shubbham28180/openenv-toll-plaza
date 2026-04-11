import uvicorn
from openenv_core.env_server import create_app
from .engine import TollPlazaEngine  # Ya TollEnv jo bhi aapka class name hai
from .models import Action, Observation

# DHAYAN DEIN: Yahan bracket () nahi lagane hain
# Galt: engine = TollPlazaEngine()
# Sahi: engine = TollPlazaEngine

app = create_app(
    TollPlazaEngine,  # Sirf class ka naam, bracket nahi!
    Action, 
    Observation, 
    env_name="toll_plaza_env"
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)