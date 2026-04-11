import random
from openenv_core.base_env import Environment
from .models import Action, Observation

class TollPlazaEngine(Environment):  # Yahan Environment add kiya hai
    def __init__(self):
        super().__init__()
        self.step_count = 0

    async def reset(self):
        self.step_count = 0
        return Observation(
            vehicle_count=random.randint(0, 50),
            avg_speed=40.0,
            current_status="Normal"
        )

    async def step(self, action: Action):
        self.step_count += 1
        status = "Congested" if action.action == 1 else "Clear"
        
        obs = Observation(
            vehicle_count=random.randint(10, 100),
            avg_speed=random.uniform(20.0, 60.0),
            current_status=status
        )
        
        return obs, 1.0, self.step_count >= 10, {"step": self.step_count}

    def close(self):
        pass