import uvicorn
from openenv_core.env_server import create_app
from .engine import TollPlazaEngine

engine = TollPlazaEngine()
app = create_app(engine)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)